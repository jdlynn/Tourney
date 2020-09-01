from flask import Blueprint, render_template, flash, redirect, url_for
from .extentions import login_required


main = Blueprint('main', __name__)


@main.route('/')
def index():
    name = 'Jim'
    return render_template('index.html', name=name)


@main.route('/tournament')
@login_required
def tournament():
    name = 'Jim'
    return render_template('tournament.html', name=name)


@main.route('/admin')
def admin():
    name = 'Jim'
    return render_template('admin.html', name=name)


@main.route('/other')
@login_required
def other():
    name = 'Jim'
    return render_template('other.html', name=name)