from ..config.database import engine, SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()