from models.config import connection


def insert_task(grade, day, hour, date, descr):
    curr_id = get_current_task_id()
    with connection.cursor() as cursor:
        query = f"insert into task values (Null, '{grade}', {day}, '{hour}', '{date}', '{descr}');"
        cursor.execute(query)
        connection.commit()
        print("inserted")
    insert_student_task(grade, curr_id)


def get_current_task_id():
    with connection.cursor() as cursor:
        query = "SELECT `AUTO_INCREMENT` FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'homeschooldb' AND TABLE_NAME = 'task';"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        return result[0]['AUTO_INCREMENT']


def get_tasks_by_class_and_date(class_, date):
    with connection.cursor() as cursor:
        query = "select homework from lesson where class = '{}' and date = {}".format(class_, date)
        cursor.execute(query)
        tasks = cursor.fetchall()
        return tasks


def get_all_students(class_):
    with connection.cursor() as cursor:
        query = f"select name_ from student where class = '{class_}'"
        cursor.execute(query)
        students = cursor.fetchall()
        return students


def insert_student_task(class_, task_id):
    students = get_all_students(class_)
    with connection.cursor() as cursor:
        for student in students:
            query = f"insert into student_task values('{student['name_']}', {task_id}, 0)"
            cursor.execute(query)
            connection.commit()
    print("insert students")
