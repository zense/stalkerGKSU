from flask import Flask, render_template, request
import get_nodes
from flask_sqlalchemy import SQLAlchemy
import json
import os

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "some_secret"

db = SQLAlchemy(app)

from models import *

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/query", methods = ['GET', 'POST'])
def query():
	if(request.method == 'GET'):
		return render_template('query.html')
	else:
		organisation = request.form['organisation']
		filename = organisation + ".html"
		info = db.session.query(User.github_username, User.name).filter_by(organisation = organisation).all()
		if(info == []):
			items = get_nodes.main(organisation)
			for i in items:
				usr = User(organisation,i.name,i.github_username)
				db.session.add(usr)
			db.session.commit()
		else:
			lists = []
			for i in info:
				lists.append([str(i.github_username), str(i.name)])
			get_nodes.creating_objs(lists, organisation)
		return render_template(filename, organisation = str(organisation) + '.json')

@app.route("/aboutus")
def contactus():
    return render_template('aboutUs.html')

if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host = "0.0.0.0", port = port)
