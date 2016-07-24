#!/usr/bin/env bash

git clone https://github.com/creationix/nvm.git ~/.nvm && cd ~/.nvm && git checkout `git describe --abbrev=0 --tags`

nvm_nodejs_versions=(0.10 0.12 4 5 6)
nvm_default_version=5
npms=(babel bower cordova electron ios-deploy nodemon, webpack typescript
gulp live-server reactive-native-cli eslint grunt http-server browserify
jshint)
for i in "${nvm_nodejs_versions[@]}"
do :
   nvm install $i
done

source ~/.zshrc

for i in "${npms[@]}"
do :
   npm install $i
done
