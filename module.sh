echo "Chcking Package..."
sleep 5
bin=$PREFIX/bin
dir=$(pwd)
echo -e "\033[1;97m Updating Packages!"
pkg update && pkg upgrade -y
if [ -e $bin/git ]; then 
  echo -e "\u001b[32mSkip install git but already installed!"
else 
  echo -e "\u001b[31mInstaling \u001b[31mgit!"
  pkg install git -y
  echo -e "\u001b[32mDone install git!"
fi
if [ -e $bin/python ]; then 
  echo -e "\u001b[32mSkip install python but already installed!"
else 
  echo -e "\u001b[31mInstaling \u001b[31mpython!"
  pkg install python -y
  echo -e "\u001b[32mDone install python!"
fi
if [ -e $bin/python2 ]; then 
  echo -e "\u001b[32mSkip install python2 but already installed!"
else 
  echo -e "\u001b[31mInstaling \u001b[31mpython2!"
  pkg install python2 -y
  echo -e "\u001b[32mDone install python2!"
fi
if [ -e $bin/bash ]; then 
  echo -e "\u001b[32mSkip install bash but already installed!"
else 
  echo -e "\u001b[31mInstaling \u001b[31mbash!"
  pkg install bash -y
  echo -e "\u001b[32mDone install bash!"
fi
echo -e "\u001b[32mInstalling pip"
sleep 5
pip install colorama
pip2 install colorama
pip install requests
pip2 install requests
pip install phonenumbers
pip2 install phonenumbers
pip install datetime
pip2 install datetime
pip3 install --upgrade instaloader 
echo -e "\u001b[32mDone installing pip!"
echo -e "Running Tools..."
sleep 5
python owlsint.py
