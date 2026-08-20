import pytest
from sqlalchemy import delete, select

from db import engine
from models import Subject


TEST_SUBJECT_ID = 999999
TEST_SUBJECT_TITLE = "Test Subject"


@pytest.fixture(autouse=True)
def cleanup():
    with engine.begin() as connection:
        connection.execute(
            delete(Subject).where(Subject.subject_id == TEST_SUBJECT_ID)
        )

    yield

    with engine.begin() as connection:
        connection.execute(
            delete(Subject).where(Subject.subject_id == TEST_SUBJECT_ID)
        )


def test_create_subject():
    with engine.begin() as connection:
        connection.execute(
            Subject.__table__.insert().values(
                subject_id=TEST_SUBJECT_ID,
                subject_title=TEST_SUBJECT_TITLE,
            )
        )

    with engine.connect() as connection:
        subject = connection.execute(
            select(Subject).where(
                Subject.subject_id == TEST_SUBJECT_ID
            )
        ).first()

    assert subject is not None
    assert subject.subject_title == TEST_SUBJECT_TITLE


def test_update_subject():
    with engine.begin() as connection:
        connection.execute(
            Subject.__table__.insert().values(
                subject_id=TEST_SUBJECT_ID,
                subject_title=TEST_SUBJECT_TITLE,
            )
        )

        connection.execute(
            Subject.__table__.update()
            .where(Subject.subject_id == TEST_SUBJECT_ID)
            .values(subject_title="Updated Subject")
        )

    with engine.connect() as connection:
        subject = connection.execute(
            select(Subject).where(
                Subject.subject_id == TEST_SUBJECT_ID
            )
        ).first()

    assert subject is not None
    assert subject.subject_title == "Updated Subject"


def test_delete_subject():
    with engine.begin() as connection:
        connection.execute(
            Subject.__table__.insert().values(
                subject_id=TEST_SUBJECT_ID,
                subject_title=TEST_SUBJECT_TITLE,
            )
        )

        connection.execute(
            delete(Subject).where(
                Subject.subject_id == TEST_SUBJECT_ID
            )
        )

    with engine.connect() as connection:
        subject = connection.execute(
            select(Subject).where(
                Subject.subject_id == TEST_SUBJECT_ID
            )
        ).first()

    assert subject is None
