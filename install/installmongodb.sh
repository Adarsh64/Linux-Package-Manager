echo "Hello" $USER
tar -zxvf ../mongodb-linux-arm64-ubuntu1604-4.0.4.tgz
sudo echo "export PATH=/home/$USER/Desktop/Packages/mongodb/mongodb-linux-arm64-ubuntu1604-4.0.4/bin:$PATH" >> ~/.bashrc

#creating data and log directories\
sudo mkdir -p /data/db
sudo mkdir -p /var/log/mongodb
sudo mongod --dbpath /data/db --logpath /var/log/mongodb/mongod.log --fork
mongo
