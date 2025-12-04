from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.models import Task
from app.schemas.task import TaskCreate
from app.dependencies import get_current_user, get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/")
def get_tasks(
    user=Depends(get_current_user),
    db: Session = Depends(get_db),
    search: str = "",
):
    return (
        db.query(Task)
        .filter(Task.user_id == user.id, Task.title.contains(search))
        .all()
    )

@router.post("/")
def create_task(
    task: TaskCreate,
    user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    new_task = Task(**task.dict(), user_id=user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(
        Task.id == task_id, Task.user_id == user.id
    ).first()
    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}
