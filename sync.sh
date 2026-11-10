#!/bin/bash

name=aglaea
host=192.168.2.201

rsync_opts=${1:-""}  # 默认空，可传入任意 rsync 参数

echo "revoke sync installation release process @$(date)"

eval rsync -avrt -P $rsync_opts --delete --exclude="sync.sh" --exclude=".git/" "/share/bang" "$name@$host:/data/vseeker"