import datetime

from flask import Blueprint
from flask import url_for, render_template, request
from flask_login import login_required, current_user
from sqlalchemy import desc

from youtube_summary import Youtube
from models import VideoLib
from app import db

main = Blueprint('main', __name__)


@main.route('/profile')
@login_required
def profile():
    user_id = current_user.id
    video_info = VideoLib.query.filter_by(user_id=user_id).order_by(desc(VideoLib.search_date)).all()
    return render_template('profile.html', name=current_user.name, video_info=video_info)


@main.route("/", methods=['GET'])
@login_required
def home():
    return render_template("index.html", summary={
        "title": 'SummarizeTube',
        "thumbnail_url": url_for('static', filename='img/youtube_summary_banner.png'),
        "publish_date": 'publish_date',
        "author": 'ashutosh64@amityonline.com',
        "page_content": 'Youtube Video Summary Generator',
        "summary": 'Youtube Video Summary Generator'
    })


@main.route("/get_summary")
def get_summary():
    youtube_url = request.args['url']
    youtube = Youtube()
    videoInfo = youtube.generate_summary(youtube_url)
    video = VideoLib(user_id=current_user.id, video_url=youtube_url, title=videoInfo['title'],
                     summary=videoInfo['summary'])
    db.session.add(video)
    db.session.commit()
    return videoInfo["summary"]


@main.route("/get_thumbnail")
def get_thumbnail():
    youtube_url = request.args['url']
    youtube = Youtube()
    summary = youtube.load_video_info(youtube_url)
    return summary
