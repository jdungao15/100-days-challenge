from flask import Flask, render_template
import datetime
import requests
app = Flask(__name__)


@app.route('/')
def home():
    today = datetime.datetime.now()
    return render_template('index.html', year=today.year)

@app.route('/guess/<name>')
def guess(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    data = response.json()
    res = requests.get(f"https://api.agify.io/?name={name}")
    age_data = res.json()
    return render_template('index.html', name=name, gender=data['gender'], age=age_data['age'])

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    res = requests.get(blog_url)
    all_posts = res.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)