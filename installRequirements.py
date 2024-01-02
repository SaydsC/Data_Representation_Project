# Python Installation Checklist
# Before packages can be installed, ensure that a Python installation containing the necessary files needed for installing  packages
# is in place by following the installation requirements
# here https://www.activestate.com/resources/quick-reads/python-package-installation-on-windows/#python-installation-requirements.

import sys
import subprocess

# taken from https://www.activestate.com/resources/quick-reads/how-to-install-python-packages-using-a-script/

# read the requirements.txt file
with open('requirements.txt', "r") as f:
    requirements =  list(map(lambda x: x.split("==")[0], f.readlines()))
   

for r in requirements:
    # The following script will run pip as a subprocess to install one or more packages, and then print an updated list of installed packages:
    subprocess.call([sys.executable, '-m', 'pip', 'install',
    r])

    
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
   
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print(installed_packages)