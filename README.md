appleseed
=========

This script uses vagrant to download the latest macOS seed.

Requirements
------------

+ VMware Fusion 8.5+ Professional
+ macOS 10.12+
+ A macOS [vagrant box](https://github.com/chilcote/vfuse) (valid macOS license required)
+ [Vagrant VMware provider](http://www.vagrantup.com/vmware) (purchase required)
+ [macOS Sierra Developer Beta Access Utility.dmg](https://developer.apple.com/devcenter/download.action?path=/OS_X_Server/OS_X_Software_Update_Seed_Configuration_Utility/OS_X_Software_Update_Seed_Configuration_Utility.dmg) (Apple Developer account required)

Prerequisite
------------

You must have an updated macOS vagrant box. Due to licencing restrictions, it is not advisable to publicly post an macOS vagrant box. You will need to create one yourself using a valid copy of the macOS installer app. I do this using [vfuse](https://github.com/chilcote/vfuse) or [osx-vm-templates](https://github.com/timsutton/osx-vm-templates).

Instructions
------------

Clone and change directories to the repo.

    git clone git@github.com:chilcote/appleseed.git && cd appleseed

Edit `Vagrantfile` to point to your vagrant box:

    config.vm.box = "YOUR VAGRANT BOX"

Move your copy of [macOS Sierra Developer Beta Access Utility.dmg](http://adcdownload.apple.com/OS_X/macOS_Sierra_Developer_Beta_Access_Utility/macOS_Sierra_Developer_Beta_Access_Utility.dmg) (Apple Developer account required) to the root of the repo.

    mv ~/Downloads/macOS_Sierra_Developer_Beta_Access_Utility.dmg /path/to/appleseed/

Launch vagrant, which will spin up a copy of macOS and automate the download of the latest macOS seed update package.

    vagrant up

You will see output indicating progress, and when finished there will be a copy of the package in the `./data` directory. There is also a `./data/seed_url` file which contains the build number a direct download link for the update package in case you need to download it again.

    ls ./data
    macOSUpd10.12.1.pkg seed_url

When complete, you can delete the vagrant box until the next time a seed is released.

    vagrant destroy

License
-------

    Copyright 2016 Joseph Chilcote

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
