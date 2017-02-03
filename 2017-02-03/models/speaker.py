from sqlalchemy import Column, String, Integer, create_engine, SmallInteger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import DB_URI, SUGGEST_USER_LIMIT

Base = declarative_base()
engine = create_engine(DB_URI)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'test_user'

    # 表的结构:
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    speaker_id = Column(String(40), index=True, unique=True)
    name = Column(String(40), index=True, nullable=False)
    gender = Column(SmallInteger, default=2)
    headline = Column(String(200))
    avatar_url = Column(String(100), nullable=False)
    bio = Column(String(200))
    description = Column(String())

    @classmethod
    def add(cls, **kwargs):
        speaker_id = kwargs.get('speaker_id', None)
        if id is not None:
            r = session.query(cls).filter_by(speaker_id=speaker_id).first()
            if r:
                return r
        try:
            r = cls(**kwargs)
            session.add(r)
            session.commit()
        except:
            session.rollback()
            raise
        else:
            return r

    @classmethod
    def suggest(cls, q, limit=SUGGEST_USER_LIMIT):
        query = session.query(User)
        users = query.filter(User.name.like('%{}%'.format(q))).limit(limit).all()
        return [user.to_dict() for user in users]

    def to_dict(self):
        d = {c.name: getattr(self, c.name, None)
             for c in self.__table__.columns}
        d.update({'type': 'user'})
        return d

Base.metadata.create_all()
