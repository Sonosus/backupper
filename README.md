# Quick And Dirty Backup Script
Ultra basic backupper using rclone to remotely copy files from user's home folder to a new timestamped folder in OneDrive.

## Prerequisites
* Python 3
* rclone

## Installation
Clone repo.

Run the rclone configurator and set up a new remote called onedrive.

## Usage
Place a file named .backupignore in the home folder of the user(s) you need backed up. This file is read by rclone using the --exclude-from flag.

Replace `sonosus` on line 3 with the name of the user.

Run the script.

Each time the script is run a new timestamped folder will be created inside the `backup` folder in OneDrive.

