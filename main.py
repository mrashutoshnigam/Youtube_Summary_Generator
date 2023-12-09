from flask import Blueprint
from flask import url_for, render_template, request
from flask_login import login_required, current_user
from youtube_summary import Youtube

main = Blueprint('main', __name__)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


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
@login_required
def get_summary():
    youtube_url = request.args['url']
    youtube = Youtube()
    summary = youtube.generate_summary(youtube_url)
    return summary


@main.route("/get_thumbnail")
@login_required
def get_thumbnail():
    youtube_url = request.args['url']
    youtube = Youtube()
    summary = youtube.load_video_info(youtube_url)
    return summary
