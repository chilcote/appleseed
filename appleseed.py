#!/usr/bin/env python

##############################################################################
# Copyright 2015 Joseph Chilcote
# 
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not
#  use this file except in compliance with the License. You may obtain a copy
#  of the License at
# 
#       http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
##############################################################################

import subprocess, glob, shutil, plistlib

def mount_dmg(dmg):
    p = subprocess.check_output(['/usr/bin/hdiutil', 'attach', dmg, '-plist'])
    d = plistlib.readPlistFromString(p)
    for i in d['system-entities']:
        if 'mount-point' in str(i):
            return i['mount-point']

def install(pkg):
    p = subprocess.Popen(['sudo', '/usr/sbin/installer', '-pkg', pkg, '-target', '/'])
    p.communicate()

def get_update_id():
    p = subprocess.check_output(['/usr/sbin/softwareupdate', '-l'])
    for line in p.splitlines():
        if 'OSXUpd' in line:
            return line.split('* ')[1].strip(), line.split('(')[1].strip()[:-1]

def download_seed(seed):
    p = subprocess.Popen(['sudo', '/usr/sbin/softwareupdate', '-d', seed])
    p.communicate()

def dl_url():
    d = plistlib.readPlist(glob.glob('/Library/Updates/031-*/*.extraInfo')[0])
    return d['ServerMetadataURL'].replace('.smd', '.pkg').strip()

def main():
    mount = mount_dmg(glob.glob('/private/var/tmp/*.dmg')[0])
    install(glob.glob(mount + '/*.pkg')[0])
    update_id, build = get_update_id()
    download_seed(update_id)
    shutil.copy(glob.glob('/Library/Updates/031-*/OSXUpd*')[0], '/vagrant_data/')
    url = dl_url()
    with open('/vagrant_data/seed_url', 'w') as f:
        f.write(build + '\n')
        f.write(url)
    print 'Build: %s' % build
    print 'URL: %s' % url

if __name__ == '__main__':
  main()