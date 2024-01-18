# Live Wallpaper Setup for Parrot OS

This guide provides detailed instructions on setting up a live wallpaper on Parrot OS using `xwinwrap` and `mpv`. It also includes scripts for easily changing the live wallpaper.

## Prerequisites

Ensure you have Parrot OS installed and have a basic understanding of the command line.

## Installation

### 1. Install Dependencies

Open a terminal and execute the following command to install the necessary dependencies:

```

sudo apt-get install build-essential libx11-dev libxrender-dev libxext-dev libxtst-dev libglib2.0-dev libpango1.0-dev libgif-dev git

```

### 2. Install xwinwrap

Clone the `xwinwrap` repository, compile the source code, and install the binary:

```

git clone https://github.com/ujjwal96/xwinwrap.git
cd xwinwrap
make
sudo cp xwinwrap /usr/local/bin/

```

### 3. Configure Desktop Environment

Disable desktop icons for better compatibility with MATE or similar environments:

1. Go to **Preferences** > **Look and Feel** > **MATE Tweak**.
2. Disable **Show Desktop Icons** in the **Desktop** section.

## Scripts

### livebackground.sh

This script is used to set the live wallpaper.

- Ensure you have made the script executable:


```

chmod +x /path/to/livebackground.sh

```

### changelivebackground.py

This Python script changes the live wallpaper dynamically.

- Usage:

```

python3 /path/to/changelivebackground.py /path/to/new/wallpaper.mp4

```

- Ensure you have made the script executable:

```

chmod +x /path/to/changelivebackground.py

```

## Setting up Auto-start

Add `livebackground.sh` to your startup applications to ensure your live wallpaper starts automatically upon login.

- For GNOME, MATE, and similar:

1. Go to **System** > **Preferences** > **Personal** > **Startup Applications**.
2. Click **Add** and input the following details:
   - **Name:** Live Wallpaper
   - **Command:** `/path/to/livebackground.sh`
   - **Delay:** (Optional) Set a delay like 25 seconds for smoother startup.
3. Click **Add** and close the window.

Your live wallpaper should now start automatically when you log in, and you can use `changelivebackground.py` to change it whenever you like.

Organizing Your Live Wallpapers
It's a good practice to keep all your live wallpapers organized in a single folder. This makes managing and changing your wallpapers easier.

## Finding Cool Live Wallpapers

If you're looking for new and cool live wallpapers, here are some resources where you can find a variety of options:

- **[WallpaperFusion](https://www.wallpaperfusion.com/)**: A great place for high-quality images of all kinds.
- **[Unsplash](https://unsplash.com/)**: Home to a vast collection of free-to-use, high-resolution photographs.
- **[Pexels](https://www.pexels.com/)**: Offers free stock photos and videos shared by talented creators.
- **[Giphy](https://giphy.com/)**: If you're looking for something more dynamic, Giphy offers a wide range of animated GIFs that can potentially be converted to live wallpapers.

Remember to respect the copyright and usage rights of the wallpapers you download and use.
