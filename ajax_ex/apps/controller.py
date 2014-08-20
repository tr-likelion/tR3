from flask import render_template, Flask, request, jsonify
from apps import app


@app.route('/_add_numbers')
def add_numbers():
	a=request.args.get('a', 0, type=int)
	b=request.args.get('b', 0, type=int)
	return jsonify(result=a+b)


@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")