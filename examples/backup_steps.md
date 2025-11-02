# Before steps  
## 1.Update Raspberry Pi OS and Packages:  
Keeping your Pi up-to-date ensures you’re backing up the latest security patches and stable packages.  
`sudo apt update && sudo apt full-upgrade -y`  
## 2.Clean Up Unnecessary Files:  
Remove temporary files, old caches, or unused packages to reduce the backup image size and ensure a clean snapshot.  
sudo apt autoremove -y  
sudo apt clean  
Safely Shut Down Before Removing the SD Card (if using an external machine):  
`sudo shutdown now`  
  
  
  
## 1.Shut Down Raspberry Pi: Ensure the system is powered off to prevent data corruption.  
## 2.Remove the sd card  : Take out the backup chip   from the Raspberry Pi.  
## 3.Connect to a Computer: Use a reader to connect the sd card to another computer.  
  
## 4.use `sudo dd if=/dev/sdb of=~/pi_backup.img bs=1M` Replace /dev/sdb with your actual SD card device and adjust the output path as desired.  
## 5.put it in lexar  

