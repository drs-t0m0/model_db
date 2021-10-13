from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.cruds import project as crud_project
from src.schemas import project as schema_project
from src.db.database import get_db

router = APIRouter()


@router.get("/all")
def project_all(db: Session = Depends(get_db)):
    return crud_project.select_project_all(db=db)


@router.get("/id/{project_id}")
def project_by_id(
        project_id: str,
        db: Session = Depends(get_db),
):
    return crud_project.select_project_by_id(
        db=db,
        project_id=project_id
    )


@router.get("/name/{project_name}")
def project_by_name(
        project_name: str,
        db: Session = Depends(get_db)
):
    return crud_project.select_project_by_name(
        db=db,
        project_name=project_name
    )


@router.post("/")
def add_project(
        project: schema_project.ProjectCreate,
        db: Session = Depends(get_db)
):
    return crud_project.add_project(
        db=db,
        project_name=project.project_name,
        description=project.description,
        commit=True
    )
