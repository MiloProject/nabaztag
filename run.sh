# Mise à jour
sudo apt update
sudo apt --yes upgrade
sudo apt --yes dist-upgrade

# Dépendances
sudo apt install -y git python3 python3-dev python-dev python3-pip sox build-essential portaudio19-dev flac hostapd dnsmasq

sudo pip3 install SpeechRecognition
sudo pip3 install pyaudio

# Désactive les services inutiles
sudo systemctl disable hostapd
sudo systemctl disable dnsmasq
