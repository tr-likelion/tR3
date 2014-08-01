# -*- coding: utf-8 -*-
# flask_mvc.py
# all the imports

from flask import request, redirect, url_for,\
	render_template
from apps import app
from database import Database

dataStorage = Database()

@app.route('/', methods=['GET', 'POST'])
def show_entries():
	entries = dataStorage.out()
	return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
	storage={}

	storage['num'] = dataStorage.num
	storage['count'] = 0
	storage['count1'] = (storage['count'] +1) - 1
	storage['title'] = request.form['title']
	storage['contents'] = request.form['contents']

	dataStorage.put(storage)
	dataStorage.num += 1

	return redirect(url_for('show_entries'))

@app.route('/del/<idx>', methods=['GET'])
def del_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			dataStorage.database.remove(data)
			break

	return redirect(url_for('show_entries'))

@app.route('/plus/<idx>', methods=['GET'])
def plus_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			data['count'] += 1
			break

	#dataStorage.database = sorted(dataStorage.database, key=lambda list: list['count'], reverse=True)

	return redirect(url_for('show_entries'))

@app.route('/minus/<idx>', methods=['GET'])
def minus_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			data['count1'] -= 1
			break


	#dataStorage.database = sorted(dataStorage.database, key=lambda list: list['count1'], reverse=True)

	return redirect(url_for('show_entries'))


@app.route('/modify/<idx>', methods=['GET'])
def modify_entry(idx):
	for data in dataStorage.database:
		if int(idx) == data['num']:
			data['title'] = request.args['title']
			data['contents'] = request.args['contents']
			break

	return redirect(url_for('show_entries'))


@app.route('/order/<idx>', methods=['GET'])
def order_entry(idx):
	dataStorage.database = sorted(dataStorage.database, key=lambda list: list['count'], reverse=True)
	return redirect(url_for('show_entries'))

@app.route('/unorder/<idx>', methods=['GET'])
def unorder_entry(idx):
	dataStorage.database = sorted(dataStorage.database, key=lambda list: list['count'])
	return redirect(url_for('show_entries'))






