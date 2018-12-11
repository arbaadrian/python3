# Instructions

## Starting and running the container

```bash
# host
vagrant up

# guest
./bDocker
./rDocker

# container
pipenv --python 3.6
pipenv install
pipenv run ./query-rpm.py vi
```

## Currently, the code does not work for Vagrant, todo