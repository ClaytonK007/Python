from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import *
from models import *
from passlib.context import CryptContext

#   Create tables
Base.metadata.create_all(bind=engine)

#   Initialize App, Templates and Password encryption
app = FastAPI()
templates = Jinja2Templates(directory="templates")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#   Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#   Registration
@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
def register(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    if db.query(User).filter(User.username == username).first():
        return templates.TemplateResponse("register.html", {"request":request, "error": "Username already exists."})
    
    hashed_password = pwd_context.hash(password)
    user = User(username=username, hashed_password=hashed_password)
    db.add(User)
    db.commit()
    return RedirectResponse(url="/login", status_code=303)

#   Login
@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return templates.TemplateResponse("login.html", {"request": request, "error": "User not found."})
    if not pwd_context.verify(password, user.hashed_password):
        return templates.TemplateResponse("login.html", {"request": request,"error": "Invalid password."})
    
    response = RedirectResponse(url="/", status_code=303)
    response.set_cookie(key="user.id", value=str(user.id), httponly=True)
    return response

#   Logout

#   Add Task

#   Toggle Complete

#   Delete Task

#   Update Task
