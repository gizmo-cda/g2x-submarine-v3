- [Setup Pi as Access Point](#setup-pi-as-access-point)

---

# Setup Pi as Access Point

[Tutorial](https://thepi.io/how-to-use-your-raspberry-pi-as-a-wireless-access-point/)

Note that I ignored the commands for routing traffic to eth0. I did the following:

- Commented out `bridge=br0` in hostapd.conf
- Skipped `Step 6: Set up traffic forwarding`
- Skipped `Step 7: Add a new iptables rule`
- Skipped `Step 8: Enable internet connection`

Note that hostapd was not running for me because it was "masked". I found this series of commands to unmask and start the service

```bash
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
```
