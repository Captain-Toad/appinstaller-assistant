#!/usr/bin/env python3


#import modules
import os
import guizero
import sys
import time

#clear the terminal :)
os.system("clear")

#define funcs - one for the next step, one for the previous step

def nxstep():
	global stepcounter
	try:
		stepcounter
	except NameError:
		stepcounter = 1
	if stepcounter == 1:
		if namebox.value == "":
			print("Input error: 'namebox.value' cannot be blank.")
			guizero.warn("Input error", "Please give your app a name.")
			return
		appname = namebox.value
		prevbutton.enable()
		print("The name of the application has been registered as: " + appname)
		appnameb.hide()
		pathnameb.show()
		stepcounter = stepcounter + 1
		return
	if stepcounter == 2:
		if pathbox.value == "":
			print("Input error: 'pathbox.value' cannot be blank.")
			guizero.warn("Input error", "You cannot leave the path blank.")
			return
		pathname = pathbox.value
		print("The path of the application has been registered as: " + pathname)
		pathnameb.hide()
		iconnameb.show()
		stepcounter = stepcounter + 1
		return
	if stepcounter == 3:
		if iconbox.value == "":
			print("Warning: 'pathbox.value' is blank, your app will have no icon.")
			guizero.warn("Warning", "You do not have an icon identifier entered - your app will have no icon.")
		iconname = iconbox.value
		print("The application icon has been registered as: " + iconname)
		iconnameb.hide()
		nextbutton.hide()
		donebutton.show()
		versionnameb.show()
		stepcounter = stepcounter + 1
		return
	if stepcounter == 4:
		if versionbox.value == "":
			print("Input error: 'versionbox.value' cannot be blank.")
			guizero.warn("Input error", "You cannot leave the version blank.")
			return
		versionname = versionbox.value
		print("The version of the application icon has been registered as: " + versionname)
		versionnameb.hide()
		prevbutton.hide()
		loadtext.show()
		os.system("printf '[Desktop Entry]\nEncoding=UTF-8\nVersion=" + versionbox.value + "\nType=Application\nTerminal=false\nExec=" + pathbox.value + "\nName=" + namebox.value + "\nIcon=" + iconbox.value + "' > ~/.appinstaller-assistant/" + namebox.value +".desktop; echo $(zenity --password --title='Copy files to write-protected directories') | sudo -S mv ~/.appinstaller-assistant/" + namebox.value + ".desktop /usr/share/applications")
		loadtext.hide()
		finishtext.show()
		stepcounter = stepcounter + 1
	if stepcounter == 5:
		sys.exit("The program finished running.")

def prevstep():
	global stepcounter
	try:
		stepcounter
	except NameError:
		stepcounter = 1
		print("If you see this message, an error has occured which caused the program to enter a NameError exception that should theoretiacally not be possible. Please open an issue on GitHub (https://github.com/Captain-Toad/appinstaller-assistant). The program will now be terminated...")
		sys.exit("Done.")
	if stepcounter == 2:
		pathnameb.hide()
		appnameb.show()
		stepcounter = stepcounter - 1
		return
	if stepcounter == 3:
		iconnameb.hide()
		pathnameb.show()
		stepcounter = stepcounter - 1
		return
	if stepcounter == 4:
		versionnameb.hide()
		iconnameb.show()
		stepcounter = stepcounter - 1
		return

#define window contents

#title
app = guizero.App(title="AppInstaller Assistant", width=580, height=335)
padding1 = guizero.Text(app, text=" ", size=12)
titleimg = guizero.Picture(app, image="parcel.png")
padding2 = guizero.Text(app, text=" ", size=7)
title = guizero.Text(app, text="AppInstaller Assistant", size=24, font="Ubuntu")
subtitle = guizero.Text(app, text="a guided .desktop file installer", size=12, font="Ubuntu")

padding3 = guizero.Text(app, text=" ", size=14)

#input box groups
appnameb = guizero.Box(app, layout="grid")
pathnameb = guizero.Box(app, layout="grid", visible=False)
iconnameb = guizero.Box(app, layout="grid", visible=False)
versionnameb = guizero.Box(app, layout="grid", visible=False)

#input instructions
nameinstruc = guizero.Text(appnameb, grid=[1,0], text="  Please enter the name of your app.  ", font="Ubuntu")
pathinstruc = guizero.Text(pathnameb, grid=[1,0], text="  Please enter the file path to your app.  ", font="Ubuntu")
iconinstruc = guizero.Text(iconnameb, grid=[1,0], text="  Please enter a system icon identifier.  ", font="Ubuntu")
versioninstruc = guizero.Text(versionnameb, grid=[1,0], text="  Please enter the version (e.g 1.0)  ", font="Ubuntu")

#input text boxes
namebox = guizero.TextBox(appnameb, grid=[3,0],  width="fill")
pathbox = guizero.TextBox(pathnameb, grid=[3,0], width="fill")
iconbox = guizero.TextBox(iconnameb, grid=[3,0], width="fill")
versionbox = guizero.TextBox(versionnameb, grid=[3,0], width="fill")
#Loading/finish text
loadtext = guizero.Text(app, text="Cooking, frying and boiling your file...", font="Ubuntu", visible=False)
finishtext = guizero.Text(app, text="Done! You may have to log in and out to see your app in the menu.", visible=False, font="Ubuntu")
padding4 = guizero.Text(app, text=" ", size=14)

#next/prev buttons, call functions
buttonbox = guizero.Box(app, layout="grid")
prevbutton = guizero.PushButton(buttonbox, text="🠴", enabled=False, grid=[1,0], command=prevstep)


padding5 = guizero.Text(buttonbox, text=" ", size=5, grid=[2,0])

donebutton = guizero.PushButton(buttonbox, text="✔", visible=False, grid=[3,0], command=nxstep)
nextbutton = guizero.PushButton(buttonbox, text="🠶", command=nxstep, grid=[3,0])



#render the app
app.display()

