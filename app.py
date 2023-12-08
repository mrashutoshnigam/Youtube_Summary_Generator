# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello():
#     return 'Hello, World!'


import datetime
from flask import Flask, redirect, url_for, render_template, request
from youtube_summary import Youtube

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html", summary={
        "title": 'SummarizeTube',
        "thumbnail_url": url_for('static', filename='img/youtube_summary_banner.png'),
        "publish_date": 'publish_date',
        "author": 'ashutosh64@amityonline.com',
        "page_content": 'Youtube Video Summary Generator',
        "summary": 'Youtube Video Summary Generator'
    })


@app.route("/", methods=['POST'])
def home_post():
    youtube_url = request.form.get('tbox_youtube_url')
    youtube = Youtube()
    summary = youtube.generate_summary(youtube_url)
    return render_template('index.html', summary=summary)


@app.route("/get_summary")
def get_summary():
    youtube_url = request.args['url']
    youtube = Youtube()
    summary = youtube.generate_summary(youtube_url)
    return summary


@app.route("/get_thumbnail")
def get_thumbnail():
    youtube_url = request.args['url']
    youtube = Youtube()
    summary = youtube.load_video_info(youtube_url)
    return summary


if __name__ == "__main__":
    app.run(debug=True)
