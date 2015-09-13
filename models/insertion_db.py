__author__ = 'supermacy'

from sqlalchemy import Column,Integer,Sequence,String,Boolean
from flask.ext.sqlalchemy import SQLAlchemy
from controllers import application

db = SQLAlchemy(application, session_options={'expire_on_commit': False})
Base = db.Model

class final_database(Base):
   __tablename__ = 'database_clicklabs'
   id = Column(Integer,Sequence('users_seq'), primary_key=True)
   engagement_id=  Column(String(100),unique=True)
   metered_distance = Column(String(150))
   time_deviation = Column(String(150))
   distance_deviation     = Column(String(150))
   faulty   = Column(Boolean)


   def __init__(self,engagement_id,metered_distance,time_distance,distance_deviation,faulty):

        self.engagement_id        = engagement_id
        self.metered_distance       = metered_distance
        self.time_deviation            = time_distance
        self.distance_deviation          = distance_deviation
        self.faulty     = faulty

