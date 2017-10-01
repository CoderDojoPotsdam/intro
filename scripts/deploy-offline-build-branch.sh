#!/bin/bash

set -e

BRANCH="offline-build"

if ! [ -n "$id_rsa" ]; then
  echo "You should set the variable id_rsa to contain a valid ssh deploy key to origin."
  exit 1
fi
if ! [ -n "$OFFLINE_BUILD_FOLDER" ]; then
  echo "You should set the variable OFFLINE_BUILD_FOLDER to contain the built version of the offline tutorial."
  exit 1
fi

mkdir -p ~/.ssh
echo "$id_rsa" > ~/.ssh/id_rsa

echo "Create a temporary folder for checking out $BRANCH."
mkdir -p temp
cp -r .git temp
(
  set -e
  cd temp
  git fetch origin "+$BRANCH:$BRANCH"
  git checkout "$BRANCH"
)
mv temp/.git "$OFFLINE_BUILD_FOLDER"
rm -r temp

(
  set -e
  cd "$OFFLINE_BUILD_FOLDER"
  echo "Commit offline version into branch \"$BRANCH\""
  git add --all .
  git commit -am"Automated build $TRAVIS_BUILD_NUMBER"
  git push --set-upstream origin "$BRANCH"
  rm -r .git
)
