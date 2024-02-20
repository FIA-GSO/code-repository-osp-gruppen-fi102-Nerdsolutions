import enum
from sqlalchemy import ForeignKey, String, Uuid, Column, Float, create_engine, Date, Enum
from sqlalchemy.orm import DeclarativeBase, declarative_base, relationship

# class Base(DeclarativeBase):
#  pass
Base = declarative_base()

DB_FILE = 'goods.sqlite'
DB_CONN = 'sqlite:///' + DB_FILE


class Location(enum.Enum):
    HOME = 1
    TRANSPORT = 2
    DEPLOYMENT = 3


class Box(Base):
    __tablename__ = 'Boxes'
    guid: Uuid = Column(
        Uuid,
        primary_key=True,
        nullable=False,
        default=lambda: Uuid.uuid4())
    description: str = Column(String)
    category: str = Column(String)
    deployment_token: str = Column(String)
    location = Column(Enum(Location))
    location_home: str = Column(String)
    location_transport: str = Column(String)
    location_deployment: str = Column(String)


class BoxItems(Base):
    __tablename__ = 'BoxItems'
    guid: Uuid = Column(
        Uuid,
        primary_key=True,
        nullable=False,
        default=lambda: Uuid.uuid4())
    gtin: Uuid = Column(Uuid)
    description: str = Column(String)
    boxes_guid: Uuid = Column(
        Uuid,
        ForeignKey(
            'Boxes.guid',
            ondelete='CASCADE'))
    box = relationship(
        'Boxes',
        foreign_keys=[boxes_guid],  # )
        lazy='selecting')
    quantity: float = Column(Float)
    unit: str = Column(String)


class ItemContents(Base):
    __tablename__ = 'ItemContents'
    guid: Uuid = Column(
        Uuid,
        primary_key=True,
        nullable=False,
        default=lambda: Uuid.uuid4())
    gtin: Uuid = Column(Uuid)
    description: str = Column(String)
    boxItems_guid: Uuid = Column(
        Uuid,
        ForeignKey(
            'BoxItems.guid',
            ondelete='CASCADE'))
    quantity: float = Column(Float)
    unit: str = Column(String)
    expiration_date = Column(Date)


class User(Base):
    __tablename__ = 'User'
    __mapper_args__ = {
        'polymorphic_identity': 'User',
        'polymorphic_on': 'role'}
    id: Uuid = Column(
        Uuid,
        primary_key=True,
        nullable=False,
        default=lambda: Uuid.uuid4())
    username: str = Column(String)
    password_hash: str = Column(String(40))
    role: str = Column((String(20)))


class Admin(User):
    __mapper_args__ = {'polymorphic_identity': 'Admin'}


class WarehouseClerk(User):
    __mapper_args__ = {'polymorphic_identity': 'Warehouse Clerk'}


class OperationsManager(User):
    __mapper_args__ = {'polymorphic_identity': 'Operations Manager'}


class Assistant(User):
    __mapper_args__ = {'polymorphic_identity': 'Assistant'}


if __name__ == '__main__':
    '''create an SQLite database if not exist and complete schema'''
    engine = create_engine(DB_CONN)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print('done.')
