from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(12), unique=True)
  password = db.Column(db.String(10))

  def __init__(self, email, password):
    self.email = email.lower()
    self.set_password(password)

  def set_password(self, password):
    self.password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)
