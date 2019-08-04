import traceback
from datetime import datetime

from django.db import connection

from model.tabRow import TabRow


class ScheduleRepo(object):

    def save(self, schedule, created_at):
        query = "INSERT INTO schedule(subject_id, day_no, start_time, end_time, class_no, added_at) VALUES(%s,%s,%s,%s,%s,%s)"
        try:
            with connection.cursor() as cursor:
                print(query)
                cursor.execute(query, [schedule.subject_id, schedule.day_no, schedule.start_time, schedule.end_time,schedule.class_no, created_at])
                return True
        except Exception as e:
            traceback.print_exc()
            return False

    def getTeacher(self, id):
        query = "SELECT first_name FROM teacher WHERE teacher_id=%i"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [id])
                row = cursor.fetchone()
                return row[0]
        except Exception as e:
            traceback.print_exc()
            return None

    def getId(self, email):
        query = "SELECT teacher_id FROM teacher WHERE email = %s"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, [email])
                row = cursor.fetchone()
                print(row[0])
                return row[0]
        except Exception as e:
            traceback.print_exc()
            return None

    def fetchScheduleAll(self, day):
        query = "SELECT teacher_id, first_name FROM teacher"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows is None:
                    return None
                else:
                    table = list()
                    for row in rows:
                        tabRow = TabRow()
                        tabRow.teacher_name = row[1]
                        row = self.fetchSchedule(row[0],day)
                        tabRow.time1 = row.time1
                        tabRow.time2 = row.time2
                        tabRow.time3 = row.time3
                        tabRow.time4 = row.time4
                        tabRow.time5 = row.time5
                        table.append(tabRow)
                    return table
        except Exception as e:
            traceback.print_exc()
            return None

    def fetchSchedule(self, teacher_id, day_no):
        query = "SELECT sch.class_no, sub.subject_name, sch.start_time FROM schedule sch INNER  JOIN subject sub ON sch.subject_id = sub.subject_id WHERE sub.teacher_id = %s AND sch.day_no = %s"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query,[teacher_id, day_no])
                rows = cursor.fetchall()
                if rows is None:
                    return None
                else:
                    tab_row = TabRow()
                    for row in rows:
                        if row[2] == "11:00":
                            tab_row.time1 = (row[0]+" "+row[1])
                        elif row[2] == "12:00":
                            tab_row.time2 = (row[0]+" "+row[1])
                        elif row[2] == "01:00":
                            tab_row.time3 = (row[0]+" "+row[1])
                        elif row[2] == "02:30":
                            tab_row.time4 = (row[0]+" "+row[1])
                        elif row[2] == "3:30":
                            tab_row.time5 = (row[0]+" "+row[1])
                return tab_row
        except Exception as e:
            traceback.print_exc()
            return None
