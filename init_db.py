from backend.database.connection import Base, engine
from backend.alchemy_models import user, entry, budget, category, recurring

Base.metadata.create_all(bind=engine)
