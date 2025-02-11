# YouTube Video Downloader

A Python-based application that allows users to download YouTube videos with a graphical user interface (GUI). The application utilizes `yt_dlp` for downloading videos and requires `ffmpeg` for processing.

## Features

- **Graphical User Interface**: Built with `tkinter` for ease of use.
- **Progress Tracking**: Displays download progress and estimated time remaining.
- **Threaded Downloads**: Ensures the GUI remains responsive during downloads.

## Requirements

- Python 3.x
- `yt_dlp` library
- `ffmpeg` executable

Installation and Troubleshooting Guide
Table of Contents
Installing yt-dlp
Installing ffmpeg
Troubleshooting Common Issues
Installing yt-dlp
yt-dlp is a command-line tool that allows downloading videos from various platforms. Follow the steps below to install it on your system.

For Windows Users
Download the Executable:

Visit the yt-dlp releases page.
Download the latest yt-dlp.exe file.
Place the Executable:

Move the downloaded yt-dlp.exe to a directory of your choice, preferably one that's included in your system's PATH for easy access from the command line.
Verify the Installation:

Open Command Prompt.
Type yt-dlp --version and press Enter.
If installed correctly, it will display the version number of yt-dlp.
For macOS and Linux Users
Using pip:

Open Terminal.
Ensure you have Python and pip installed. If not, install them using your system's package manager.
Run the following command to install yt-dlp:
bash
Copy
Edit
python3 -m pip install -U yt-dlp
This command installs or updates yt-dlp to the latest version.
Verify the Installation:

In Terminal, type yt-dlp --version and press Enter.
The version number of yt-dlp should be displayed if the installation was successful.
For more detailed installation instructions, refer to the yt-dlp Installation Guide.

Installing ffmpeg
ffmpeg is a multimedia framework used by yt-dlp for processing video and audio files. Follow the steps below to install it on your system.

For Windows Users
Download ffmpeg:

Visit the FFmpeg download page.
Choose a suitable build for Windows and download it.
Extract the Files:

Extract the downloaded archive to a directory, e.g., C:\ffmpeg.
Add ffmpeg to System PATH:

Open the Start Menu, search for "Environment Variables," and select "Edit the system environment variables."
In the System Properties window, click on the "Environment Variables" button.
In the Environment Variables window, find the "Path" variable under "System variables," select it, and click "Edit."
Click "New" and add the path to the bin directory inside your ffmpeg folder, e.g., C:\ffmpeg\bin.
Click "OK" to close all windows.
Verify the Installation:

Open Command Prompt.
Type ffmpeg -version and press Enter.
If installed correctly, it will display the version information of ffmpeg.
For a detailed walkthrough, refer to the guide on How to Install FFmpeg on Windows.

For macOS and Linux Users
Using Homebrew (macOS):

Open Terminal.
Run the following commands:
bash
Copy
Edit
brew update
brew install ffmpeg
This will install ffmpeg using Homebrew.
Using Package Manager (Linux):

Open Terminal.
For Debian/Ubuntu-based distributions, run:
bash
Copy
Edit
sudo apt update
sudo apt install ffmpeg
For other distributions, use the appropriate package manager to install ffmpeg.
Verify the Installation:

In Terminal, type ffmpeg -version and press Enter.
The version information of ffmpeg should be displayed if the installation was successful.
Troubleshooting Common Issues
Here are some common issues users might encounter during installation and their solutions:

'yt-dlp' is not recognized as an internal or external command:

Cause: The system cannot find the yt-dlp executable.
Solution: Ensure that yt-dlp is installed correctly and that its directory is added to the system's PATH. Alternatively, navigate to the directory containing yt-dlp.exe in the command line or provide the full path to the executable when running it.
'ffmpeg' is not recognized as an internal or external command:

Cause: The system cannot find the ffmpeg executable.
Solution: Verify that ffmpeg is installed and that the path to its bin directory is added to the system's PATH. Ensure you have applied the changes and restarted your terminal or command prompt.
Permission Denied Errors:

Cause: Insufficient permissions to execute the files.
Solution: Ensure that you have the necessary permissions to execute yt-dlp and ffmpeg. On Unix-based systems, you might need to change the file permissions using chmod. For example:
bash
Copy
Edit
chmod +x /path/to/yt-dlp
chmod +x /path/to/ffmpeg
SSL Certificate Errors:

Cause: Issues with SSL certificates when yt-dlp tries to download videos.
Solution: Update Python and the certifi package. You can do this by running:
bash
Copy
Edit
python3 -m pip install --upgrade certifi
Outdated Versions:

Cause: Using outdated versions of yt-dlp or ffmpeg can lead to compatibility issues.
Solution: Regularly update both tools. For yt-dlp, you can update it using pip:
bash
Copy
Edit
python3 -m pip install -U yt-dlp
For ffmpeg, download the latest version from the official website and replace the old files with the new ones.
Missing Dependencies:

Cause: Certain features of yt-dlp might require additional dependencies.
Solution: Refer to the yt-dlp documentation to identify and install any additional dependencies required for your specific use case.
If you encounter issues not covered here, consider consulting the yt-dlp GitHub Issues page or the FFmpeg documentation for further assistance.
