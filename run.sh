# Mise à jour
sudo apt update
sudo apt --yes upgrade
sudo apt --yes dist-upgrade

# Dépendances
sudo apt install -y git python3 python3-dev python-dev python3-pip sox build-essential portaudio19-dev flac

sudo pip3 install SpeechRecognition
sudo pip3 install pyaudio

git clone https://github.com/MiloProject/snowboy

cd snowboy/swig/python
make
