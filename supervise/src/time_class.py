import time

# used to record time infomation of a task(activity)
# start_time(when does this activity was assigned)
# time spent on it each start time and end time
# ddl
class time_class:
    def __init__(self):
        self.start_ticks = time.time()
        self.duration = 0
        # work_instance_list [(starttime,endtime,duration)]
        self.act_instance_list = []

    def get_start_date(self):
        start_localtime = time.localtime(self.start_ticks)
        return (start_localtime[0],start_localtime[1],start_localtime[2])

    def get_start_clock(self):
        start_localtime = time.localtime(self.start_ticks)
        return (start_localtime[3],start_localtime[4],start_localtime[5])

    def set_ddl(self,ddl):
        self.ddl = ddl

    # start will record the start time in a file and will end() is called 
    # start will subtract two timepoint and calculate the duration
    # used to start a work instance with the computer shutdown
    def start(): # start a work instance rather than the start of the activity
        pass
    def end():
        pass

    # no start_interval needed , end_interval is used to record information ,marked the end of  a work instance
    def end_interval(self,interval): 
        end_time = time.time()
        duration = interval * 60
        start_time = end_time - duration
        self.act_instance_list.append((start_time,end_time,duration))

