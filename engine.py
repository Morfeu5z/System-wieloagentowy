from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:root@localhost/sklep_agentowy_1", encoding="utf8_unicode_ci", echo=True)
metadata = MetaData()
db_scope = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_scope.query_property()

def init_db():
    import model

    Base.metadata.create_all(bind=engine)
    #metadata.create_all(bind=engine)