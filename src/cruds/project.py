import uuid
from typing import List, Optional

from sqlalchemy.orm import Session
from src.models import project as model_project
from src.schemas import project as schema_project


def select_project_all(db: Session) -> List[schema_project.Project]:
    return db.query(model_project.Project).all()


def select_project_by_id(db: Session, project_id: str) -> schema_project.Project:
    return db.query(model_project.Project).filter(model_project.Project.project_id == project_id).first()


def select_project_by_name(db: Session, project_name: str) -> schema_project.Project:
    return db.query(model_project.Project).filter(model_project.Project.project_name == project_name).first()


def add_project(
        db: Session,
        project_name: str,
        description: Optional[str] = None,
        commit: bool = True
) -> schema_project.Project:
    exists = select_project_by_name(db=db, project_name=project_name)
    if exists:
        return exists
    else:
        project_id = str(uuid.uuid4())[:6]
        data = model_project.Project(
            project_id=project_id,
            project_name=project_name,
            description=description,
        )
        db.add(data)
        if commit:
            db.commit()
            db.refresh(data)
        return data
