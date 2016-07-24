#!/usr/bin/env bash -xv
echo "Installing homebrew"
/usr/bini/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew_packages=(wget ag fzf python3 golang neovim vim git jenv mercurial
neovim-dot-app tmate tree rename)
additional_packages=(android-ndk android-sdk asciinema packer)

for i in "${brew_packages[@]}"
do :
   brew install $i
done

for i in "${additional_packages[@]}"
do :
   brew install $i
done
