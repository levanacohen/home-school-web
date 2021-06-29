from models.config import connection


def insert_fun_task(grade, descr, link):
    with connection.cursor() as cursor:
        query = f"insert into fun_task values ('{grade}','{descr}', '{link}');"
        cursor.execute(query)
        connection.commit()
        print("inserted fun task")
