from flask import render_template,current_app
from werkzeug.exceptions import NotFound, abort

from app.models import Post
from . import public_bp


@public_bp.route("/")
def index():
    # current_app.logger.info('Mostrando los posts del blog') #show log info in console
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)


@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    post = Post.get_by_slug(slug)
    if post is None:
        # abort(404)
        raise NotFound(slug)
    return render_template("public/post_view.html", post=post)

