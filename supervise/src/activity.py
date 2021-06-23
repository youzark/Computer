import os
from time_class import time_class
from time_class import minute_to_formatted_time
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
    def __init__(self,priority_status,subject = None,section = None,description = None):
        self.priority_status = priority_status
        self.subject = subject
        self.section = section 
        self.description = description

    def activity_type_info(self,for_prompt = False):
        if for_prompt:
            info = f'性质:{self.priority_status}   科目:{self.subject}   章节:{self.section}'
            return info
        else:
            info = f'{self.priority_status}_{self.subject}_{self.section}'
            return info

    def aim_gene(self):
        if self.priority_status == '作业':
            aim = '正在写作业\n'
            if not self.subject == None:
                aim += f'科目：{self.subject}\n'
            if not self.section == None:
                aim += f'章节：{self.section}\n'
        elif self.priority_status == '复习':
            aim = '正在复习\n'
            if not self.subject == None:
                aim += f'科目：{self.subject}\n'
            if not self.section == None:
                aim += f'章节：{self.section}\n'
        elif self.priority_status == '课外':
            aim  = f'正在{self.subject}\n'
            aim += f'目标:{self.section}\n'
        else:
            aim = '正在休息\n'
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
            prompt_gen.main()
            countdown.main(duration)
            print('\n')
            self.write_file(duration)
            prompt_gen.main()
            self.time.end_interval(duration)

    def write_file(self,interval):
        if not self.act_type.priority_status == '休息':
            self.write_prompt(interval)
            self.write_record(interval)

    def write_prompt(self,interval):
        file_name = date_record_file_name_gen(self.time.get_start_date())
        if not os.path.exists(file_name):
            duration = 0
            file_prompt_inst = open('../prompt/date_report.txt','w')
            file_prompt_inst.write(f'当日累积已完成学习时间:{minute_to_formatted_time(interval)}\n')
            file_prompt_inst.write('当日完成事物列表:\n')
            file_prompt_inst.close()
        else:
            file_inst = open(file_name,'r')
            records = file_inst.readlines()
            duration = int(records[-2].strip())
            file_inst.close()
        file_prompt_inst = open('../prompt/date_report.txt','r')
        day_records = file_prompt_inst.readlines()
        day_records[0] = f'当日累积已完成学习时间:{minute_to_formatted_time(interval + duration)}\n'
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

# interval_vec 课内学习 课外学习 休息
def task_list_gen(interval_vec = (45,30,10)):
    with open('../task_list.txt','r') as f:
        task_list = []
        task_records = f.readlines()
        for task_record in task_records:
            task_record_items = task_record.split('_')
            task = []
            task.append(task_record_items[0].strip())
            task.append(task_record_items[1].strip())
            task.append(task_record_items[2].strip())
            if task[0] == '作业' or task[0] == '复习':
                task.append(interval_vec[0])
            else:
                task.append(interval_vec[1])
            task.append(interval_vec[2])
            task_list.append(task)
    return task_list


# task : activity_type info + interval + rest_interval 
def load_task_list(task_list = []):
    while not len(task_list) == 0:
        task_list.reverse()
        task = task_list.pop()
        act_type = activity_type(task[0],task[1],task[2])
        activity_inst = activity(act_type)
        activity_inst.start_exc(int(task[3]))
        print('\a')
        act_type = activity_type('休息')
        activity_inst = activity(act_type)
        activity_inst.start_exc(task[4])
        print('\a')
    while True:
        priority_status = textinput('priority_status','please input priority_status')
        if priority_status == 'end':
            exit()
        if not priority_status == 'continue':
            old_priority = priority_status
            subject = textinput('subject','please input subject')
            section = textinput('chapter','please input chapter')
            interval = textinput('time','please input study time')
        else:
            priority_status = old_priority
        act_type = activity_type(priority_status,subject,section)
        activity_inst = activity(act_type)
        activity_inst.start_exc(int(interval))
        print('\a')
        act_type = activity_type('休息')
        activity_inst = activity(act_type)
        activity_inst.start_exc(10)
        print('\a')


if __name__ == '__main__':
    print(task_list_gen())
    load_task_list(task_list_gen())
