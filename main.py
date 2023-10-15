from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional, List

from api import users, sections, cources

app = FastAPI(
        title="Fast API LMS",
        description="LMS for managing students and courses.",
        version="0.0.1"
    )

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(cources.router)