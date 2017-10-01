#!/bin/bash

set -e

BRANCH="offline-build"
REMOTE="https://$GITHUB_API_KEY@github.com/CoderDojoPotsdam/intro.git"

if ! [ -n "$GITHUB_API_KEY" ]; then
  echo "You should set the variable GITHUB_API_KEY to contain an api key with push access to this repository. It should have the form \"USERNAME:API_KEY\" See https://stackoverflow.com/a/33125422/1320237"
  exit 1
fi
if ! [ -n "$OFFLINE_BUILD_FOLDER" ]; then
  echo "You should set the variable OFFLINE_BUILD_FOLDER to contain the built version of the offline tutorial."
  exit 1
fi

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
  git push -f -q "$REMOTE-$BRANCH" "$BRANCH"
  rm -rf .git
)
