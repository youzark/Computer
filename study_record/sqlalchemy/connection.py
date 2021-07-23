from sqlalchemy import text,create_engine
from sqlalchemy.orm import Session


# connection
engine = create_engine("sqlite:///:memory:",echo=True,future=True)

# connect and commit
with engine.connect() as conn:
    conn.execute(text("create table some_table(x int,y int)"))
    conn.execute(text("insert into some_table (x,y) values (:x,:y)"),[{"x":1,"y":1},{"x":2,"y":4}])
    conn.commit()

# connect with begin (auto commit)
with engine.begin() as conn:
    conn.execute(text("insert into some_table (x,y) values (:x,:y)"),[{"x":6,"y":8},{"x":9,"y":10}])

#stmt with argument
with engine.begin() as conn:
    result = conn.execute(text("select x,y from some_table where y > :y"),{"y":3})
    for x,y in result:
        print(f"x:{x},y:{y}")

# stmt with argument (parameter bind)
t = 6
stmt = text("select x,y from some_table where y > :y").bindparams(y = t)
with engine.begin() as conn:
    result = conn.execute(stmt)
    for x,y in result:
        print(f"x:{x},y:{y}")

# session with commit(commit as you go)
with Session(engine) as session:
    session.execute(text("update some_table set y=:y where x=:x"),[{"x":9,"y":11},{"x":1,"y":123}])
    session.commit()

# connection with session
with Session(engine) as session:
    result = session.execute(stmt)
    for x,y in result:
        print(f"x:{x},y:{y}")














