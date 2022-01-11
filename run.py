from flask import Flask,render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    posts = []
    return render_template("index.html", num_posts=len(posts))


@app.route("/post/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)


@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)



@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        next_url = request.args.get('next', None)
        if next_url:
            return redirect(next_url)
        return redirect(url_for('index'))
    return render_template("signup.html")


# if __name__ == "__run__":
#     app.run(debug=True, port=8001)


app.config.update(
    FLASK_APP="Curso",
)
