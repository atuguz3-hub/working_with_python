from sqlalchemy import URL, create_engine

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="LA.",
    host="127.0.0.1",
    port=5432,
    database="QA 1",
)

engine = create_engine(DATABASE_URL)
