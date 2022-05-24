from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class MostCommonMethodsModel(Base):

    __tablename__ = 'mc_methods'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    method = Column(String(50), nullable=False)
    count = Column(Integer(), nullable=False)

class MostCommonRequestsModel(Base):

    __tablename__ = 'mc_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    request = Column(String(255), nullable=False)
    count = Column(Integer(), nullable=False)

class MostCommonUsersServerErrorModel(Base):

    __tablename__ = 'mc_users_srverror'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String(16), nullable=False)
    count = Column(Integer(), nullable=False)

class BiggestRequestsClientError(Base):

    __tablename__ = 'bgst_reqs_clienterror'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String(16), nullable=False)
    request = Column(String(255), nullable=False)
    status = Column(Integer(), nullable=False)
    size = Column(Integer(), nullable=False)
