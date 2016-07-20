#!/System/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python

import os
import distutils.spawn

system_packages = ['wget','cask']

def is_tool(name):
    return distutils.spawn.find_executable(name) is not None

if not is_tool('brew'):
    print 'Installing Homebrew'
    os.system('/usr/bini/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
else:
    print 'Homebrew installed'

print 'Installing brew cask'
os.system('brew tap caskroom/cask')

if not is_tool('salt'):
    print 'Installing saltstack...'
    os.system('brew install saltstack')
else:
    print 'Saltstack installed'

