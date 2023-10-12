import yaml, os.path

Books = yaml.safe_load(
    open(
        os.path.join(
            os.path.dirname(__file__),
            "data.yml"
            )
        )
    )

i = 0
for book in Books:
    book['id'] = i 
    i += 1

def get_sample():
    return Book.query.limit(10).all()

from .app import db
class Author (db.Model ):
    id = db.Column(db.Integer , primary_key =True)
    name = db.Column (db.String (100))
class Book(db.Model ):
    id = db.Column(db.Integer , primary_key =True)
    price = db.Column(db.Float)
    author_id = db.Column(db.Integer , db.ForeignKey ("author.id"))
    author = db.relationship("Author",backref =db.backref ("books", lazy="dynamic"))
class url(db.Model ):
    id = db.Column(db.Integer , primary_key =True)
    price = db.Column(db.Sting(100))
class img(db.Model ):
    id = db.Column(db.Integer , primary_key =True)
    image = db.Column(db.Sting(100))
class title(db.Model ):
    id = db.Column(db.Integer , primary_key =True)
    price = db.Column(db.Sting(100))

