This is how this program should be executed.

```
virtualenv lb
source ./lb/bin/activate	# To activate the virtualenv
pip install flask
pip install pytest
pip install requests
pip install pyyaml

  docker build -t flask-server . 		# Creates the flask-server image to set up containers from
  pytest		# To run the tests (containers must be pre-loaded)
  make		# Sets up containers, runs tests, then tears down containers (flask-server image must be pre-built)
  // If faced with the error: [cannot update snap namespace: cannot create symlink in "/etc/docker": existing file in the way]
  sudo rm -rf /etc/docker
  sudo snap refresh

deactivate		# To deactivate the virtualenv
```
