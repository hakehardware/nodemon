# Nodemon
Monitors a Spacemesh Node


### Install Instructions (Ubuntu)

```
git clone https://github.com/hakehardware/nodemon.git
```

```
cd nodemon
```

### Create & Activate Virtual Environment
Make sure you have python-venv installed

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Create Config
```
cp example.config.json config.json
```

### Update the Config
For every node that you have, add a new entry. The name can be whatever you want. Public should be the IP and port for the public endpoints for grpc. Private should be the IP and port for the private endpoints for grpc.

You also need to update the config with a path to your state file. This should be a local path. 

### Run Nodemon
```
python3 app.py
```
## Update to Latest
If you want to update to the latest version, you can do so with git
```
git pull
```

Then make sure to install the latest requirements with 
```
pip install -r requirements.txt
```
