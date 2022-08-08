from sqlalchemy import create_engine,MetaData
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




engine = create_engine("mysql+pymysql://root:root123@localhost:3306/story_with_me")
meta=MetaData()
conn=engine.connect()
Base =declarative_base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DATABASE_URL = "mysql+mysqlconnector://root:root123@localhost:3306/story_with_me"
# engine = create_engine(DATABASE_URL)
# conn=engine.connect
# meta=MetaData()
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()