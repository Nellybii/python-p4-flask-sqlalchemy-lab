from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable= False)
    birthday= db.Column(db.DateTime, nullable= False)

    animal_id=db.Column(db.Integer, db.ForeignKey('animals.id'))

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String, nullable= False)
    open_to_visitors = db.Column(db.String, nullable= False)

    animal_id=db.Column(db.Integer, db.ForeignKey('animals.id'))

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable= False)
    species= db.Column(db.String, nullable= False)

    zookeeper= db.relationship('Zookeeper', backref='animal')
    enclosure= db.relationship('Enclosure', backref='animal')
