- [Setup Git Remote](#setup-git-remote)

---

# Setup Git Remote

Run the following commands on the Pi:

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

APP_DIR="home/pi/app"

if [ "$1" == "refs/heads/master" ]; then
    echo "Detected commit to master"
    echo "Updating ${APP_DIR} directory."
    git -C "${APP_DIR}" pull
fi
```

Some things to note:

- This file will need to be executable
- This assumes you want to update `/home/pi/app`. Alter the script if you wish to use another directory.

In order to push to this remote repository, you'll need to add this remote on your development machine:

```sh
git remote add pi pi@submarine:g2x-submarine-v3.git
```

You'll now be able to push to that repository:

```sh
git push pi master
```
