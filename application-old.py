import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, json, jsonify, session
import omdb
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/search', methods=['POST'])
def search():
	term = request.form['keyword']
	session['keyword'] = term
	res = omdb.get(title=term, tomatoes=True)
	imdb_rating = res.imdb_rating
	term = res.title
	plot = res.plot
	tomato_rating = res.tomato_rating
	overall_rating = 8.9
	youtube_rating = 4.6
	twitter_rating = 6.3
	if (tomato_rating=="N/A"):
		tomato_rating = tomato_rating.replace("/", "")
	overall_img = "Images/" + str(math.trunc(overall_rating)) + ".png"
	twitter_img = "Images/" + str(math.trunc(twitter_rating)) + ".png"
	youtube_img = "Images/" + str(math.trunc(youtube_rating)) + ".png"
	imdb_img = "Images/" + imdb_rating.split('.', 1)[0] + ".png"
	tomato_img = "Images/" + tomato_rating.split('.', 1)[0] + ".png"
	return render_template('ratings.html', keyword=term, plot=plot, imdb_rating=imdb_rating, youtube_rating=youtube_rating, \
		tomato_rating=tomato_rating, twitter_rating=twitter_rating, overall_rating=overall_rating, overall_img=overall_img, \
		youtube_img=youtube_img, twitter_img=twitter_img, imdb_img=imdb_img, tomato_img=tomato_img)

@app.route('/twitter', methods=['POST'])
def twitter():
	term = session.get('keyword', None)
	return render_template('twitter.html', keyword=term, twitter_comment=comment_list)

@app.route('/youtube', methods=['POST'])
def youtube():
	term = session.get('keyword', None)
	return render_template('youtube.html', keyword=term, youtube_comment=comment_list)

if __name__ == '__main__':
    app.run(
        host="",
        port=int("5000"),
        debug=True
    )