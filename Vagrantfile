# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "osx114"
  config.vm.boot_timeout = 300
  config.vm.synced_folder "./data", "/vagrant_data"
  config.vm.provision "file", source: "./OS_X_Software_Update_Seed_Configuration_Utility.dmg", destination: "/private/var/tmp/OS_X_Software_Update_Seed_Configuration_Utility.dmg"
  config.vm.provision "shell", path: "./appleseed.py"
end
