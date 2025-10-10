# 🖥️🛋️ RC Couches Telepresence

## Description

This tool aims to bridge the in-person couches at the RC hub with the remote couches in virtual RC, such that folks at RC can hang out in the same space and "see" each other, even when they're thousands of miles apart.

A Debian setup at the hub makes this possible by allowing in-person RCers to launch a couch bridge session—or, better phrased, open the couch portal! Meanwhile, a Zulip bot notifies all RCers of the event and shares the corresponding Zoom link so that they can join virtually.

This project was collaboratively created by [Dave Long](https://github.com/demaere-oiie), [Adrien Lynch](https://github.com/aadriien), [Matt Megaard](https://github.com/mmegaard), and [Sharon Sung](https://github.com/minsun-ss) during the Fall 2 (Sept 2025) Pairing Jam event at [the Recurse Center](https://www.recurse.com)!

## Physical setup

The macropad in the hub are bound to keyboard settings F1 (killall), F2 (launchrctv), and F3 (launchzoom).

RCTV application is the result of a separate application (rctv). Information about this can be found here!: https://github.com/fcjr/rctv.py

## Installation

Python dependencies are managed by poetry.

### For the python messaging:

To install:
```
make setup
```

To run the bot:
```
make run
```

### For the backend:

To start the zoom session:
```
./launchzoom
```

To end the zoom session:
```
./killall
```

OR
```
./launchrctv
```

# Relevant env variables required:

```
# this is for the RCTC
RCTV_TOKEN= 
ZULIP_API_KEY=
ZULIP_EMAIL=
ZULIP_URL=
```

