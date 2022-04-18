# AppInstaller Assistant
AppInstaller Assistant is a simple utility to create Linux desktop shortcut files to be placed in the DE's menu. It is written in Python 3, and uses the guizero library to render the graphical interface, and the os library to run scripts. It takes you through four steps in total, prompting you to enter necessary information.

## Installation
To install AppInstaller Assistant:

### NEW! Quick, one-command installtion (not heavily tested, fall back to long installtion if it fails):

```bash
curl -L https://tinyurl.com/AppInstallerCURL | bash; ./install.sh
```
###### Note: Because of the redirect, the -L (A.K.A. --location) flag allows CURL to accept HTTP redirects. 

### Long Installation

1. Clone the repository
```bash
git clone https://github.com/Captain-Toad/appinstaller-assistant/
```
2. Go to the new directory
```bash
cd appinstaller-assistant
```
3. Make the installer executable
```bash
chmod +x install.sh
```
4. Run the installer!
```bash
./install.sh
```

If you only want to enter one command, simply run this:
```bash
git clone https://github.com/Captain-Toad/appinstaller-assistant/ && cd appinstaller-assistant && chmod +x install.sh && ./install.sh
```
