from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150)) 
    password = db.Column(db.String(150))
    Note = db.relationship('Note') 
    Post = db.relationship('Post') 
    Comment = db.relationship('Comment')




class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    user = db.relationship('User', backref='posts') 


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))



