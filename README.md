# sentry

Based on https://github.com/nmilford/stormLauncher

# Installation

```bash
# Install python dependencies
$ sudo pip3 install pyusb

# Install udev file to allow non-root access to the USB device
$ sudo cp 99-sentry.rules /etc/udev/rules.d/
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

