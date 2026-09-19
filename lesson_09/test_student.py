from db import Session, Student


def test_add_student():
    session = Session()

    student = Student(
        user_id=999999,
        level="junior",
        education_form="online",
        subject_id=1,
    )

    session.add(student)
    session.commit()

    result = session.query(Student).filter_by(
        user_id=999999
    ).first()

    assert result.level == "junior"

    session.delete(student)
    session.commit()

    session.close()


def test_update_student():
    session = Session()

    student = Student(
        user_id=999998,
        level="junior",
        education_form="online",
        subject_id=1,
    )

    session.add(student)
    session.commit()

    student.level = "middle"
    session.commit()

    result = session.query(Student).filter_by(
        user_id=999998
    ).first()

    assert result.level == "middle"

    session.delete(student)
    session.commit()

    session.close()


def test_delete_student():
    session = Session()

    student = Student(
        user_id=999997,
        level="junior",
        education_form="online",
        subject_id=1,
    )

    session.add(student)
    session.commit()

    session.delete(student)
    session.commit()

    result = session.query(Student).filter_by(
        user_id=999997
    ).first()

    assert result is None

    session.close()