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

# if not is_tool('salt'):
    # print 'Installing saltstack...'
    # os.system('brew ins,otall saltstack')
# else:
    # print 'Saltstack installed'

# os.system('sudo salt-call --log-file=salt_log.log --local -c salt saltutil.sync_all')
# os.system('sudo salt-call --log-file=salt_log.log --local -c salt state.apply test=True')
# os.system('sudo salt-call --id=minion.yaml --file-root=./ --pillar-root=./salt/pillar --states-dir=./salt/states --log-level=debug --log-file=salt_log.log --local -c salt state.apply test=True')

print 'Installing bunch of stuff'

# Add the following to ~/.zshrc or your desired shell
# configuration file:

#   export NVM_DIR="$HOME/.nvm"
#   . "$(brew --prefix nvm)/nvm.sh"



os.system('brew install wget ag fzf python3 golang neovim vim nvm git')

