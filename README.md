# 🖥️🛋️ RC Couches Telepresence

## Description

This tool aims to bridge the in-person couches at the RC hub with the remote couches in virtual RC, such that folks at RC can hang out in the same space and "see" each other, even when they're thousands of miles apart.

A Debian setup at the hub makes this possible by allowing in-person RCers to launch a couch bridge session—or, better phrased, open the couch portal! Meanwhile, a Zulip bot notifies all RCers of the event and shares the corresponding Zoom link so that they can join virtually.

This project was collaboratively created by [Dave Long](https://github.com/demaere-oiie), [Adrien Lynch](https://github.com/aadriien), [Matt Megaard](https://github.com/mmegaard), and [Sharon Sung](https://github.com/minsun-ss) during the Fall 2 (Sept 2025) Pairing Jam event at [the Recurse Center](https://www.recurse.com)!

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
./killzoom
```

## To Do:

- add launch and kill zoom scripts
- rebuild scripts to launch without needing the command line (i.e., bring profile in), and not maximize not based on timing
- add the RCTV script to launch on zoom kill
- set up laptop so recurse account does not need sudo, and turn off sleep so it's functionally a server with a gui

## Features

Additional features in the works!
