import httplib2
import hashlib

from flask import render_template, redirect, request, flash

from . import app, db
from .models import Url

BASE_LINK = "http://localhost:5000/"


def url_exists(url):
    h = httplib2.Http()
    try:
        resp = h.request(url, 'HEAD')
        if resp[0].status == 200:
            return True
    except (httplib2.RelativeURIError, httplib2.ServerNotFoundError):
        return False


def random_key(link, length=4):
    hash = hashlib.sha1(link.encode("UTF-8")).hexdigest()
    return hash[:length]


def shorten_link(url):
    if url_exists(url):
        long_link = Url.query.filter_by(url=url).first()
        # Check is the same link is already shortened
        if long_link is not None:
            return BASE_LINK + long_link.random_code
        unique_hash = random_key(url)
        short_link = Url(unique_hash, url)
        db.session.add(short_link)
        db.session.commit()
        return BASE_LINK + unique_hash


def expand_link(code):
    link = Url.query.filter_by(random_code=code).first()
    if link is not None:
        return link.url


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=["POST"])
def form():
    url = request.form['url']
    short_url = shorten_link(url)
    if not short_url:
        flash("Link doesn't exist")
        return render_template("index.html")
    return render_template('shortened.html', url=short_url)


@app.route('/<string:handler>')
def handle_url(handler=None):
    link = expand_link(handler)
    if not link:
        # Returns to the main page if the url is not presented in the database
        return redirect('/', code=302)
    else:
        return redirect(link, code=302)


@app.errorhandler(404)
def handle_error(e):
    return render_template("404.html"), 404