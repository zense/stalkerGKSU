from routes import db
import json
# Define a base model for other database tables to inherit

class User(db.Model):

    __tablename__ = 'users'

    # Organisation
    organisation = db.Column(db.String(128), nullable=False)

    # User Name
    name    = db.Column(db.String(128),  nullable=False)

    # Github username
    github_username = db.Column(db.String(128), primary_key = True, nullable = False, unique = True)

    # New instance instantiation procedure
    def __init__(self, organisation, name, github_username):

        self.organisation = organisation
        self.name    = name
        self.github_username = github_username

    def __repr__(self):
        return json.dumps([self.name, self.github_username])
