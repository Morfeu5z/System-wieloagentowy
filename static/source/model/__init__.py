from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

_engines = create_engine("mysql://morfeu5z:KarmazynowaBroda69>@trashpanda.pwsz.nysa.pl/sklep_agentowy_1")
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=_engines))
_Base = declarative_base()
_Base.query = session.query_property()
_Base.metadata.create_all(bind=_engines)
