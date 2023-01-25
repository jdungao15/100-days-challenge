from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        string = function()
        return f"<b>{string}</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        string = func()
        return f"<em>{string}</em>"
    return wrapper

def make_italic(func):
    def wrapper():
        string = func()
        return f"<i>{string}"
    return wrapper



@app.route('/')
def hello_world():
    return "<h1>Hello worldHi World</h1>"


@app.route('/bye')
@make_italic
def bye():
    return "Bye"


if __name__ == '__main__':
    app.run(debug=True)