from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base


engine = create_engine("mysql://root:admin@localhost/rh")


db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from.models.departamento import Departamento
    Base.metadata.create_all(bind=engine)
