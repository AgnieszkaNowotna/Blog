from app import fake, db
from app.models import Entry
import datetime

for i in range (10):
    post = Entry(title = fake.sentence(), body = fake.text(), publish_date = fake.date_time_between_dates(datetime.datetime(2022, 1, 1), datetime.datetime.now()), is_published = True)
    db.session.add(post)
    db.session.commit()