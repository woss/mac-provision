# mac-provision

sudo salt-call --log-file=salt_log.log --local -c salt saltutil.sync_all
sudo salt-call --log-file=salt_log.log --local -c salt state.apply test=True
sudo salt-call --id=minion.yaml --file-root=./ --pillar-root=./salt/pillar --states-dir=./salt/states --log-level=debug --log-file=salt_log.log --local -c salt state.apply test=True

# What's included

System packages:

* nvm
* rvm
* jenv
* wget
* ag
* fzf
* python3
* golang
* neovim
* git
* mercurial
* tmate
* tree
* rename
* watch


Dev packages:

* Neovim (neovim-dot-app)
* 


when installing brew should be installed in `~/brew`  dir

http://www.hammerspoon.org/
