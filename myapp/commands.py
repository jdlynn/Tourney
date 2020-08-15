from flask import Blueprint
import click
from flask.cli import with_appcontext

commands = Blueprint('commands', __name__, cli_group=None)


@commands.cli.command('printit')
@click.argument('name')
@with_appcontext
def printit(name):
    print(f"This is a command for {name}")