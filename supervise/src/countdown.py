import time
import multiprocessing
from tkinter import messagebox

# countdonw for interval minutes
def main(interval):
    countdown_pro = multiprocessing.Process(target = countdown,args = [interval])
    countdown_pro.start()
    countdown_pro.join()
    print("\a")
    messagebox.showinfo("Time's up","Take a rest!")
    
#invoked by main function ,core of countdown
def countdown(interval,write_gap = 30):
    seconds = interval * 60
    while seconds > 0:
        time.sleep(write_gap)
        seconds -= write_gap 
        remain_time = seconds / 60
        p = multiprocessing.Process(target = write_interval,args = [remain_time])
        p.start()

# write interval to time.txt and update prompt
def write_interval(remain_time):
    file_inst = open("../prompt/count.txt","w")
    file_inst.write(f"剩余时间 : {round(remain_time,2)} 分钟\n" )
    print(f"remain_time : {round(remain_time,2)}")
    file_inst.close()



if __name__ == '__main__':
    main()

