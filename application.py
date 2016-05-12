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
	imdb_rating = res.imdb_rating
	plot = res.plot
	overall_rating = 8
	youtube_rating = 4
	twitter_rating = 6
	return render_template('ratings.html', keyword=term, plot=plot, imdb_rating=imdb_rating, twitter_rating=twitter_rating, \
		youtube_rating=youtube_rating, overall_rating=overall_rating)

if __name__ == '__main__':
    app.run(
        host="",
        port=int("5000"),
        debug=True
    )