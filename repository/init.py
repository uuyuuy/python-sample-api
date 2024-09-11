from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config

db = "mysql+pymysql://{user}:{password}@localhost:{port}/sample?charset=utf8".format(
    user=config.DB_USER, password=config.DB_PASS, port=config.DB_PORT
)
engine = create_engine(db)
SessionLocal = sessionmaker(autocommit=False, bind=engine)


def get_session():
    db = SessionLocal()
    try:
        yield db
        db.close()
    finally:
        db.close()
