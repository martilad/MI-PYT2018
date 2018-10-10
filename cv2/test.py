

import flask
import jinja2


app = flask.Flask(__name__)

@app.route('/')
def index():
	return "Test pyt"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = 'anonymous'):
	return flask.render_template('hello.tml', username = name)
	#return f"Hello {name}"

@app.route('/square/<int:n>')
def square(n):
	return str(n**2)

@app.template_filter('camel')
def camel_case_filter(txt):
	return ''.join(t.title() for t in txt.split('_'))

@app.route('/nav')
def navigation():
	url = flask.url_for('square', n=10)
	return '<a href="{}"> square of 10 </a>'.format(url)
	#lepsi lze menit url adresy nezavisle
	#return '<a href="/square/10"> square of 10 </a>'

