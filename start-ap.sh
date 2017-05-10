#! /bin/bash

dev=wlan0

conf_hostapd=./hostapd.conf
conf_dnsmasq=./dnsmasq.conf

killall wpa_supplicant

ifconfig $dev down
ifconfig $dev up

hostapd $conf_hostapd &

sleep 5

ifconfig $dev 10.0.0.1 netmask 255.255.255.0
route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1

dnsmasq -C $conf_dnspmasq $dev

echo '1' > /proc/sys/net/ipv4/ip_forward
iptables --policy INPUT ACCEPT
iptables --policy FORWARD ACCEPT
iptables --policy OUTPUT ACCEPT
iptables -F
iptables -t nat -F
iptables -t nat -A PREROUTING -i $dev -p udp --dport 53 -j DNAT --to 10.0.0.1
