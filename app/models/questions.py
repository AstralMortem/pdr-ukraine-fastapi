from sqlalchemy import ForeignKey, ForeignKeyConstraint, UniqueConstraint
from sqlalchemy.dialects.postgresql import ARRAY, ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..utils.enums import DriverLicense
from .mixins import CommonIntMixin, BaseTable, CommonUUIDMixin


class Topic(CommonIntMixin, BaseTable):
    __tablename__ = "test_topics"
    code: Mapped[str]
    title: Mapped[str]
    max_questions: Mapped[int]

    # list of questions for special topic
    questions: Mapped[list["Question"]] = relationship()


class Question(CommonIntMixin, BaseTable):
    __tablename__ = "test_questions"
    topic_id: Mapped[int] = mapped_column(
        ForeignKey("test_topics.id"), primary_key=True
    )
    question: Mapped[str]
    correct_answer: Mapped[int]
    related_rule_id: Mapped[str | None] = mapped_column(default=None)
    for_license: Mapped[ARRAY | None] = mapped_column(
        ARRAY(ENUM(DriverLicense, name="driverlicense", create_type=False)),
        default=None,
    )
    answer_1: Mapped[str]
    answer_2: Mapped[str]
    answer_3: Mapped[str | None]
    answer_4: Mapped[str | None]
    answer_5: Mapped[str | None]

    has_image: Mapped[bool] = mapped_column(default=False)
    # images: Mapped[list["QuestionImage"]] = relationship()


class QuestionImage(CommonUUIDMixin, BaseTable):
    __tablename__ = "test_question_images"
    question_id: Mapped[int]
    topic_id: Mapped[int]
    image: Mapped[str]

    __table_args__ = (
        ForeignKeyConstraint(
            ["question_id", "topic_id"],
            ["test_questions.id", "test_questions.topic_id"],
        ),
    )
