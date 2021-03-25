from mongoengine import signals

from application import db

class Store(db.Document):
    # Use external ID and not db ID to show to public
    external_id = db.StringField(db_field="ei")
    name = db.StringField(db_field="na")
    neighborhood = db.StringField(db_field="n")
    street_address = db.StringField(db_field="sa")
    city = db.StringField(db_field="c")
    state = db.StringField(db_field="st")
    zip = db.StringField(db_field="z")
    phone = db.StringField(db_field="p")
    live = db.BooleanField(db_field="l", default=True)

    meta = {
        'indexes': [('external_id', 'live')]
    }
