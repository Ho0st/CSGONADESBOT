import psycopg2
from config import user_name, password, host, db_name
from datetime import  datetime


def TestInsert(user_id,nade_info,request_date,status,position_info):
    try:
        conn = psycopg2.connect(dbname=db_name, user=user_name,
                                    password=password, host=host)
        cursor =conn.cursor()

        cursor.execute("insert into info_monitor(user_id,nade_info,request_date,position_info,status)values(%s,%s,%s,%s,%s)",(user_id,nade_info,request_date,position_info,status))
        conn.commit()
        cursor.close()


        conn.close()
    except:
        print('DB CONNECTION ERROR TestInsert')


def users_count():
    try:
        conn = psycopg2.connect(dbname=db_name, user=user_name,
                                password=password, host=host)

        cursor = conn.cursor()
        cursor.execute("select max(id_table) from new_users_info")
        res = cursor.fetchall()
        for i in res:
            for j in i:
                return j
        cursor.close()
        conn.close()
    except:
        print('DB CONNECTION ERROR users_count')


def db_take(map_name, position_number):
    try:
        conn = psycopg2.connect(dbname=db_name, user=user_name,
                                password=password, host=host)
        cursor = conn.cursor()
        slct = "select link_video from nade_video_3 where map_name = %s and position_number =%s"
        cursor.execute(slct, (map_name.lower(), position_number.lower()))
        return cursor.fetchall()
        print(type(cursor.fetchall()))
        cursor.close()
        conn.close()

    except:
        print('DB CONNECTION ERROR db_take')


def addUserToDB(first_name, last_name, username, user_id, time):
    try:
        conn = psycopg2.connect(dbname=db_name, user=user_name,
                                password=password, host=host)

        cursor = conn.cursor()
        cursor.execute("select id_table from new_users_info  where user_id = %s", (str(user_id),))
        check_result = cursor.fetchall()
        print(check_result, 'ID FROM DATABASE')
        if not check_result:
            command = "insert into new_users_info(first_name,last_name,user_name,user_id,add_time) values(%s,%s,%s,%s,%s)"
            cursor.execute(command, (first_name, last_name, username, user_id, time))
        else:
            print('ALREADY IN THE DATABASE')
        view = conn.cursor()
        view.execute("select * from new_users_info")
        conn.commit()
        cursor.close()
        view.close()
        conn.close()
    except:
        print('DB CONNECTION ERROR addUsersToDB')


def id_take():
    try:
        conn = psycopg2.connect(dbname=db_name, user=user_name,
                                password=password, host=host)

        cursor = conn.cursor()
        cursor.execute("select user_id from new_users_info")
        res = cursor.fetchall()
        return res
        cursor.close()
        conn.close()
    except:
        print('DB CONNECTION ERROR ID TAKE')


def TestDB():
    conn = psycopg2.connect(dbname=db_name, user=user_name,
                                password=password, host=host)
    date = datetime.today().strftime("%Y-%m-%d")
    cursor = conn.cursor()
    print(date,type(date))
    date = '%'+date+'%'
    print(date, type(date))
    cursor.execute("select count(nade_info) from info_monitor where request_date LIKE %s",(date,))
    res = cursor.fetchall()
    return res
    cursor.close()
    conn.close()