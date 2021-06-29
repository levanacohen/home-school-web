from models.config import connection


def is_student(username):
    with connection.cursor() as cursor:
        query = f"select name_ from student where name_ = '{username}';"
        cursor.execute(query)
        res = cursor.fetchone()
        if res:
            return True
        return False


def is_teacher(username):
    with connection.cursor() as cursor:
        query = f"select name_ from teacher where name_ = '{username}';"
        cursor.execute(query)
        res = cursor.fetchone()
        if res:
            return True
        return False
