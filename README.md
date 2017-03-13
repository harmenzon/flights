# flights

STEP 1: DEFAULTS
https://mattwilcox.net/web-development/setting-up-a-secure-home-web-server-with-raspberry-pi
sudo raspi-config
	- Change the Pi password
	- Disable "Boot to Desktop"
	- Update your Locale settings
	- Set your Hostname
	- Set the Memory Split
	- Ensure SSH is enabled
	- Commit the changes and reboot
sudo reboot

STEP 2: SETUP WIFI
https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
	network={
		ssid="Your_wifi_network"
		psk="Your_wifi_password"
	}
	
STEP 3: CHANGE USER NAME
groups
				pi adm dialout cdrom sudo audio video plugdev games users input netdev gpio i2c spi
sudo useradd -m -G adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,gpio,i2c,spi USERNAME
sudo passwd USERNAME
sudo reboot

STEP 4: REMOVE USER PI
sudo deluser --remove-all-files pi	
	
STEP 5: UPDATE && UPGRADE
sudo apt-get update
sudo apt-get upgrade

STEP 6: INSTALL PACKAGES
sudo apt-get install python3-dev python3-pip
sudo pip3 install PyYAML
sudo apt-get install python3-pandas
sudo apt-get install git

STAP 7: CREATE DIRECTORY
sudo mkdir /services
sudo mkdir -p /services/python/flights

STAP 8: GIT


STEP 9: RUNNING PYTHON SCRIPT AT BOOT
sudo crontab -e

using your cursor keys scroll to the bottom and add the following line:
@reboot python3 /services/python/flights/tracker.py &

STEP 10: REBOOT
sudo reboot

