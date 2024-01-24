from sqlmodel import Field, SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI")

print(DATABASE_URI)

# class Database():
    