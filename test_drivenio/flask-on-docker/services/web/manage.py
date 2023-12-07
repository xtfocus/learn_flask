from flask.cli import FlaskGroup

from project import app, db

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    """
    This registers a new command, create_db, to the CLI
    so that we can run it from the command line, which
    we'll use shortly to apply the model to the database.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
