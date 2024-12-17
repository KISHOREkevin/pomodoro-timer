#!/usr/bin/env bash

mkdir -p $HOME/.local/bin/
mkdir -p $HOME/.local/lib/pomodoro/
mkdir -p $HOME/.local/share/pomodoro/music/
mkdir -p $HOME/.local/share/applications/

cp ./index.py $HOME/.local/lib/pomodoro/
cp ./requirements.txt $HOME/.local/lib/pomodoro/
cp ./music/notify.wav $HOME/.local/share/pomodoro/music/
cp ./pomodoro.desktop $HOME/.local/share/applications
cp ./pomodoro $HOME/.local/bin/

cd $HOME/.local/lib/pomodoro/

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cd $HOME 

exit 0

