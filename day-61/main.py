import os

from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

WTF_CSRF_SECRET_KEY = "Hatdog"


class MyForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(), Email(check_deliverability=True)])
    password = PasswordField(label='Password',
                             validators=[DataRequired(), Length(min=8, message="Must be atleast 8 characters long")])
    submit = SubmitField(label='Log In')



app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = WTF_CSRF_SECRET_KEY




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    admin = "admin@email.com"
    admin_password = "12345678"
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        if name == admin and password == admin_password:
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
