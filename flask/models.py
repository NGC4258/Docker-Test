from database import Base
from sqlalchemy import Column, String

class User(Base):
    __tablename__ = 'Users'
    name = Column(String(20), primary_key=True)
    job_title = Column(String(20), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    mobile = Column(String(10), unique=True, nullable=False)

    def __init__(self, name, email, job_title, mobile):
        self.name = name
        self.email = email
        self.job_title = job_title
        self.mobile = mobile

    def __repr__(self):
        return '<User %r>' % self.name
