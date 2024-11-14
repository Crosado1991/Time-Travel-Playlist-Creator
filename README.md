# Time Travel Playlist Creator

A Python application that generates a Spotify playlist with the top Billboard 100 songs from a specified date. Using this tool, you can "time travel" to any date in the past and create a Spotify playlist with the most popular songs from that day.

## Features

- **Web Scraping**: Uses BeautifulSoup to scrape the Billboard 100 chart for the specified date.
- **Spotify Integration**: Automatically creates a private playlist on the user's Spotify account with the top Billboard songs from that date.
- **Interactive GUI**: A Tkinter-based graphical user interface allows the user to input a date and see the success message for playlist creation.

## Prerequisites

- Python 3.x
- Spotify Developer Account (for client credentials)

## Libraries Used

- `requests`: To make HTTP requests to the Billboard website.
- `BeautifulSoup`: For parsing HTML and extracting song information.
- `spotipy`: Spotify's Web API for creating playlists and adding songs.
- `dotenv`: For securely loading environment variables.
- `tkinter`: For creating the graphical user interface.

## Setup

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/TimeTravel_Playlist_Creator.git
    cd TimeTravel_Playlist_Creator
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up a Spotify Developer account at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/). Create a new app to get the **Client ID** and **Client Secret**.

4. Create a `.env` file in the project directory to store your Spotify API credentials. Replace `YOUR-CLIENT-ID` and `YOUR-CLIENT-SECRET` with your actual Spotify credentials:

    ```env
    CLIENT_ID=YOUR-CLIENT-ID
    CLIENT_SECRET=YOUR-CLIENT-SECRET
    ```

5. Make sure the **Redirect URI** in your Spotify app settings matches the one used in the script (e.g., `https://example.com/callback/`).

## Usage

1. Run the program:

    ```bash
    python main.py
    ```

2. A graphical window will open with an input field. Enter the desired date in the format `YYYY-MM-DD` and click **Create Playlist**.

3. The program will:
   - Scrape the top 100 Billboard songs for the given date.
   - Authenticate with your Spotify account.
   - Create a private playlist on your Spotify account with the songs from the specified date.
   
4. A message will display confirming that the playlist has been created, along with the number of songs added.

## Example

```text
Enter date (YYYY-MM-DD): 1985-07-13
