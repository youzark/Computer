import time_class
import time
import multiprocessing
import prompt_gen

# countdonw for interval minutes
def main(interval):
    countdown_pro = multiprocessing.Process(target = countdown,args = [interval])
    countdown_pro.start()
    countdown_pro.join()
    
#invoked by main function ,core of countdown
def countdown(interval,write_gap = 10):
    seconds = interval * 60
    while seconds > 0:
        remain_time = seconds / 60
        p = multiprocessing.Process(target = write_interval,args = [remain_time])
        p.start()
        time.sleep(write_gap)
        seconds -= write_gap 

# write interval to time.txt and update prompt
def write_interval(remain_time):
    file_inst = open("../prompt/count.txt","w")
    file_inst.write(f"剩余时间 : {time_class.minute_to_formatted_time(remain_time)}\n" )
    print(f"remain_time : {round(remain_time,2)}")
    file_inst.close()
    prompt_gen.main()

if __name__ == '__main__':
    main()

