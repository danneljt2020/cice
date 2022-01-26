from flask import render_template, current_app, redirect, url_for, request
from flask_login import current_user
from werkzeug.exceptions import NotFound, abort

from app.models import Post, Comment
from . import public_bp
from .form import CommentForm


@public_bp.route("/")
def index():
    # current_app.logger.info('Mostrando los posts del blog') #show log info in console
    page = int(request.args.get('page', 1))
    post_pagination = Post.all_paginated(page, 4)
    return render_template("public/index.html", post_pagination=post_pagination)


@public_bp.route("/p/<string:slug>/", methods=['GET', 'POST'])
def show_post(slug):
    post = Post.get_by_slug(slug)
    if not post:
        abort(404)
    form = CommentForm()
    if current_user.is_authenticated and form.validate_on_submit():
        content = form.content.data
        comment = Comment(content=content, user_id=current_user.id,
                          user_name=current_user.name, post_id=post.id)
        comment.save()
        return redirect(url_for('public.show_post', slug=post.title_slug))
    return render_template("public/post_view.html", post=post, form=form)

