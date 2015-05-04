appleseed
=========

This script uses [vagrant](https://github.com/chilcote/vfuse/wiki/Vagrant) to download the latest OS X seed. 

Requirements
------------

+ VMware Fusion 7.x Professional
+ OS X 10.10.3+
+ An OS X [vagrant box](https://github.com/chilcote/vfuse/wiki/Vagrant) (valid OS X license required)
+ [Vagrant VMware provider](http://www.vagrantup.com/vmware) (purchase required)
+ [OS X Software Update Seed Configuration Utility](https://developer.apple.com/devcenter/download.action?path=/OS_X_Server/OS_X_Software_Update_Seed_Configuration_Utility/OS_X_Software_Update_Seed_Configuration_Utility.dmg) (Apple Developer account required)

Prerequisite
------------

You must have an updated OS X vagrant box (10.10.3 as of this writing). Due to licencing restrictions, it is not advisable to publicly post an OS X vagrant box. You will need to create one yourself using a valid copy of Install OS X Yosemite.app. See [vfuse](https://github.com/chilcote/vfuse/wiki/Vagrant) or [osx-vm-templates](https://github.com/timsutton/osx-vm-templates) for two ways create an OS X vagrant box. 

Instructions
------------

Clone and change directories to the repo.

    git clone git@github.com:chilcote/appleseed.git && cd appleseed

Edit `Vagrantfile` to point to your vagrant box:
    
    config.vm.box = "YOUR VAGRANT BOX"

Move your copy of [SeedConfigurationUtility.dmg](https://developer.apple.com/devcenter/download.action?path=/OS_X_Server/OS_X_Software_Update_Seed_Configuration_Utility/OS_X_Software_Update_Seed_Configuration_Utility.dmg) (Apple Developer account required) to the root of the repo.

    mv ~/Downloads/SeedConfigurationUtility.dmg /path/to/appleseed/

Launch vagrant, which will spin up a copy of OS X and automate the download of the latest OS X seed update package.

    vagrant up

You will see output indicating progress, and when finished there will be a copy of the package in the `./data` directory. There is also a `./data/seed_url` file which contains the build number as well as a direct download link for the update package in case you need to download it again.

    ls ./data
    OSXUpd10.10.4.pkg seed_url

When complete, you can delete the vagrant box until the next time a seed is released.

    vagrant destroy

License
-------

    Copyright 2015 Joseph Chilcote
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
