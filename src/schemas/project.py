import datetime
from typing import Optional

from pydantic import BaseModel


class ProjectBase(BaseModel):
    project_name: str
    description: Optional[str]


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    project_id: int
    created_datetime: datetime.datetime

    class Config:
        orm_mode = True
