#!/bin/bash

git pull

cp bash/.bashrc ~/

mkdir /home/$USER/.config/i3/
mkdir /home/$USER/.config/i3status/
cp i3/config /home/$USER/.config/i3/
cp i3status/config /home/$USER/.config/i3status

mkdir /home/$USER/.newsboat/
cp newsboat/urls /home/$USER/.newsboat/

mkdir /home/$USER/.config/rofi/
cp rofi/config /home/$USER/.config/rofi/
