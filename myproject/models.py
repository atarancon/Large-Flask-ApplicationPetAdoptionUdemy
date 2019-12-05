
from myproject import db



##just type the classes for the models###
#########################################


class Puppy(db.Model):

    #establish table name
    __tablename__ = 'puppies'
    #make prymery id
    id = db.Column(db.Integer,primary_key = True)
    #make a name colum  of type text
    name = db.Column(db.Text)
    #One to one relationship
    owner = db.relationship("Owner",backref='puppy',uselist=False)
    
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name: {self.name} and owner's name: {self.owner.name}"
        else:
            return f"Puppy name: {self.name} and has no owner"
    
class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text) 
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner name: {self.name}"