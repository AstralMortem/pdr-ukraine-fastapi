from uuid import UUID
from fastapi_users import schemas

from ..utils.enums import DriverLicense, Language


class UserRead(schemas.BaseUser[UUID]):
    first_name: str | None
    last_name: str | None
    phone: str | None
    image: str | None
    license: list[DriverLicense] = []
    lang: Language


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    phone: str
    image: str | None = None
    license: list[DriverLicense] = []
    lang: Language = Language.uk


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str | None
    last_name: str | None
    phone: str | None
    image: str | None
    license: list[DriverLicense] = []
    lang: Language
