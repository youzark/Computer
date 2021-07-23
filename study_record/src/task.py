from sqlalchemy import Column,String,create_engine,Integer,Numeric
from sqlalchemy import DateTime,ForeignKey,Boolean
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine('sqlite:///database/task.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Cookie(Base):
    __tablename__ = 'cookies'

    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(20),index = True)
    cookie_cost = Column(Integer)
    cookie_size = Column(Numeric(12,2))

Base.metadata.create_all(engine)

c1 = Cookie(cookie_name = 'test_cookie1',cookie_cost=4,cookie_size=54.2)
c2 = Cookie(cookie_name = 'test_cookie2',cookie_cost=2,cookie_size=24.12)
c3 = Cookie(cookie_name = 'test_bunny3',cookie_cost=3,cookie_size=234.1)

session.bulk_save_objects([c1,c2,c3])
session.commit()


record = session.query(Cookie).filter(Cookie.cookie_name.like('%bunny%'))
for reco in record:
    print(reco.cookie_name)


