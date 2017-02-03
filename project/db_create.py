from views import db
from models import task
from datetime import date

# create DB and DB table
db.create_all()

# insert data to DB
db.session.add(Task("Finish this tutorial", date(2016, 9, 22), 10, 1))
db.session.add(Task("Finish Real Python", date(2016, 10, 3), 10, 1))


# commit
db.session.commit()
