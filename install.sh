clear
chmod +x main.py
printf "Exec=$HOME/.appinstaller-assistant/main.py" >> appinstaller-assistant.desktop
echo -e "\033[36mWelcome to the AppInstaller Assistant installer. This will install AppInstaller Assistant on your GNU/Linux machine.\033[0m" 
echo "This installer will install, update or modify the following:"
echo " - INSTALL/UPDATE: python3, pip3 (if not already installed)"
echo " - INSTALL/UPDATE: guizero (through pip3, if not already installed)"
echo " - INSTALL: AppInstaller Assistant and required assets"
echo " - MODIFY: an .appinstaller-assistant directory will be created in your home directory"
echo " - MODIFY: A desktop shortcut to AppInstaller Assistant will be installed in /usr/share/applications"
echo "Are you sure you want to continue? (y/n)"
read answer
if [ "$answer" != "y" ]; then
    echo "The installation wil be aborted. Remove the installation files? (~/appinstaller-assistant) (y/n)"
    read answer1
    if [ "$answer1" != "y" ]; then
        echo "The installation has been aborted, but files have been preserved."
        exit
    fi
    echo "Removing..."
    rm -rf ../appinstaller-assistant
    echo "Files have been removed, and the installation has been aborted."
    exit
fi
command -v apt >/dev/null || error "\033[31mYou are not running Debian or a deriatve of it. This installer is for Debian based systems.\033[0m"
clear
echo -e "\033[34m⬇ Downloading or Updating python3...\033[0m"
sudo apt install python3
echo -e "\033[32m😀 python3 has been installed or updated! Continuing...\033[0m"
echo -e "\033[34m⬇ Downloading or Updating guizero...\033[0m"
pip3 install guizero
echo -e "\033[32m😀 guizero has been installed or updated! Continuing...\033[0m"
echo -e "\033[34m↔ Installing program files and assets...\033[0m"
chmod +x main.py
mkdir ~/.appinstaller-assistant
cp main.py ~/.appinstaller-assistant/main.py
cp parcel.png ~/.appinstaller-assistant/parcel.png
sudo cp appinstaller-assistant.desktop /usr/share/applications/appinstaller-assistant.desktop
echo -e "\033[32m😀 Program files have been installed! Continuing...\033[0m"
echo -e "\033[32m😀 You can now run AppInstaller Assistant by selecting 'AppInstaller Assistant' in the menu. You may have to reboot to see it.\033[0m"
echo -e "\033[32m🙏 Thank you for installing AppInstaller Assistant! Would you like to remove the installation files? (~/appinstaller-assistant) (y/n)\033[0m"
read answer1
    if [ "$answer1" != "y" ]; then
        echo "The installation has been completed, and installation files have been preserved."
        exit
    fi
echo "Removing installation files..."
rm -rf ../appinstaller-assistant
echo "The installation files have been removed. Bye!"
