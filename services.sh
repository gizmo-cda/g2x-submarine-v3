#!/usr/bin/env bash

if [ $# != 1 ]; then
    echo "usage: $0 <systemctl-cmd>"
    exit 1
fi

SERVICES=("camera" "enviro" "light")

for service in "${SERVICES[@]}"; do
    echo "sudo systemctl $1 g2x-${service}"
    # sudo systemctl "$1" "g2x-$service"
done
