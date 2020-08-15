from flask import Blueprint, render_template, flash, redirect, url_for


main = Blueprint('main', __name__)


@main.route('/')
def index():
    name = 'Jim'
    return render_template('index.html', name=name)
