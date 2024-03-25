from sqlalchemy.orm import Session

from db.models.course import Course
from pydantic_schemas.course import CourseCreate, CourseBase


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()

def get_courses(db: Session):
    return db.query(Course).all()

def get_user_courses(db: Session, user_id: int):
    courses = db.query(Course).filter(Course.user_id == user_id).all()
    return courses

def create_course(db: Session, course: CourseCreate):
    db_course = Course(title=course.title, description=course.description, user_id=course.user_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_course(db: Session, course_id: int, course: CourseBase):
    course_to_update = get_course(db=db, course_id=course_id)
    course_to_update.title = course.title
    course_to_update.description = course.description
    db.commit()
    return course_to_update

def delete_course(db: Session, course_id: int):
    course_to_delete = get_course(db=db, course_id=course_id)
    db.delete(course_to_delete)
    db.commit()
    return course_to_delete
