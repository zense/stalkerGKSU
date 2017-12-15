from flask import Flask, render_template, request, flash
import get_nodes
from flask_sqlalchemy import SQLAlchemy
import json
import os
from rq import Queue
from rq.job import Job
from worker import conn
import uuid
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = "some_secret"
db = SQLAlchemy(app)
mail = Mail(app)

q = Queue(connection=conn)

import emails
from models import *

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

def save_info(organisation, email_address):
	key = str(uuid.uuid4())
	info = db.session.query(User.github_username, User.name).filter_by(organisation = organisation).all()
	if(info == []):		# Another entry in the queue could have updated the DB
		items = get_nodes.main(organisation)
		for i in items:
			usr = User(organisation,i.name,i.github_username)
			db.session.add(usr)
		db.session.commit()
	emails.send_email(organisation, [email_address])
	return key

@app.route("/query", methods = ['GET', 'POST'])
def query():
	if(request.method == 'POST'):
		organisation = request.form['organisation']
		email_address = request.form['email_address']
		filename = organisation + ".html"
		info = db.session.query(User.github_username, User.name).filter_by(organisation = organisation).all()
		if(info == []):
			job = q.enqueue_call(
				func="routes.save_info", args=(organisation, email_address, ), result_ttl=5000, timeout=600
			)
			flash("We shall notify you at " + email_address + " when the processing is complete")
		else:
			lists = []
			for i in info:
				lists.append([str(i.github_username), str(i.name)])
			get_nodes.creating_objs(lists, organisation)
			return render_template(filename, organisation=str(organisation)+'.json')
	return render_template('query.html')

@app.route("/aboutus")
def contactus():
    return render_template('aboutUs.html')

if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host = "0.0.0.0", port = port, threaded = True)
