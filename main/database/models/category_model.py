from sqlmodel import SQLModel, Field

class Category(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }