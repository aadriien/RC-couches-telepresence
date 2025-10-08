# 🖥️🛋️ RC Couches Telepresence

## Description

This tool aims to bridge the **in-person couches** at the RC hub with the **remote couches** in virtual RC, such that folks at RC can hang out in the same space and "see" each other, even when they're thousands of miles apart. 

A Debian setup at the hub makes this possible by allowing in-person Recursers to **launch a couches bridge session**—or, better phrased, open the couch portal! Meanwhile, a Zulip bot notifies all Recursers of the event and shares the corresponding Zoom link so that they can join virtually. 

Recursers can also **interact with the Zulip bot** by sending it a DM, or otherwise tagging it in a topic, with a request for the bridge to be opened. The bot checks the status of the bridge to reduce noise, and if it's not already open, the bot will **send a notification** to Recursers who are at the hub in person, forwarding the request.

This project was collaboratively created by [Dave Long](https://github.com/demaere-oiie), [Adrien Lynch](https://github.com/aadriien), [Matt Megaard](https://github.com/mmegaard), and [Sharon Sung](https://github.com/minsun-ss) during the Fall 2 (Sept 2025) Pairing Jam event at [the Recurse Center](https://www.recurse.com)! 


## Features

Additional features in the works! 


## Installation

Python dependencies are managed by Poetry.


### For the Zulip bot:

To **install** Python dependencies:
```
make setup
```

To run bot as a **client** (`launch` mode: one-off, when Zoom call starts):
```
make run-launch
```

To run bot as a **client** (`close` mode: one-off, when Zoom call ends):
```
make run-close
```

To run bot as a **server** (listens for & responds to messages 24/7):
```
make run-server
```

### For the backend:

To **start** the Zoom session:
```
./launchzoom
```

To **end** the Zoom session:
```
./killzoom
```


## To Do:

- rebuild scripts to launch without needing the command line (i.e., bring profile in), and not maximize not based on timing
- add the RCTV script to launch on zoom kill
- set up laptop so recurse account does not need sudo, and turn off sleep so it's functionally a server with a gui


