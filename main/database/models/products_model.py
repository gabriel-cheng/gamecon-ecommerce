from sqlmodel import SQLModel, Field
from main.database.models.category_model import Category

class Products(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    category: int = Field(foreign_key=Category.id)
    brand: str

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "brand": self.brand
        }