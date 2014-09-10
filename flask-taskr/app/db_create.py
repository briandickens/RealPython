'''
Created on Sep 2, 2014

Create the db for the app.

@author: bdickens
'''
from views import db
from models import FTasks
from datetime import date

# create the database and the db Table
db.create_all()

# insert data
# db.session.add(FTasks("Finish this tutorial", date(2014, 3, 13), 10, 1))
# db.session.add(FTasks("Finish Real Python", date(2014, 3, 13), 10, 1))

# commit the Changes
db.session.commit()