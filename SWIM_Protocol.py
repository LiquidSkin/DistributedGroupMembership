
#Vignesh Raghav and Mahesh Chandra


from SWIM import membership_process
import time
import json
crash_list = []
process_crash_list = []
process_active_list = []
log_list = []
with open('crashed_processes.json') as fp:
    crashes = json.load(fp)

    print("printing crashes")
    print(crashes)


for key,values in membership_process.items():
     key_value = key
     for value in values:
         value_key = value
         time_value = time.time()
         time_value = repr(time_value)
         print(key_value + "  "  + " process pinging the process" + " " + value_key + " " +"at" + " " + time_value)

         if crashes[value_key] == 'crashed' and value not in process_crash_list:

             message1 = key + "is pinging the process" + " " + value_key + "at" + " "  + time_value

             log_list.append(message1)
             time.sleep(10)
             print(value_key + " " + "process is not responding to the ping request")
             message = value_key + " " + " process is not responding to the ping request"
             log_list.append(message)
             with open('SwimLogs.txt', 'w+') as fp:
                 for item in log_list:
                     fp.write("%s\n" % item)
             process_crash_list.append(value)
         elif crashes[value_key] == 'Active' and value not in process_active_list:
             time_value1 = time.time()
             time_value1= repr(time_value)
             mssg1 = key + "  " +  "is pinging the process" + " " + value_key + "at" + "  " +  time_value1
             log_list.append(mssg1)
             time.sleep(2)
             print(value_key + " " + "is responding to the ping request")
             mssg = value_key + " " + " process is responding to the ping request" + "at" + "  " + time_value1
             log_list.append(mssg)
             with open('SwimLogs.txt', 'w+') as fp:
                 for item in log_list:
                     fp.write("%s\n" % item)
             process_active_list.append(value)



for key, value in crashes.items():
    if crashes[key] == 'crashed' and key not in process_crash_list:
        time.sleep(10)
        print("Process" + "  " + key + "  " + "is not responding to the ping request")
        process_crash_list.append(key)


print(process_crash_list)
print(process_active_list)