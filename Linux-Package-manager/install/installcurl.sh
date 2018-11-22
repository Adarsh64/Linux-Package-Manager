echo "Hello" $USER
tar -xvf Packages/curl/curl-7.62.0.tar.gz
cd curl-7.62.0
./configure

#making install
make
sudo make install
curl --version
