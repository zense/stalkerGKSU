from flask import Flask, render_template, request
import get_nodes

app = Flask(__name__)

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
		get_nodes.main(organisation)
		return render_template(filename)

@app.route("/aboutus")
def contactus():
    return render_template('aboutUs.html')

if __name__ == '__main__':
	app.run(debug = True, port = 3000)
