from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = ""

db = create_engine(db_connection_string)


def test_insert():
    db = create_engine(db_connection_string)

    sql_1 = text("""
                insert INTO subject(\"subject_id\", \"subject_title\")
                values (:new_subject_id, :new_subject_title)""")
    db.execute(sql_1, new_subject_id=16, new_subject_title='Chinese')

    sql_2 = text("delete from subject where subject_id = :subject_id")
    db.execute(sql_2, subject_id=16)


def test_update():
    db = create_engine(db_connection_string)

    sql_1 = text("""insert INTO subject(\"subject_id\", \"subject_title\")
                 values (:new_subject_id, :new_subject_title)""")
    db.execute(sql_1, new_subject_id=16, new_subject_title='Chinese')

    sql_2 = text("""update subject set subject_title = :new_subject_title
                 where subject_id = :new_subject_id""")
    db.execute(sql_2, new_subject_title='QA', new_subject_id=16)

    sql_3 = text("delete from subject where subject_id = :subject_id")
    db.execute(sql_3, subject_id=16)


def test_delete():
    db = create_engine(db_connection_string)

    sql_1 = text("""
        insert INTO student(\"user_id\", \"level\",
                \"education_form\", \"subject_id\")
        values (:user_id, :level, :education_form, :subject_id)""")

    db.execute(sql_1, user_id=555555, level='Elementary',
               education_form='group', subject_id=1)

    sql_2 = text("delete from student where user_id = :user_id")

    db.execute(sql_2, user_id=555555)
