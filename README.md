https://docs.google.com/spreadsheets/d/1z1lsk2sjAPcxZ0nFInf2cReDjhKEc0bvCF8rch9Ev1Y/edit#gid=0

This would require python3 to run:

https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04

How to read CSV file in Python:
https://www.alexkras.com/how-to-read-csv-file-in-python/



In Ubuntu, we can do:
```
sudo apt-get update
python3 -V
sudo apt-get install -y python3-pip
```
To make an env:
```
sudo apt-get install -y python3-venv
mkdir environments
cd environments
python3 -m venv my_env
ls my_env
source my_env/bin/activate
```
To leave the environment, simply type the command deactivate and you will return to your original directory.
```
pip3 install requests
```
