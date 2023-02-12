from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from API.database import Base

class Wardrobe(Base):
    __tablename__ = 'Wardrobe'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    id_collection: Mapped[int] = mapped_column(ForeignKey("Collection.id"))