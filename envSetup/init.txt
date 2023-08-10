# Raspberry Pi headless initial tweaks

# Add new user and make him sudoer
useradd <new user>
useradd <new user> sudo

# Disable stock user's autologin & delete
systemctl disable getty@tty && reboot
userdel pi

# Disable display manager service
systemctl disable ligtdm

# Remove xserver
apt remove xserver-xorg

# Disable VNC server for remote access
vncserver-x11-serviced
apt remove realvnc-vnc-server

# Install xrdp for remote GUI
apt install xrdp

# Get low level config
vcgencmd get_config int
vcgencmd get_config str

# Monitor GPU temperature & volts
vcgencmd measure_temp
vcgencmd measure_volts

# Configure Pi from commandline
raspi-config

# Shutdown
shutdown -h now

# Install remmina client on a
# desktop to access Pi's GUI
apt install remmina

# See pin map
pinout
