# sentry

Based on https://github.com/nmilford/stormLauncher

# Installation

```bash
# Install git and pip3
$ sudo apt install -y git python3-pip vim

# Install python dependencies
$ sudo pip3 install pyusb

# Clone the git repository
$ git clone https://github.com/nrobinson2000/sentry
$ cd sentry

# Install udev file to allow non-root access to the USB device
$ sudo cp 99-sentry.rules /etc/udev/rules.d/

$ sudo apt install motion

daemon on

width 640

height 480

framerate 5

ffmpeg_output_movies off

stream_quality 90

stream_motion on

stream_maxrate 5

stream_localhost off

$ sudo motion
$ sudo chmod 777 /var/log/motion/motion.log
```

# Usage

```
$ python3

>>> from sentry import sentry 	# Load the sentry module
>>> sentry.up() 		# Move the sentry upwards
>>> sentry.down() 		# Move the sentry downwards
>>> sentry.left() 		# Move the sentry left
>>> sentry.right() 		# Move the sentry right
>>> sentry.stop() 		# Stop any movement in progress
>>> sentry.fire() 		# Fire the cannon
```

