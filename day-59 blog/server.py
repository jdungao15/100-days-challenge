from flask import Flask, render_template, request
import requests
import smtplib
import os

MY_EMAIL = os.environ.get('GMAIL_ADDRESS')
MY_PASSWORD = os.environ.get('GMAIL_PASSWORD')
print(MY_EMAIL, MY_PASSWORD)

res = requests.get("https://api.npoint.io/b6a90f6e92287d955f90")
posts_data = res.json()

app = Flask(__name__)


def sent_message(name, email, phone, message):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")


@app.route('/')
def home():
    posts = posts_data
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


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


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name, email, phone, message)

        sent_message(name, email, phone, message)
        return render_template('contact.html', msg_sent=True)

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
