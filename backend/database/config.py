import os
from dotenv import load_dotenv
from databases import Database
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from a .env file (if present)
load_dotenv()

# MySQL database URL
database_url = "mysql+aiomysql://dbuser:dbpassword@mysql:3306/mydatabase"
# Create async engine
engine = create_async_engine(database_url, echo=True)

# Create async session
async_session = sessionmaker(
    engine, expire_on_commit=False, autocommit=False, class_=AsyncSession
)

# Declarative Base
Base = declarative_base()

# Database instance
database = Database(database_url)
