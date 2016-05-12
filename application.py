import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, json, jsonify
import omdb

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
	print 'hello'
	term = request.form['keyword']
	print term
	res = omdb.get(title=term)
	rating = res.imdb_rating
	return render_template('ratings.html', rate=rating)

if __name__ == '__main__':
    app.run(
        host="",
        port=int("5000"),
        debug=True
    )