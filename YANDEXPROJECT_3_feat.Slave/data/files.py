import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class File(SqlAlchemyBase):
    __tablename__ = 'files'

    uid = sqlalchemy.Column(sqlalchemy.Integer,
                            primary_key=True, autoincrement=True)
    filename = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
    code = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)