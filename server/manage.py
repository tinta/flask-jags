from app.models import db
from app.fixtures import test_items
from app.routes import app
import app.models import TodoItem

# other libraries
import requests
import time

def init_db():
    # do this import so that all models are create when create_all is called
    db.create_all()

def populate_db():
    for item in test_items:
        db.session.add(item)
    db.session.commit()

def main():
    with app.app_context():
        init_db()
        populate_db()

if __name__ == "__main__":
    main()


