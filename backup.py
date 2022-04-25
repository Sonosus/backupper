import os; from datetime import datetime
name = "sonosus" # enter username here
timenow = datetime.now()
stamp = timenow.strftime("%d-%b-%Y-%H-%M-%S ")
print("Sonosus' Quick And Dirty Backup Script \n Current Time:" + stamp + "\n Starting Backup!")
command = ("/usr/bin/rclone sync /home/" + name + " onedrive:backup/" + stamp + "--exclude-from '/home/" + name + "/.backupignore.txt' -v")
os.chdir("/home/"+ name)
os.system(command)

