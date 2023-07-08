import re
import logging

from flask import Flask, render_template, request

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="/tmp/youtube_viewer.log",
    filemode="a",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)


app = Flask(__name__)
VIDEO_ID_REGEX = re.compile(r"v=([0-9A-Za-z_-]{11}).*")


@app.route("/")
def index():
    youtube_url = request.args.get("url")
    supposed_video_ids = VIDEO_ID_REGEX.findall(youtube_url)

    if not supposed_video_ids:
        logger.error(f"No video id found in url: {youtube_url}")
        return render_template("not_found.html", youtube_url=youtube_url)

    video_id = supposed_video_ids[0]
    return render_template("index.html", video_id=video_id)
