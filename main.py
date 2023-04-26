from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Base, Student
from database import *

app = FastAPI()
Base.metadata.create_all(bind=engine)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/student')
def students_list(db: Session = Depends(get_db)):
    return db.query(Student).all()


@app.post('/add-student')
async def add_student(req: Request, db: Session = Depends(get_db)):
    req_info = await req.json()
    student = Student(
        name=req_info['name'],
        email=req_info['email'],
        roll_no=req_info['rollNo'],
        phone_no=req_info['phone'],
        course=req_info['course'],
        address=req_info['address']
    )
    print(student.json())
    db.add(student)
    db.commit()
    db.close()


@app.delete('/delete-student/{id}')
def delete_student(id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter_by(id=id).first()
    db.delete(student)
    db.commit()
    db.close()


@app.get('/student/{id}')
def get_student(id: int, db: Session = Depends(get_db)):
    return db.query(Student).filter_by(id=id).first()


@app.post('/student/update/{id}')
async def update_student(id: int, request: Request, db: Session = Depends(get_db)):
    req_info = await request.json()
    new_student = Student(
        name=req_info['name'],
        email=req_info['email'],
        roll_no=req_info['rollNo'],
        course=req_info['course'],
        address=req_info['address'],
        phone_no=req_info['phone']
    )
    student = db.query(Student).filter_by(id=id).first()
    student.update(new_student)
    db.commit()
    db.close()
