# sentry

Based on https://github.com/nmilford/stormLauncher

# Installation

```bash
$ bash -v <(curl -sL https://raw.githubusercontent.com/nrobinson2000/sentry/master/install.sh)
```

# Usage

Interactive utility:

Use the arrow keys to move the turret, press CTRL-C to exit.

```bash
$ ./sentry-control.py
```

Command line scripting:

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
