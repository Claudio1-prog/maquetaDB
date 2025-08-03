from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

# 1. Cargar variables desde .env
load_dotenv()

# 2. Leer la URL de conexión
DATABASE_URL = os.getenv("DATABASE_URL")

# 3. Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# 4. Configurar la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Base para los modelos
Base = declarative_base()
