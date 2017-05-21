#! /bin/bash

dev=wlan0

# Préconfiguré pour le RPI
conf_hostapd=/home/pi/nabaztag/hostapd.conf
conf_dnsmasq=/home/pi/nabaztag/dnsmasq.conf

killall wpa_supplicant
killall hostapd
killall dnsmasq

ifconfig $dev down
ifconfig $dev up

hostapd $conf_hostapd &

sleep 5

ifconfig $dev 10.0.0.1 netmask 255.255.255.0
route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1

dnsmasq -C $conf_dnsmasq

echo '1' > /proc/sys/net/ipv4/ip_forward
iptables --policy INPUT ACCEPT
iptables --policy FORWARD ACCEPT
iptables --policy OUTPUT ACCEPT
iptables -F
iptables -t nat -F
iptables -t nat -A PREROUTING -i $dev -p udp --dport 53 -j DNAT --to 10.0.0.1
