from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import pandas as pd
import pprint as pp

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired(),URL(True)])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', validators=[DataRequired()],
                         choices=[(1, '☕️'), (2, '☕️☕️'), (3, '☕️☕️☕️'), (4, '☕️☕️☕️☕️'), (5, '☕️☕️☕️☕️☕️')])
    wifi = SelectField('Wifi Strength Rating', validators=[DataRequired()],
                       choices=[(1, '✘'), (2, '💪'), (3, '💪💪'), (4, '💪💪💪'), (5, '💪💪💪💪'), (6, '💪💪💪💪💪')])
    power = SelectField('Power Socket Availability', validators=[DataRequired()],
                        choices=[(1, '✘'), (2, '🔌'), (3, '🔌🔌'), (4, '🔌🔌🔌'), (5, '🔌🔌🔌🔌'), (6, '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location = form.location.data
        store_open = form.open.data
        store_close = form.close.data

        coffee = '☕' * int(form.coffee.data)
        wifi = '💪' * int(form.wifi.data)
        power = '🔌' * int(form.power.data)

        # update csv file
        df = pd.read_csv('cafe-data.csv')
        new_cafe = [cafe, location, store_open, store_close, coffee, wifi, power]
        df.loc[len(df)] = new_cafe
        df.to_csv('cafe-data.csv', index=False)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    csv_data = pd.read_csv('cafe-data.csv')
    cafes = csv_data.to_dict(orient='records')
    return render_template('cafes.html', cafes=cafes)


if __name__ == '__main__':
    app.run(debug=True)
