from flask import Flask, render_template, request
import requests
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    res = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    blog_data = res.json()
    all_posts = [Post(blog['title'], blog['subtitle'], blog['body'], blog['id']) for blog in blog_data]
    return render_template("index.html", posts=all_posts)


@app.route('/post/<post_id>')
def get_post(post_id):
    title = request.args.get('title')
    subtitle = request.args.get('subtitle')
    body = request.args.get('body')

    return render_template('post.html', title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
