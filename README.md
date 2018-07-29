# We host our backfill script in:
# Jogchat Test digital ocean droplet:
```
206.189.76.189
```
https://docs.google.com/spreadsheets/d/1z1lsk2sjAPcxZ0nFInf2cReDjhKEc0bvCF8rch9Ev1Y/edit#gid=0


# To setup a new backfill environment on Ubuntu 16.04 server do the following
# This would require python3 to run:

https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04

Read Google docs spreadsheet using Python:
http://www.madhur.co.in/blog/2016/05/13/google-docs-spreadsheet.html



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
source ~/environments/my_env/bin/activate
```
To leave the environment, simply type the command deactivate and you will return to your original directory.
```
pip3 install requests
```
