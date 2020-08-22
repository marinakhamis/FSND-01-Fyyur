#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ARRAY, ForeignKey
from flask_migrate import Migrate

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models
#----------------------------------------------------------------------------#


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO (Done): implement any missing fields, as a database migration using Flask-Migrate
    genres = db.Column(db.String())
    seeking_talent = db.Column(db.Boolean, default=False, nullable=False)
    seeking_description = db.Column(db.String(500))

    # To place a dynamic relationship on a backref, use the backref() function in conjunction with lazy='dynamic':
    # Read more on : https://docs.sqlalchemy.org/en/13/orm/collections.html
    shows = db.relationship('Show', backref='Venue', lazy='dynamic')

    def __repr__(self):
        return f'<Venue id={self.id} name={self.name}>'


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO(Done): implement any missing fields, as a database migration using Flask-Migrate
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String())

    shows = db.relationship('Show', backref='artist',
                            cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Artist id={self.id} name={self.name}>'


# TODO(Done) Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'Show'

    # Composite PK: artist.id, venue.id and show_time as an artist can have multiple shows at the same venue at different times.
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'Artist.id'), primary_key=True)

    venue_id = db.Column(db.Integer, db.ForeignKey(
        'Venue.id'), primary_key=True)

    show_time = db.Column(db.DateTime(), primary_key=True)

    def __repr__(self):
        return f'<Show artist_id={self.artist_id} venue_id={self.venue_id} time={self.show_time}>'
