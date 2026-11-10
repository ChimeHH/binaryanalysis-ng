#!/usr/bin/env bash
set -euo pipefail
PS4='+ '
set -x

user_id="$(id -u)"
group_id="$(id -g)"

sudo mkdir -p \
  /data/logs \
  /data/bin/cpp \
  /data/bin/cpp/plugin \
  /data/ide-shm \
  /data/bin/sdk/cpp/lib \
  /data/bin/sdk/cs/lib \
  /data/bin/cs/plugin

if mountpoint -q /data/ide-shm; then
  sudo mount -o remount,size=4g,mode=1777 /data/ide-shm
else
  sudo mount -t tmpfs -o size=4g,mode=1777 tmpfs /data/ide-shm
fi

sudo chown -R "$user_id:$group_id" \
  /data/logs \
  /data/bin/cpp \
  /data/bin/sdk \
  /data/bin/cs

sudo chmod -R u+rwX \
  /data/logs \
  /data/bin/cpp \
  /data/bin/sdk \
  /data/bin/cs

stat -c '%A %U:%G %n' \
  /data/logs \
  /data/bin/cpp \
  /data/bin/sdk \
  /data/bin/cs
