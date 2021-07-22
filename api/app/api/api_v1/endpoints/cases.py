from typing import Any, Union
from pydantic.error_wrappers import ValidationError

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import DistrictCase, AppellateCase
from app.models import User
from app.api import dependency
from app.crud import case
from app.db import get_db

router = APIRouter()
clerk = dependency.AllowRoles(['clerk'])


@router.get("/{case_id}", response_model=Union[AppellateCase, DistrictCase])
def read_items(
    case_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(clerk)
) -> Any:
    '''
    Returns details about case associated with {case_id}
    '''
    the_case = case.get(db, case_id)
    if the_case is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return the_case


@router.post("/send_appeal/{case_id}", response_model=AppellateCase)
def send_appeal(
    case_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(clerk)
) -> Any:
    '''
    Creates a new appellate case base on the original
    '''
    try:
        the_case = case.send_roa(db, case_id)
    except ValidationError as e:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, str(e))

    if the_case is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return the_case
