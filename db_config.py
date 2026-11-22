import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host='gateway01.ap-northeast-1.prod.aws.tidbcloud.com',
        user='4J8GvDVCSRkvBV1.root',
        password='m5Skj4Oj0BTSmBFi',
        database='student_task_manager',
        port=4000
    )

    return connection
