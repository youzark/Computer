from sqlalchemy import create_engine,insert,Column,Integer,Time,ForeignKey
from sqlalchemy.orm import registry

db_address = "database/task.db"
engine = create_engine(f"sqlite:///{db_address}",echo=True,future=True)

mapper = registry()
Base = mapper.generate_base()

class task(Base):
    __tablename__ = 'task'
    id = Column(Integer,primary_key=True)
    ddl = Column(Time)
    knowledge_set = Column(Integer,ForeignKey("knowledge_set.id"))
    activity = Column(Integer,ForeignKey("activity.id"))
    time = Column(Integer) # time spant on it
    status = Column(Integer) # 0 for on going 1 for done

def query_unfinished_task():
    pass

    

class knowledge_set(Base):
    __tablename__ = 'knowledge_set'
    id = Column(Integer,primary_key=True)

class activity(Base):
    __tablename__ = 'activity'
    id = Column(Integer,primary_key=True)
    
mapper.metadata.create_all(engine)

