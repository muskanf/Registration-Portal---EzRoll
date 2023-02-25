import mysql.connector


def get_class_time(major, minor, crn):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='ezroll',
                                             user='root',
                                             password='LDW3ll$1998')

        cursor = connection.cursor()
        sql_select_query = """Select TITLE, CONCAT(SUBJ_CODE, "", CRSE_NUM), SCHD_DESC, MON_DAY, TUE_DAY, WED_DAY, 
        THU_DAY, FRI_DAY, BEGIN_TIME, END_TIME, CREDIT_HR FROM classes where (SUBJ_DESC = %s or SUBJ_DESC = %s)
         and CRSE_NUM = %s"""
        # set variable in query
        cursor.execute(sql_select_query, (major, minor, crn,))
        # fetch result
        record = cursor.fetchall()

        for row in record:
            title = row[0]
            course_num = row[1]
            class_type = row[2]
            monday = row[3]
            tuesday = row[4]
            wednesday = row[5]
            thursday = row[6]
            friday = row[7]
            start_time = row[8]
            end_time = row[9]
            credit_hour = row[10]

            print(title + " " + course_num + " " + class_type + " " + monday + " " + tuesday
                  + " " + wednesday + " " + thursday + " " +friday + " " + start_time
                  + " " + end_time + " " + credit_hour + "\n")

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")

get_class_time("Computer Science", "Business Information&Analytics", 1672)
get_class_time("Computer Science", "Business Information&Analytics", 3140)
