from enum import Enum


class CourtType(str, Enum):
    district = "district"
    appellate = "appellate"
    bankruptcy = "bankruptcy"


class CaseType(str, Enum):
    civil = "Civil"
    miscellaneous = "Miscellaneous"
    criminal = "Criminal"
    magistrate_judge = "Magistrate Judge"
    petty_offense = "Petty Offense"
    special = "Special"
    multidistrict_litigation = "Multidistrict Litigation"
    grand_jury = "Grand Jury"
