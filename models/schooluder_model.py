from models.config import connection


def get_lessons_by_day_and_grade(grade, day):
    with connection.cursor() as cursor:
        query = f"select hour, teacher, name_, zoom_link from week_schedule , subject_ where class = '{grade}' and day_ = {day} and subject_id = id order by hour;"
        cursor.execute(query)
        res = cursor.fetchall()
        return res


def get_week_schedule_by_class(grade):
    res = []
    for i in range(1, 7):
        res.append(get_lessons_by_day_and_grade(grade, i))
    return res


def get_class_by_student(student_name):
    with connection.cursor() as cursor:
        query = f"select class from student where name_ = '{student_name}';"
        cursor.execute(query)
        res = cursor.fetchone()
        return res['class']


def get_key_subject_by_name(subject):
    with connection.cursor() as cursor:
        query = f"select id from subject_ where name_ = '{subject}';"
        cursor.execute(query)
        res = cursor.fetchall()
        return res[0]['id']


def insert_lesson_to_schedule(grade, day, hour, subject, zoom_link=None):
    with connection.cursor() as cursor:
        subject_key = get_key_subject_by_name(subject)
        print(subject_key)
        query = f"insert into week_schedule values ('{grade}', {day}, '{hour}', {subject_key});"
        print(query)
        cursor.execute(query)
        connection.commit()
