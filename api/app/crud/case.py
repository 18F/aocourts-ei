from typing import Optional, Any, Union

from sqlalchemy.orm import Session, contains_eager

from app.models import DistrictCase, AppellateCase, Case, DocketEntry
from app.schemas import DistrictCase as ValidDistrictCase, AppellateCaseInput


class CrudCase:
    '''
    Create, read, update, and delete cases
    '''
    def get(self, db: Session, id: Any) -> Optional[Union[DistrictCase, AppellateCase]]:
        return db.query(Case).filter(Case.id == id).one_or_none()

    def set_sealed(self, db: Session, id: Any, sealed: Any) -> Optional[Union[DistrictCase, AppellateCase]]:
        print(id, sealed)
        case = db.query(Case).filter(Case.id == id).one_or_none()
        if case is not None:
            case.sealed = sealed
            db.add(case)
            db.commit()
        return case

    def send_roa(self, db: Session, id: Any) -> Optional[AppellateCase]:
        # For now just grab orders to demonstrate filtering
        # This will probably need to allow specific filtering of docket items
        original = db.query(Case).options(contains_eager(Case.docket_entries))
        original = original.join(DocketEntry).filter(Case.id == id).filter(DocketEntry.entry_type == 'order')
        original = original.one_or_none()
        if original is None:
            return
        # make an appeal
        # this raises a ValidationError if the original is not
        # a proper district case
        valid_case = ValidDistrictCase.from_orm(original)

        appellate = valid_case.dict(exclude={'id', 'type'})
        appellate['original_case_id'] = valid_case.id
        app_case = AppellateCaseInput(**appellate)
        app_case.docket_entries = [DocketEntry(**d.dict()) for d in app_case.docket_entries]

        appeal = AppellateCase(**app_case.dict())
        db.add(appeal)
        db.commit()

        return appeal


case = CrudCase()
