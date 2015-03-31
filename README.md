# API
FAForever API project

## Installation - Automatic

To setup the development environment automatic we use Vagrant and a VM.

1. Install Vagrant: http://www.vagrantup.com/downloads
2. Install VirtualBox: https://www.virtualbox.org/wiki/Downloads
3. Clone this repository
4. Open the command console and navigate to folder of this repository (check with `ls` or `dir` that `Vagrantfile` is present)
5. Run `vagrant up`

To login the vm use `vagrant ssh`.
To shutdown the vm use `vagrant halt`.
You find the data under `/vagrant` in the VM.
This folder is autmatically synced from host to guest and back.

## Start Development Server - Vagrant

Run `python3 /vagrant/manage.py runserver 0.0.0.0:8000`
