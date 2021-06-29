from models.config import connection


def get_student_info(name):
    with connection.cursor() as cursor:
        query = f"select * from student where name_ = '{name}';"
        cursor.execute(query)
        res = cursor.fetchall()
        return res[0]


def get_teacher_email_by_name(name):
    with connection.cursor() as cursor:
        query = f"select email from teacher where name_ = '{name}';"
        cursor.execute(query)
        res = cursor.fetchall()
        return res[0]['email']
