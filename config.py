import sys
import datetime

part = sys.argv[1]
rc = sys.argv[2]
time = sys.argv[3]


filething=""
with open('C:/Users/elija/OneDrive/Desktop/Training App/rest.cfg','r') as f:
    filething=f.readlines()
    for line in range(0,len(filething)):
        vals = filething[line].split()
        if vals[0] == part:
            if rc == "rest":
                filething[line] = vals[0]+" "+time+" "+vals[2]+"\n"
                break
            elif rc == "current":
                filething[line] = vals[0]+" "+vals[1]+" "+time
                break
            else:
                print("Invalid command "+rc)
                break
    if filething == f.readlines():
        print("No value changed. Check spelling.")


with open('C:/Users/elija/OneDrive/Desktop/Training App/rest.cfg','w') as f:
    writefile = ""
    for i in filething:
        writefile = writefile + i
    f.write(writefile)
    print("Updated rest.cfg")
with open('C:/Users/elija/OneDrive/Desktop/Training App/event_log.txt','a') as f:
    now = datetime.datetime.now()
    f.write(now.strftime("%Y-%m-%d %H:%M:%S")+" set "+part+" "+rc+"\n")
