import os
from time_class import time_class
import countdown
import prompt_gen
from turtle import textinput

#parameter:
#    priority_status: homework review rest afterschool
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

    def activity_type_info(self,for_prompt = False):
        if for_prompt:
            info = f'性质:{self.priority_status}   科目:{self.subject}   章节:{self.chapter_num}'
            return info
        else:
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
            prompt_gen.main()
            self.time.end_interval(duration)

    def write_file(self,interval):
        file_name = date_record_file_name_gen(self.time.get_start_date())
        if not os.path.exists(file_name):
            duration = 0
            file_inst = open(file_name,'w')
            file_prompt_inst = open('../prompt/date_report.txt','w')
            file_prompt_inst.write(f'当日累积已完成学习时间:{interval} 分钟\n')
            file_prompt_inst.write('当日完成事物列表:\n')
            file_prompt_inst.close()
            file_inst.close()
        else:
            file_inst = open(file_name,'r')
            records = file_inst.readlines()
            duration = int(records[-2].strip())
            file_inst.close()
        file_prompt_inst = open('../prompt/date_report.txt','r')
        day_records = file_prompt_inst.readlines()
        day_records[0] = f'当日累积已完成学习时间:{duration+interval} 分钟\n'
        file_prompt_inst.close()
        file_prompt_inst = open('../prompt/date_report.txt','w')
        day_records = file_prompt_inst.writelines(day_records)
        file_prompt_inst.close()
        file_prompt_inst = open('../prompt/date_report.txt','a')
        day_records = file_prompt_inst.write(self.act_type.activity_type_info(True) + f'   时间:{interval} 分钟')
        day_records = file_prompt_inst.write('\n')
        file_prompt_inst.close()
        file_inst = open(file_name,'a')
        file_inst.write(date_formate(self.time.get_start_date()))
        file_inst.write('\n')
        file_inst.write(self.act_type.activity_type_info()+f'_{interval}')
        file_inst.write('\n')
        file_inst.write(str(duration+interval))
        file_inst.write('\n')
        file_inst.write('\n')

    def write_prompt(self,interval):
        file_name = date_record_file_name_gen(self.time.get_start_date())
        if not os.path.exists(file_name):
            duration = 0
            file_prompt_inst = open('../prompt/date_report.txt','w')
            file_prompt_inst.write(f'当日累积已完成学习时间:{interval} 分钟\n')
            file_prompt_inst.write('当日完成事物列表:\n')
            file_prompt_inst.close()
        else:
            file_inst = open(file_name,'r')
            records = file_inst.readlines()
            duration = int(records[-2].strip())
            file_inst.close()
        file_prompt_inst = open('../prompt/date_report.txt','r')
        day_records = file_prompt_inst.readlines()
        day_records[0] = f'当日累积已完成学习时间:{duration+interval} 分钟\n'
        file_prompt_inst.close()
        file_prompt_inst = open('../prompt/date_report.txt','w')
        file_prompt_inst.writelines(day_records)
        file_prompt_inst.close()
        file_prompt_inst = open('../prompt/date_report.txt','a')
        file_prompt_inst.write(self.act_type.activity_type_info(True) + f'   时间:{interval} 分钟')
        file_prompt_inst.write('\n')
        file_prompt_inst.close()

    def write_record(self,interval):
        file_name = date_record_file_name_gen(self.time.get_start_date())
        if not os.path.exists(file_name):
            duration = 0
        else:
            file_inst = open(file_name,'r')
            records = file_inst.readlines()
            duration = int(records[-2].strip())
            file_inst.close()
        file_inst = open(file_name,'a')
        file_inst.write(date_formate(self.time.get_start_date()))
        file_inst.write('\n')
        file_inst.write(self.act_type.activity_type_info()+f'_{interval}')
        file_inst.write('\n')
        file_inst.write(str(duration+interval))
        file_inst.write('\n')
        file_inst.write('\n')

if __name__ == '__main__':
    while not stop:
        priority_status = textinput('priority_status','please input priority_status')
        subject = textinput('subject','please input subject')
        chapter = textinput('chapter','please input chapter')
        interval = textinput('time','please input study time')
        act_type = activity_type(priority_status,subject,chapter)
        activity_inst = activity(act_type)
        activity_inst.start_exc(interval)
        act_type('rest')
