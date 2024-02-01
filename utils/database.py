from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the URL for the SQLite database.
# For PostgreSQL, you can uncomment the alternative URL.
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Create a SQLAlchemy engine with the specified database URL.
# Setting `check_same_thread` to False for SQLite to allow multithreaded access.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session factory (sessionmaker) bound to the engine.
# It will generate new Session objects when called.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models.
# All models will inherit from this base class.
Base = declarative_base()
