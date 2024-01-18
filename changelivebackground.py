#!/usr/bin/env python3
import sys
import subprocess

def change_wallpaper(new_wallpaper):
    script_path = '/home/golden/downloads/LiveBackground/livebackground.sh'  # Absolute path to the script
    
    # Kill any existing xwinwrap and mpv processes
    subprocess.run(["pkill", "xwinwrap"], stdout=subprocess.PIPE)
    subprocess.run(["pkill", "mpv"], stdout=subprocess.PIPE)
    
    # Allow a moment for the processes to be properly terminated
    subprocess.run(["sleep", "2"])
    
    # Write the new wallpaper command to the livewallpaper.sh script
    with open(script_path, 'w') as file:
        file.write("#!/bin/bash\n")
        file.write("xwinwrap -ov -g 1920x1080 -- mpv -wid WID --loop --no-audio ")
        file.write(new_wallpaper)
        file.write(" --no-stop-screensaver --panscan=1.0 --no-osc --no-osd-bar --no-input-default-bindings")
    
    # Start the new wallpaper
    subprocess.Popen(script_path)  # Use the absolute path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        change_wallpaper(sys.argv[1])
    else:
        print("Usage: changelivebackground.py /path/to/new/livebackground.mp4")

