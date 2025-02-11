import yt_dlp
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
import threading
import os
import sys

# Locate ffmpeg.exe inside the same directory as the EXE
def get_ffmpeg_path():
    if getattr(sys, 'frozen', False):  # Running as an EXE
        return os.path.join(sys._MEIPASS, "ffmpeg.exe")
    return os.path.join(os.getcwd(), "ffmpeg.exe")

FFMPEG_PATH = get_ffmpeg_path()

def download_video(url, save_path="C:/Users/tchpo/Videos"):
    # Hide the URL input and download button when starting the download
    url_label.grid_forget()
    url_entry.grid_forget()
    download_button.grid_forget()

    # Show the extracting message and progress bar right after the download starts
    extracting_label.grid(row=0, column=0, padx=10, pady=10)
    progress_label.grid(row=2, column=0, padx=10, pady=5, sticky="ew")  # Directly above the progress bar
    progress_bar.grid(row=3, column=0, padx=20, pady=10, columnspan=2, sticky="ew")
    eta_label.grid(row=4, column=1, padx=10, pady=10)
    cancel_button.grid(row=4, column=0, padx=10, pady=10)

    download_complete = False  # Flag to track if download is complete

    # Thread for the download process so it doesn't block the UI
    def start_download():
        def progress_hook(d):
            nonlocal download_complete

            if d['status'] == 'downloading':
                if 'total_bytes' in d and d['total_bytes'] > 0:
                    percent = d['downloaded_bytes'] / d['total_bytes'] * 100
                    progress_bar["value"] = percent
                    progress_label.config(text=f"{percent:.2f}%")

                    # Calculate the download speed and ETA
                    if 'downloaded_bytes' in d and 'elapsed' in d:
                        downloaded_bytes = d['downloaded_bytes']
                        elapsed_time = d['elapsed']
                        download_speed = downloaded_bytes / elapsed_time  # bytes per second
                        remaining_bytes = d['total_bytes'] - downloaded_bytes
                        eta_seconds = remaining_bytes / download_speed if download_speed > 0 else 0
                        eta_minutes = eta_seconds // 60
                        eta_seconds = eta_seconds % 60
                        eta_label.config(text=f"ETA: {int(eta_minutes)}m {int(eta_seconds)}s")
                    else:
                        eta_label.config(text="ETA: Calculating...")
                else:
                    # If total_bytes is not available, just update based on downloaded bytes
                    progress_bar["value"] = d['downloaded_bytes'] / 1000000  # Rough progress estimation
                    progress_label.config(text=f"{progress_bar['value']:.2f}%")
                
                root.after(0, root.update_idletasks)

            elif d['status'] == 'finished' and not download_complete:
                download_complete = True  # Set the flag to True when download finishes
                messagebox.showinfo("Success", f"Download Complete! Video saved to: {save_path}")
                progress_bar.grid_forget()
                progress_label.grid_forget()
                eta_label.grid_forget()
                extracting_label.grid_forget()
                download_complete_label.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

                # Once finished, show the "Return" button
                return_button.grid(row=4, column=0, padx=10, pady=10)
                cancel_button.grid_forget()

                root.after(0, root.update_idletasks)

            elif d['status'] == 'error':
                messagebox.showerror("Error", "An error occurred during download.")
                progress_bar["value"] = 0
                root.after(0, root.update_idletasks)

        ydl_opts = {
            "format": "bestvideo+bestaudio",
            "outtmpl": f"{save_path}/%(title)s.%(ext)s",
            "progress_hooks": [progress_hook],
            "ffmpeg_location": FFMPEG_PATH  # Use the bundled FFmpeg
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            progress_bar["value"] = 0
            extracting_label.grid_forget()
            root.after(0, root.update_idletasks)

    # Run the download in a separate thread to keep the UI responsive
    threading.Thread(target=start_download, daemon=True).start()

def on_download_button_click():
    url = url_entry.get()
    if url:
        download_video(url)
    else:
        messagebox.showwarning("Input Error", "Please enter a URL.")

def cancel_download():
    # Instead of quitting the app, return to the initial state
    return_to_initial()

def return_to_initial():
    # Reset the interface to the initial state after download
    download_complete_label.grid_forget()  # Hide the "Download Complete" label
    return_button.grid_forget()  # Hide the return button
    url_label.grid(row=0, column=0, padx=10, pady=10)  # Show the URL label
    url_entry.grid(row=1, column=0, padx=10, pady=5)  # Show the URL entry
    download_button.grid(row=2, column=0, padx=20, pady=10, columnspan=2)  # Show the download button

root = tk.Tk()
root.title("YouTube Video Downloader")

# URL input
url_label = tk.Label(root, text="Enter YouTube Video URL:")
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=1, column=0, padx=10, pady=5)

download_button = tk.Button(root, text="Download Video", command=on_download_button_click)
download_button.grid(row=2, column=0, padx=20, pady=10, columnspan=2)

# Progress bar
progress_bar = Progressbar(root, orient="horizontal", length=300, mode="determinate")

# Progress label to display percentage
progress_label = tk.Label(root, text="0.00%", font=("Helvetica", 10))

# ETA label to display the estimated time remaining
eta_label = tk.Label(root, text="ETA: Calculating...", font=("Helvetica", 10))

# Cancel button
cancel_button = tk.Button(root, text="Cancel", command=cancel_download)

# Return button after download
return_button = tk.Button(root, text="Return", command=return_to_initial)

# Downloading label (will appear during download)
downloading_label = tk.Label(root, text="Downloading...", font=("Helvetica", 12, "bold"))

# "Download Complete" label
download_complete_label = tk.Label(root, text="Download Complete!", font=("Helvetica", 12, "bold"))

# Credits
credits_label = tk.Label(root, text="Made by Soulz", font=("Helvetica", 6), anchor="e")
credits_label.grid(row=5, column=0, padx=10, pady=10, columnspan=2, sticky="se")

# Label for extracting URL message
extracting_label = tk.Label(root, text="Extracting URL...", font=("Helvetica", 12, "bold"))

root.mainloop()
