# 🖥️🛋️ RC Couches Telepresence

## Description

This tool aims to bridge the **in-person couches** at the RC hub with the **remote couches** in virtual RC, such that folks at RC can hang out in the same space and "see" each other, even when they're thousands of miles apart. 

This project was collaboratively created by [Dave Long](https://github.com/demaere-oiie), [Adrien Lynch](https://github.com/aadriien), [Matt Megaard](https://github.com/mmegaard), and [Sharon Sung](https://github.com/minsun-ss) during the Fall 2 (Sept 2025) Pairing Jam event at [the Recurse Center](https://www.recurse.com)! 


## How It Works

A Debian setup at the hub makes this possible by allowing in-person Recursers to **launch a couches bridge session**—or, better phrased, open the couch portal! Meanwhile, a Zulip bot notifies all Recursers of the event and shares the corresponding Zoom link so that they can join virtually. 

Recursers can also **interact with the Zulip bot** by sending it a DM, or otherwise tagging it in a topic, with a request for the bridge to be opened. Tagging can be done from any public Zulip stream. 

The bot checks the status of the bridge to reduce noise, and if it's not already open, the bot will **send a notification** to Recursers who are at the hub in person, forwarding the request.


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

To run bot as a **service** (listen for and respond to messages 24/7):
```
make run-service
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


## RC Heap Cluster

**`Couches Bridge Bot` runs 24/7 on [RC's Heap Community Cluster](https://www.recurse.com/blog/126-heap-sponsors-rc-community-cluster).** This service functionality is what enables folks in the RC community to engage with the bot via Zulip messaging. 

### Overview notes:

These commands are designed for **project collaborators**, i.e. folks responsible for **maintaining the bot**. They have been granted explicit permission on the Heap Cluster, which authorizes them to perform these actions. All steps below assume that the user has already **SSH'ed into the relevant cluster machine** with valid credentials. 

For more information, reach out to [Adrien Lynch](https://github.com/aadriien) or [Florian Ragwitz](https://github.com/rafl). 

### Heap deployment:

Install **Ansible** (if needed):
```
brew install ansible
```

**Deploy `Couches Bridge Bot`** via Ansible:
```
ansible-playbook -i ansible/inventory ansible/deploy.yml
```

### Heap maintenance:

Run **new bash shell** (switch to bot service user):
```
sudo -u svc-couches-telepresence-bot bash
```

Point to bot **service user environment** (view from there):
```
export XDG_RUNTIME_DIR="/run/user/$(id -u)"
```

Check bot **service status**:
```
systemctl --user status couches-telepresence.service
```

Review any bot **service logs**:
```
journalctl --user -u couches-telepresence.service
```


## To Do:

- rebuild scripts to launch without needing the command line (i.e., bring profile in), and not maximize not based on timing
- add the RCTV script to launch on zoom kill
- set up laptop so recurse account does not need sudo, and turn off sleep so it's functionally a service with a gui


