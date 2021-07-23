from sqlalchemy import MetaData
from sqlalchemy import Table,Column,Integer,String

# define metadata the container , one for the whole project is enough
metadata = MetaData()

# define table
user_table = Table(
        "user_account",
        metadata,
        Column('id',Integer,primary_key)
        )
