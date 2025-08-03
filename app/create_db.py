from .database import Base, engine
from . import models

print("🔄 Creando tablas en PostgreSQL...")
Base.metadata.create_all(bind=engine)
print("✅ Tablas creadas correctamente")
