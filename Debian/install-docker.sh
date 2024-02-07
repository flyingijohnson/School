#!/bin/bash

# This is Docker install
# https://www.linuxtech1.com/install-docker-engine-on-debian/
# This is for Debian
# IJ 2/7/2024

# not complete, look at class recording
sudo apt update
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release -y


# this is in addition to docker documentation
sudo docker version
sudo systemctl start docker
sudo systemctl enable docker
sudo suermod -aG docker preuss
