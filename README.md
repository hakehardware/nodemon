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

### Run Nodemon
```
python3 app.py
```
