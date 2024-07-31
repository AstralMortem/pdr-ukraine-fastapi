from typing import List
from fastapi_users.db import (
    SQLAlchemyBaseUserTableUUID,
    SQLAlchemyBaseOAuthAccountTableUUID,
)
from sqlalchemy.dialects.postgresql import ARRAY, ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..utils.enums import DriverLicense, Language
from .mixins import BaseTable, TimestampMixin


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, BaseTable):
    pass


class User(SQLAlchemyBaseUserTableUUID, TimestampMixin, BaseTable):
    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined"
    )
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    phone: Mapped[str | None]
    image: Mapped[str | None]
    license: Mapped[ARRAY] = mapped_column(ARRAY(ENUM(DriverLicense)), default=[])
    lang: Mapped[ENUM] = mapped_column(ENUM(Language), default="uk")
