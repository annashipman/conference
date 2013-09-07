#!/bin/sh
export DEBIAN_FRONTEND=noninteractive
apt-get update > /dev/null
apt-get -y install postgresql
