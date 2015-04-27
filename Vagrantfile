# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "osx103"
  config.vm.boot_timeout = 300
  config.vm.synced_folder "./data", "/vagrant_data"
  config.vm.provision "file", source: "./SeedConfigurationUtility.dmg", destination: "/private/var/tmp/SeedConfigurationUtility.dmg"
  config.vm.provision "shell", path: "./appleseed.py"
end
