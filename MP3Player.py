import random

class MP3Playlist:
    def __init__(self):
        self.tracks = []  # Initialize an empty list to store tracks
        self.durations = {}  # Dictionary to store track durations

    def load_playlist(self, filename):
        """Load a playlist from a text file."""
        try:
            with open(filename, 'r') as file:
                for line in file:
                    track = line.strip()
                    if track:  # Ensure the line is not empty
                        self.enqueue(track)
            print(f"Loaded playlist from {filename}.")
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")

    def display_tracks(self):
        """Display all tracks in the playlist."""
        if not self.tracks:
            print("The playlist is empty.")
        else:
            print("Current Playlist:")
            for index, track in enumerate(self.tracks, start=1):
                print(f"{index}. {track} (Duration: {self.durations.get(track, 'N/A')} seconds)")

    def enqueue(self, track, duration=None):
        """Add an MP3 track to the end of the playlist."""
        self.tracks.append(track)
        if duration is not None:
            self.durations[track] = duration  # Store the duration if provided
        print(f"Added track: {track}")

    def remove_track(self, track):
        """Remove an MP3 track from the playlist."""
        if track in self.tracks:
            self.tracks.remove(track)
            self.durations.pop(track, None)  # Remove duration if it exists
            print(f"Removed track: {track}")
        else:
            print(f"Track not found: {track}")

    def save_playlist(self, filename):
        """Save the current playlist to a text file."""
        with open(filename, 'w') as file:
            for track in self.tracks:
                file.write(track + '\n')
        print(f"Playlist saved to {filename}.")

    def shuffle_playlist(self):
        """Shuffle all the songs in the playlist."""
        random.shuffle(self.tracks)
        print("Playlist shuffled.")

    def count_tracks(self):
        """Count the number of tracks in the playlist."""
        count = len(self.tracks)
        print(f"Number of tracks in the playlist: {count}")
        return count

    def total_duration(self):
        """Calculate the total duration of the playlist."""
        total = sum(self.durations.get(track, 0) for track in self.tracks)
        print(f"Total duration of the playlist: {total} seconds")
        return total

    def clear_playlist(self):
        """Clear/reset the playlist."""
        self.tracks.clear()
        self.durations.clear()
        print("Playlist cleared.")

    def is_empty(self):
        """Check if the playlist is empty."""
        empty = len(self.tracks) == 0
        if empty:
            print("The playlist is empty.")
        else:
            print("The playlist is not empty.")
        return empty

# Example usage
if __name__ == "__main__":
    playlist = MP3Playlist()
    playlist.enqueue("Song 1 - Artist A.mp3", 240)  # 4 minutes
    playlist.enqueue("Song 2 - Artist B.mp3", 180)  # 3 minutes
    playlist.enqueue("Song 3 - Artist C.mp3", 300)  # 5 minutes
    playlist.display_tracks()

    playlist.shuffle_playlist()
    playlist.display_tracks()

    playlist.count_tracks()
    playlist.total_duration()

    playlist.save_playlist('import random')

class MP3Playlist:
    def __init__(self):
        self.tracks = []  # Initialize an empty list to store tracks
        self.durations = {}  # Dictionary to store track durations

    def load_playlist(self, filename):
        """Load a playlist from a text file."""
        try:
            with open(filename, 'r') as file:
                for line in file:
                    track = line.strip()
                    if track:  # Ensure the line is not empty
                        self.enqueue(track)
            print(f"Loaded playlist from {filename}.")
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")

    def display_tracks(self):
        """Display all tracks in the playlist."""
        if not self.tracks:
            print("The playlist is empty.")
        else:
            print("Current Playlist:")
            for index, track in enumerate(self.tracks, start=1):
                print(f"{index}. {track} (Duration: {self.durations.get(track, 'N/A')} seconds)")

    def enqueue(self, track, duration=None):
        """Add an MP3 track to the end of the playlist."""
        self.tracks.append(track)
        if duration is not None:
            self.durations[track] = duration  # Store the duration if provided
        print(f"Added track: {track}")

    def remove_track(self, track):
        """Remove an MP3 track from the playlist."""
        if track in self.tracks:
            self.tracks.remove(track)
            self.durations.pop(track, None)  # Remove duration if it exists
            print(f"Removed track: {track}")
        else:
            print(f"Track not found: {track}")

    def save_playlist(self, filename):
        """Save the current playlist to a text file."""
        with open(filename, 'w') as file:
            for track in self.tracks:
                file.write(track + '\n')
        print(f"Playlist saved to {filename}.")

    def shuffle_playlist(self):
        """Shuffle all the songs in the playlist."""
        random.shuffle(self.tracks)
        print("Playlist shuffled.")

    def count_tracks(self):
        """Count the number of tracks in the playlist."""
        count = len(self.tracks)
        print(f"Number of tracks in the playlist: {count}")
        return count

    def total_duration(self):
        """Calculate the total duration of the playlist."""
        total = sum(self.durations.get(track, 0) for track in self.tracks)
        print(f"Total duration of the playlist: {total} seconds")
        return total

    def clear_playlist(self):
        """Clear/reset the playlist."""
        self.tracks.clear()
        self.durations.clear()
        print("Playlist cleared.")

    def is_empty(self):
        """Check if the playlist is empty."""
        empty = len(self.tracks) == 0
        if empty:
            print("The playlist is empty.")
        else:
            print("The playlist is not empty.")
        return empty

# Example usage
if __name__ == "__main__":
    playlist = MP3Playlist()
    playlist.enqueue("Song 1 - Artist A.mp3", 240)  # 4 minutes
    playlist.enqueue("Song 2 - Artist B.mp3", 180)  # 3 minutes
    playlist.enqueue("Song 3 - Artist C.mp3", 300)  # 5 minutes
    playlist.display_tracks()

    playlist.shuffle_playlist()
    playlist.display_tracks()

    playlist.count_tracks()
    playlist.total_duration()

    playlist.save_playlist('my_playlist.txt')
    playlist.remove_track("Song 2 - Artist B.mp3")
    playlist.display_tracks()

    playlist.clear_playlist()
    playlist.is_empty()
    playlist.remove_track("Song 2 - Artist B.mp3")
    playlist.display_tracks()

    playlist.clear_playlist()
    playlist.is_empty()