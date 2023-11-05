from fastapi import FastAPI

from api import users, sections, cources
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
        title="Fast API LMS",
        description="LMS for managing students and courses.",
        version="0.0.1"
    )

app.include_router(users.router)
app.include_router(cources.router)
app.include_router(sections.router)
