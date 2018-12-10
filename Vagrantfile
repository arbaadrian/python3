# -*- mode: ruby -*-
# vi: set ft=ruby :

#### Variables

box = "centos/7"
cpus = 2

#### Code

Vagrant.configure("2") do |config|

  config.vm.define "python" do |py|
    py.vm.box = box
    py.vm.network "private_network", ip: "192.168.56.20"
    # py.vm.synced_folder ".", "/vagrant", type: "smb"
    # py.vm.synced_folder ".", "/python"
    py.vm.provider :virtualbox do |vb|
      vb.customize [
        'modifyvm', :id,
        '--natdnshostresolver1', 'on',
        '--memory', '2048',
        '--cpus', cpus
        ]
    end
    py.vm.provision :hosts, :add_localhost_hostnames => false
    # py.vm.provision "shell", :path => "general_provision.sh"
  end
end