- [Setup Static IP Fallback](#setup-static-ip-fallback)
- [Setup Git Remote](#setup-git-remote)
- [Setup Pimoroni](#setup-pimoroni)
- [Setup Service](#setup-service)

---

# Setup Static IP Fallback

Edit `/etc/dhcpcd.conf` and add the following text to the end of the file:

```
interface eth0
fallback static_eth0

profile static_eth0
static ip_address=192.168.0.1/24
```

# Setup Git Remote

Run the following commands on the Pi to create the git remote directory:

```sh
cd
mkdir g2x-submarine-v3.git
cd g2x-submarine-v3.git
git init --bare
```

In order to update the application directory on the Pi each time a commit to master is pushed to it, create the following script at `/home/pi/g2x-submarine-v3.git/hooks/post-update:

```sh
#!/usr/bin/env bash

unset GIT_DIR

APP_DIR="/home/pi/app"
BRANCH="master"

if [ "$1" == "refs/heads/${BRANCH}" ]; then
    echo "Detected commit to ${BRANCH}"
    echo "Updating ${APP_DIR} directory."
    git -C "${APP_DIR}" pull
fi
```

Some things to note:

- This file needs to be executable
- This assumes you want to update `/home/pi/app`. Alter the `APP_DIR` variable in the script if you wish to use another directory.

In order to push to this remote repository, you'll need to add the remote to your development machine:

```sh
git remote add pi pi@submarine:g2x-submarine-v3.git
```

You'll now be able to push to that repository:

```sh
git push pi master
```

# Setup Pimoroni

- [Enviro Phat Getting Started](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat)

```bash
curl https://get.pimoroni.com/envirophat | bash
```

# Setup Service

Run the following to initialize the service and make it start automatically when the system boots:

```bash
sudo cp g2x-camera.service /etc/systemd/system
sudo systemctl enable g2x-camera
```

You can start/stop/restart the service using the following commands:

```bash
sudo systemctl start g2x-camera
sudo systemctl stop g2x-camera
sudo systemctl restart g2x-camera
```

If you make changes to the service file, you will need to reload the service daemon and restart the service

```bash
sudo systemctl daemon-reload
sudo systemctl restart g2x-camera
```

You can check the status of your service:

```bash
systemctl status g2x-camera
```
