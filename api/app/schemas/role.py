from pydantic import BaseModel


class RoleBase(BaseModel):
    rolename: str


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True
