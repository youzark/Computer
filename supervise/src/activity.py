import os
from time_class import time_class
import countdown

#parameter:
#    priority_status: study rest afterschool
#    subject:study subject
#    chapter:subject chapter
#    description:
def date_record_file_name_gen(date):
    file_name = f'../prompt/date_record/{date[0]}_{date[1]}_{date[2]}'
    return file_name

def date_formate(date):
    formate = f'{date[0]}_{date[1]}_{date[2]}'
    return formate

class activity_type:
    def __init__(self,priority_status,subject = None,chapter_num = 0,description = None):
        self.priority_status = priority_status
        self.subject = subject
        self.chapter_num = chapter_num
        self.description = description
    def activity_type_info(self):
        info = f'{self.priority_status}_{self.subject}_{self.chapter_num}'
        return info
    def aim_gene(self):
        if self.priority_status == 'homework':
            if not self.subject == None:
                aim = f'目标科目：{self.subject}\n'
            if not self.chapter_num == 0:
                aim += f'目标章节：{self.chapter_num}\n'
        else:
            aim =f'正在:self.{self.priority_status}\n'
        return aim

class activity: 
    def __init__(self,act_type):
        self.time = time_class()
        self.act_type = act_type
        self.finished = False

    def start_exc(self,duration = 0):
        if not duration == 0:
            file_inst = open('../prompt/aim.txt','w')
            file_inst.write(self.act_type.aim_gene())
            file_inst.close()
            countdown.main(duration)
            self.write_file(duration)
            self.time.end_interval(duration)

    def write_file(self,interval):
        file_name = date_record_file_name_gen(self.time.get_start_date())
        if not os.path.exists(file_name):
            duration = 0
            file_inst = open(file_name,'w')
            file_inst.close()
        else:
            file_inst = open(file_name,'r')
            records = file_inst.readlines()
            duration = int(records[-1])
            file_inst.close()
        file_inst = open(file_name,'a')
        file_inst.write('\n')
        file_inst.write(date_formate(self.time.get_start_date()))
        file_inst.write('\n')
        file_inst.write(self.act_type.activity_type_info())
        file_inst.write('\n')
        file_inst.write(str(duration+interval))

if __name__ == '__main__':
    act_type = activity_type('homework','计算方法','10')
    activity_inst = activity(act_type)
    activity_inst.start_exc(45)
