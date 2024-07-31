from datetime import datetime
from pydantic import BaseModel, ConfigDict

from ..utils.enums import DriverLicense


class TimeStampMixin:
    created_at: datetime
    updated_at: datetime | None
    is_active: bool


# Topic Schema
class ITopicAdd(BaseModel):
    code: str
    title: str
    max_questions: int

    model_config = ConfigDict(from_attributes=True)


class ITopicUpdate(ITopicAdd):
    code: str | None = None
    title: str | None = None
    max_questions: int | None = None


class ITopicList(ITopicAdd):
    id: int


class ITopicDetail(ITopicList, TimeStampMixin):
    pass


# Question Schema
class IQuestionAdd(BaseModel):
    topic_id: int
    question: str
    correct_answer: int
    related_rule_id: str | None = None
    for_license: list[DriverLicense] | None = None
    answer_1: str
    answer_2: str
    answer_3: str | None = None
    answer_4: str | None = None
    answer_5: str | None = None
    has_image: bool = False


class IQuestionUpdate(IQuestionAdd):
    topic_id: int | None = None
    question: str | None = None
    correct_answer: int | None = None
    answer_1: str | None = None
    answer_2: str | None = None


class IQuestionList(IQuestionAdd):
    id: int


class IQuestionDetail(IQuestionList, TimeStampMixin):
    pass
