from sqlalchemy import insert
from sqlalchemy.orm import registry,relationship
from sqlalchemy import ForeignKey,create_engine,text
from sqlalchemy import MetaData
from sqlalchemy import Table,Column,Integer,String


engine = create_engine("sqlite:///:memory:",echo=True,future=True)

# define metadata the container , one for the whole project is enough
metadata = MetaData()

# define table
user_table = Table(
        "user_account",
        metadata,
        Column('id',Integer,primary_key=True),
        Column('name',String(30)),
        Column('fullname',String)
        )


# foreign key demo
address_table = Table(
        "address",
        metadata,
        Column('id',Integer,primary_key=True),
        Column('user_id',ForeignKey('user_account.id'),nullable=False),
        Column('email_address',String,nullable=False)
        )

# emit all the table object to DDL and to the database


# registry
# construct the registry (contain a metadata)
mapper_registry = registry()
print(mapper_registry.metadata)


Base = mapper_registry.generate_base()

# Class(to table ) define
# __repr__ is use to print out the class info
# when "print(class_instance)" is called ,the __repr__ will be called and return to replace class_instance
class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer,primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address",back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r},name={self.name!r},fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer,primary_key=True)
    email_address = Column(String,nullable=False)
    user_id = Column(Integer,ForeignKey('user_account.id'))

    user = relationship("User",back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r},email_address={self.email_address!r})"


# emit to ddl
mapper_registry.metadata.create_all(engine)
# or 
# Base.metadata.create_all(engine)


# Combine ORM class and Table
# class User(Base):
#     __table__ = user_table

#     addresses = relationship("Address",back_populates="user")



# tabel reflection
with engine.connect() as conn:
    conn.execute(text("create table some_table(x int,y int)"))
    conn.execute(text("insert into some_table (x,y) values (:x,:y)"),[{"x":1,"y":1},{"x":2,"y":4}])
    conn.commit()
some_table = Table("some_table",metadata,autoload_with=engine)




# Inserting Rows (Down with Cores)
stmt = insert(user_table).values(name='spongebob',fullname="Spongbob Squarepants")
print(stmt)
# output :INSERT INTO user_account (name, fullname) VALUES (:name, :fullname)
compiled = stmt.compile()
print(compiled.params)
# output :{'name': 'spongebob', 'fullname': 'Spongebob Squarepants'}

#submit insert stmt
with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()

#another way

with engine.connect() as conn:
    result = conn.execute(
            insert(user_table),
            [
                {"name":"saucy","fullname":"Saucy Cheeks"},
                {"name":"patrick","fullname":"Patrick Star"}
                ]
            )
    conn.commit()

# we alse got "insert form select" and "insert return"







