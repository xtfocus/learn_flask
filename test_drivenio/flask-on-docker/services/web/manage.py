from flask.cli import FlaskGroup

from project import User, app, db

cli = FlaskGroup(app)

# @cli.command registers a new command, (here it's create_db), to the CLI
# so that we can run it from the command line, which
# we'll use shortly to apply the model to the database.


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="michael@mherman.org"))
    db.session.commit()


if __name__ == "__main__":
    cli()
