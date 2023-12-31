import os
import re

print("### Wait.. Filename Change Ongoing ###")
nowdir = os.getcwd()
#logdir = "\log"
#nextdir = nowdir+logdir
os.chdir(str(nowdir))

file_list = os.listdir(os.getcwd())

### Parsing ###

for file_num in range(len(file_list)):
    
    log_file = open("%s" %file_list[file_num], "r", encoding='utf-8-sig')
    log_line = log_file.readlines()
    log_file.close()

    ### OS ###
    for os_parsing in range(len(log_line)):
        os_pattern = r'^Cisco\s(IOS|Internetwork Operating System|IOS XR)\sSoftware'
        os_result = re.search(os_pattern, log_line[os_parsing])
        if os_result != None:
            os_name = os_result.group()
            break
        else:
            pass

    ### Hostname ###
    if os_name == "Cisco IOS XR Software":
        for host_parsing in range(len(log_line)):
            host_pattern = r'^\w\w/\d/\w\w\d/\w\w\w\d:.*#show.*'
            host_result = re.search(host_pattern, log_line[host_parsing])
            if host_result != None:
                hostname = host_result.group()
                hostname = hostname.split(sep = ":", maxsplit = 1)
                hostname = hostname[1]
                hostname = hostname.split(sep = "#", maxsplit = 1)
                hostname = hostname[0]
                hw_type = "ASR-9912"
                break
            else:
                pass
        os.rename("%s" %file_list[file_num],"%s.txt" %hostname)
        print("Filename %s -> %s.txt" %(file_list[file_num], hostname))
    else:
        for host_parsing in range(len(log_line)):
            host_pattern = r'^.*#show.*$'
            host_result = re.search(host_pattern, log_line[host_parsing])
            if host_result != None:
                hostname = host_result.group()
                hostname = hostname.split(sep = "#s", maxsplit = 1)
                hostname = hostname[0]
                break
            else:
                pass
        os.rename("%s" %file_list[file_num],"%s.txt" %hostname)
        print("Filename %s -> %s.txt" %(file_list[file_num], hostname))

print("### Inspection Successful ###")
input("Press enter to exit ;)")
