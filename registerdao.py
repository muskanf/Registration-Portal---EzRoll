import mysql.connector
from bs4 import BeautifulSoup

# connects to the database

connection = mysql.connector.connect(host='localhost',
                                     database='ezroll',
                                     user='root',
                                     password='') #your password

cursor = connection.cursor()
sql_select_query = """Select TITLE, COURSE_CRN, SCHD_DESC, MON_DAY, TUE_DAY, WED_DAY, 
    THU_DAY, FRI_DAY, BEGIN_TIME, END_TIME, CREDIT_HR FROM classes where COURSE_CRN = %s
    and TERM_DESC = "Spring Quarter 2022" """

# to store a list of classes
classes1 = []
classes2 = []
classes3 = []
classes4 = []
classes5 = []
# to store all classes as a schedule
schedule1 = []
schedule2 = []
schedule3 = []
schedule4 = []


def get_class_time1(crn):
    # set variable in query
    cursor.execute(sql_select_query, (crn,))
    # fetch result
    record = cursor.fetchall()

    for row in record:
        title = row[0]
        course_crn = row[1]
        class_type = row[2]
        monday = row[3]
        tuesday = row[4]
        wednesday = row[5]
        thursday = row[6]
        friday = row[7]
        start_time = row[8]
        end_time = row[9]
        credit_hour = row[10]

        classes1.append([title, course_crn, class_type, monday, tuesday, wednesday, thursday, friday,
                         start_time, end_time, credit_hour])

        # print(title + " " + course_crn + " " + class_type + " " + monday + " " + tuesday
        #       + " " + wednesday + " " + thursday + " " + friday + " " + start_time
        #       + " " + end_time + " " + credit_hour + "\n")
        # print(classes1)


def get_class_time2(crn):
    # set variable in query
    cursor.execute(sql_select_query, (crn,))
    # fetch result
    record = cursor.fetchall()

    for row in record:
        title = row[0]
        course_crn = row[1]
        class_type = row[2]
        monday = row[3]
        tuesday = row[4]
        wednesday = row[5]
        thursday = row[6]
        friday = row[7]
        start_time = row[8]
        end_time = row[9]
        credit_hour = row[10]

        classes2.append([title, course_crn, class_type, monday, tuesday, wednesday, thursday, friday,
                         start_time, end_time, credit_hour])


def get_class_time3(crn):
    # set variable in query
    cursor.execute(sql_select_query, (crn,))
    # fetch result
    record = cursor.fetchall()

    for row in record:
        title = row[0]
        course_crn = row[1]
        class_type = row[2]
        monday = row[3]
        tuesday = row[4]
        wednesday = row[5]
        thursday = row[6]
        friday = row[7]
        start_time = row[8]
        end_time = row[9]
        credit_hour = row[10]

        classes3.append([title, course_crn, class_type, monday, tuesday, wednesday, thursday, friday,
                         start_time, end_time, credit_hour])


def get_class_time4(crn):
    # set variable in query
    cursor.execute(sql_select_query, (crn,))
    # fetch result
    record = cursor.fetchall()

    for row in record:
        title = row[0]
        course_crn = row[1]
        class_type = row[2]
        monday = row[3]
        tuesday = row[4]
        wednesday = row[5]
        thursday = row[6]
        friday = row[7]
        start_time = row[8]
        end_time = row[9]
        credit_hour = row[10]

        classes4.append([title, course_crn, class_type, monday, tuesday, wednesday, thursday, friday,
                         start_time, end_time, credit_hour])


def get_class_time5(crn):
    # set variable in query
    cursor.execute(sql_select_query, (crn,))
    # fetch result
    record = cursor.fetchall()

    for row in record:
        title = row[0]
        course_crn = row[1]
        class_type = row[2]
        monday = row[3]
        tuesday = row[4]
        wednesday = row[5]
        thursday = row[6]
        friday = row[7]
        start_time = row[8]
        end_time = row[9]
        credit_hour = row[10]

        classes5.append([title, course_crn, class_type, monday, tuesday, wednesday, thursday, friday,
                         start_time, end_time, credit_hour])


#to read from register.html
# r = open('register.html', 'r')
# results = []
# soup = BeautifulSoup(r, "html.parser")
#
# for element in soup.findAll('div'):
#     name = element.find('div', class_="column")
#     if name not in results:
#         results.append(name)
# print(results)

crn1 = input("Enter crn in XXXX XXXX format ") # COMP 2673 -> major
crn2 = input("Enter crn2 in XXXX XXXX format ") # INFO 1021 -> minor
crn3 = input("Enter crn3 in XXXX XXXX format ") # GEOG 1203 -> elective
crn4 = input("Enter crn4 in XXXX XXXX format ") # MATH 1200 -> elective
crn5 = input("Enter crn5 in XXXX XXXX format ") # blank

get_class_time1(crn1)
get_class_time2(crn2)
get_class_time3(crn3)
get_class_time4(crn4)
#prints all of the sections for a given crn
# print(classes1)
# print(classes2)
# print(classes3)
# print(classes4)

#stores the class in its own indices
schedule1.append(classes1[0])
schedule1.append(classes2[0])
schedule1.append(classes3[0])
schedule1.append(classes4[0])
# print(schedule1[0])
# print(schedule1[1])
# print(schedule1[2])
# print(schedule1[3])

schedule2.append(classes1[1])
schedule2.append(classes2[0])
schedule2.append(classes3[1])
schedule2.append(classes4[1])

schedule3.append(classes1[3])
schedule3.append(classes2[0])
schedule3.append(classes3[2])
schedule3.append(classes4[2])


# to open/create a new html file in the write mode
f = open('results.html', 'w')

# the html code which will go in the file results.html
html_template = f"<html> <head> <title>Results </title> </head> <body> <h2>Results From Entered CRNs</h2>" \
                f" <h2> Result 1 </h2>" \
                f"<p>{schedule1[0]}</p> " \
                f" <p>{schedule1[1]}</p>" \
                f" <p>{schedule1[2]}</p>" \
                f" <p>{schedule1[3]}</p>" \
                f" <h2> Result 2 </h2>" \
                f"<p>{schedule2[0]}</p> " \
                f" <p>{schedule2[1]}</p>" \
                f" <p>{schedule2[2]}</p>" \
                f" <p>{schedule2[3]}</p>" \
                f" <h2> Result 3 </h2>" \
                f"<p>{schedule3[0]}</p> " \
                f" <p>{schedule3[1]}</p>" \
                f" <p>{schedule3[2]}</p>" \
                f" <p>{schedule3[3]}</p>" \
                f" </body> </html>"

# writing the code into the file
f.write(html_template)

# close the file
f.close()
