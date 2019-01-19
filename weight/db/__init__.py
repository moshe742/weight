from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


class SessionScope:
    def __init__(self):
        pass

    def __enter__(self):
        self.session = Session(engine)
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.session.commit()
        except:
            self.session.rollback()
        finally:
            self.session.close()


engine = create_engine("postgresql://moshe:He1!oworld@localhost/weight", echo=True)
Base = declarative_base()
