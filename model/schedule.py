from repo.subject_repo import SubjectRepo


class Schedule(object):
    def __init__(self):
        self.__subject_id = None
        self.__faculty = None
        self.__subject = None
        self.__day_no = None
        self.__class_no = None
        self.__start_time = None
        self.__end_time = None

    @property
    def subject_id(self):
        return self.__subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        self.__subject_id = subject_id

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, faculty):
        self.__faculty = faculty

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        self.__subject = subject

    @property
    def day_no(self):
        return self.__day_no

    @day_no.setter
    def day_no(self, day_no):
        self.__day_no = day_no

    @property
    def class_no(self):
        return self.__class_no

    @class_no.setter
    def class_no(self, class_no):
        self.__class_no = class_no

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, end_time):
        self.__end_time = end_time
