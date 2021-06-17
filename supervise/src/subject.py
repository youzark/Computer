class subject:
    def __init__(self,name,name_english,year,semester,compulsory):
        self.name = name
        self.year = year
        self.english_name = english_name
        self.semester = semester
        self.compulsory = compulsory
        self.chapter_list = []

    def get_name(self):
        return self.name

    # automatically called by chapter_init_ function
    def add_chapter(self,chapter):
        self.chapter_list.append(chapter)


class chapter:
    def __init__(self,chapter_number,subject,chapter_name = None):
        self.chapter_name = chapter_name
        self.chapter_number =chapter_number
        self.homework_list = []
        self.finished_homework_info_list = []
        self.subject = subject
        subject.add_chapter(self)
        
    def add_homework(self,homework):
        self.homework_list.append(homework)

    def finish_homework(self,homework):
        self.finished_homework_info_list.append(homework)


class homework:
    def __init__(self,subject,chapter,ddl):
        self.subject = subject
        self.chapter  = chapter
        self.ddl = ddl
