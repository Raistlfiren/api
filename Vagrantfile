# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = "2"

box = 'trusty64'
box_url = 'https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box'
hostname = 'faf.api'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = box
  config.vm.box_url = box_url

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
  end

  config.vm.synced_folder ".", "/vagrant"

  # -- Networking ------------------------------------------
  config.vm.hostname = hostname

  # Web Development Server
  config.vm.network :forwarded_port, guest: 5000, host: 5000
  # My Sql DB
  config.vm.network :forwarded_port, guest: 3306, host: 5001

  # -- Provisioning ----------------------------------------
  provision_dir = "vagrant/provision"

  vm = config.vm
  vm.provision :shell, path: "#{provision_dir}/vagrant_provision"
  vm.provision :shell, path: "#{provision_dir}/python_provision"

  config.vm.provision :docker do |d|
    d.pull_images "mysql"
    d.run "mysql",
      args: ' -e MYSQL_ROOT_PASSWORD="test1234" -e MYSQL_DATABASE="faf_lobby" --restart="always" --name faf -p 3306:3306'
  end
end
