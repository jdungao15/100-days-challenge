from flask import Flask, render_template
import requests

res = requests.get("https://api.npoint.io/b6a90f6e92287d955f90")
posts_data = res.json()

app = Flask(__name__)


@app.route('/')
def home():
    posts = posts_data
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def show_post(post_id):
    for post in posts_data:
        if post_id == post['id']:
            post_data = {
                'title': post['title'],
                'subtitle': post['subtitle'],
                'body': post['body'],
                'author': post['author'],
                'date': post['date']
            }
            return render_template('post.html', post=post_data)
    pass


@app.route('/form', methods=['GET'])
def receive_data():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
