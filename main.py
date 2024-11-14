from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import messagebox

# Load environment variables from .env file
load_dotenv()


def create_playlist():
    # Get the date from the entry field
    date = date_entry.get()

    # Check if date is provided
    if not date:
        messagebox.showwarning("Input Error", "Please enter a date in the format YYYY-MM-DD.")
        return

    # Scraping Billboard 100
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
    billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
    response = requests.get(url=billboard_url, headers=header)

    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]

    # Spotify Authentication
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="https://example.com/callback/",
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            show_dialog=True,
            cache_path="token.txt"
        )
    )

    # Retrieve the current user ID
    user_id = sp.current_user()["id"]

    # Searching Spotify for songs by title
    song_uris = []
    year = date.split("-")[0]
    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    # Creating a new private playlist in Spotify
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

    # Adding songs found to the new playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

    # Display the playlist creation success message
    output_text.set(f"Playlist '{playlist['name']}' created successfully!\nAdded {len(song_uris)} songs.")


# Set up the Tkinter GUI
root = tk.Tk()
root.title("Time Travel Playlist Creator")
root.geometry("400x300")

# Date entry label and entry field
tk.Label(root, text="Enter date (YYYY-MM-DD):").pack(pady=10)
date_entry = tk.Entry(root, width=20)
date_entry.pack()

# Button to create playlist
create_button = tk.Button(root, text="Create Playlist", command=create_playlist)
create_button.pack(pady=20)

# Output message area
output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, wraplength=350, justify="left")
output_label.pack(pady=10)

# Run the GUI event loop
root.mainloop()
