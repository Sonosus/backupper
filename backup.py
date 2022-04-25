import os
from datetime import datetime
name = "sonosus" # enter username here
print("Sonosus' Quick And Dirty Backup Script")
print("Current Time:")
timenow= datetime.now()
stamp = timenow.strftime("%d-%b-%Y-%H-%M-%S ")
print(stamp)
args = "--exclude-from '/home/" + name + "/backupignore.txt' -v"
command = ("/usr/bin/rclone sync /home/" + name + " onedrive:backup/" + stamp + args)
print("Starting Backup!")
os.chdir("/home/"+ name)
os.system(command)
print("Backup Complete!")
