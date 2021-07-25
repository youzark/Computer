from sqlalchemy import create_engine,insert
from sqlalchemy.orm import registry

db_address = "/home/hyx/Computer/study_record/database/task.db"
engine = create_engine(f"sqlite://{db_address}",ehco=True)

mapper = registry()
Base = mapper.generate_base()

class 
