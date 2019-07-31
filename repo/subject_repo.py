import traceback

from django.db import connection


class SubjectRepo(object):

    def fetch_subjects(self):
        query = "SELECT faculty, subject_name FROM subject ORDER BY subject_id"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows is None:
                    return None
                else:
                    subjects = list()
                    for row in rows:
                        subject = {"name": row[1], "faculty": row[0]}
                        subjects.append(subject)
                return subjects
        except Exception as e:
            traceback.print_exc()
            return None

    def get_subjectid(self, faculty, subject):
        query = "SELECT subject_id FROM subject WHERE faculty=%s AND subject_name=%s"
        try:
            with connection.cursor() as cursor:
                cursor.execute(query,[faculty,subject])
                row = cursor.fetchall()
                if row is None:
                    return None
                else:
                    return row[0]
        except Exception as e:
            traceback.print_exc()
            return None


