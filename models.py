from main import db

class QuasselUser(db.Model):
    __table__ = db.metadata.tables['quasseluser']
    networks = db.relationship('Network', backref='user')

class Backlog(db.Model):
    __table__ = db.metadata.tables['backlog']

class Buffer(db.Model):
    __table__ = db.metadata.tables['buffer']

class Network(db.Model):
    __table__ = db.metadata.tables['network']

class Sender(db.Model):
    __table__ = db.metadata.tables['sender']
