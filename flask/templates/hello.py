#!/usr/bin/python3
"""
Example flask code
"""

from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Vivy Emerekpomkpom',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'May 20, 2024'
    },
    {
        'author': 'Nazy Emerekpomkpom',
        'title': ' Blog post 2',
        'content': 'Second post content',
        'date_posted': 'May 21, 2024'
    }
]

@ app.route("/")
@ app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@ app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
