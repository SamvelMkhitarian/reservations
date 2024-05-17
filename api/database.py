from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from .settings import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, DB_PORT, DB_HOST

DB_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"
DB_SYNC_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"

engine = create_async_engine(DB_URL)
sync_engine = create_engine(DB_SYNC_URL)
SessionLocal = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    async with SessionLocal() as session:
        async with session.begin():
            yield session
