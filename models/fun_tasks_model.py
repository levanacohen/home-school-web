from models.config import connection


def get_fun_tasks_by_grade(grade):
    with connection.cursor() as cursor:
        query = f"select descr, link from fun_task where class = '{grade}';"
        cursor.execute(query)
        res = cursor.fetchall()
        return res
