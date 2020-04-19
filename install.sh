#!/bin/bash
# bash -v <(curl -sL https://raw.githubusercontent.com/nrobinson2000/sentry/master/install.sh)

# Install git and pip3
sudo apt update
sudo apt install -y git python3-pip vim motion

# Install python dependencies
sudo pip3 install pyusb

# Clone the git repository
git clone https://github.com/nrobinson2000/sentry
cd sentry

# Install udev file to allow non-root access to the USB device
sudo cp 99-sentry.rules /etc/udev/rules.d/

echo "
daemon on
width 640
height 480
framerate 5
ffmpeg_output_movies off
stream_quality 90
stream_motion on
stream_maxrate 5
stream_localhost off
"

# sudo motion
# sudo chmod 777 /var/log/motion/motion.log
