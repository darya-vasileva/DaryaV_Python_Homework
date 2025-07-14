from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = ""

db = create_engine(db_connection_string)


def test_insert():
    db = create_engine(db_connection_string)

    sql_1 = text("""insert INTO subject(\"subject_id\", \"subject_title\")
                values (:test_subject_id, :test_subject_title)""")

    test_subject_id = 16
    test_subject_title = 'Chinese'

    db.execute(sql_1, {"test_subject_id": test_subject_id,
                       "test_subject_title": test_subject_title})

    sql_2 = text("delete from subject where subject_id = :test_subject_id")
    db.execute(sql_2, {"test_subject_id": test_subject_id})


def test_update():
    db = create_engine(db_connection_string)

    sql_1 = text("""insert INTO subject(\"subject_id\", \"subject_title\")
                values (:test_subject_id, :test_subject_title)""")

    test_subject_id = 16
    test_subject_title = 'Chinese'

    db.execute(sql_1, {"test_subject_id": test_subject_id,
                       "test_subject_title": test_subject_title})

    sql_2 = text("""update subject set subject_title = :new_subject_title
                 where subject_id = :new_subject_id""")

    new_subject_title = 'QA'
    new_subject_id = 17

    db.execute(sql_2,
               {"new_subject_title": new_subject_title,
                "new_subject_id": new_subject_id})

    sql_3 = text("delete from subject where subject_id = :new_subject_id")
    db.execute(sql_3, {"new_subject_id": new_subject_id})


def test_delete():
    db = create_engine(db_connection_string)

    sql_1 = text("""
        insert INTO student(\"user_id\", \"level\",
                \"education_form\", \"subject_id\")
        values (:test_user_id, :test_level,
                 :test_education_form, :test_subject_id)""")

    test_user_id = 555555
    test_level = 'Elementary'
    test_education_form = 'group'
    test_subject_id = 1

    db.execute(sql_1, {"test_user_id": test_user_id,
                       "test_level": test_level,
                       "test_education_form": test_education_form,
                       "test_subject_id": test_subject_id})

    sql_2 = text("delete from student where user_id = :test_user_id")

    db.execute(sql_2, {"test_user_id": test_user_id})
