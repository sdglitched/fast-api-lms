from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from api.utils.courses import get_course, get_courses, get_user_courses, create_course, update_course, delete_course
from pydantic_schemas.course import Course, CourseCreate, CourseBase


router = fastapi.APIRouter()


@router.get("/courses", response_model=List[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db)
    return courses


@router.post("/courses", response_model=Course, status_code=201)
async def create_new_course(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)


@router.get("/courses/{course_id}")
async def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not present")
    return db_course


@router.patch("/courses/{course_id}", response_model=Course)
async def updt_course(course_id: int, course: CourseBase, db: Session = Depends(get_db)):
    course_to_update = update_course(db=db, course_id=course_id, course=course)
    return course_to_update


@router.delete("/courses/{course_id}")
async def dlt_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not present")
    course_to_delete = delete_course(db=db, course_id=course_id)
    return course_to_delete


@router.get("/courses/{course_id}/sections")
async def read_course_sections():
    return {"courses": []}
