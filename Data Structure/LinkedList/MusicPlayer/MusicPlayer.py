import os
import tkinter as tk
import pygame
import Circular_Doubly_Linked_List as list


def play_song(file_path, position=0):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(0, position / 1000)


def stop_song():
    pygame.mixer.music.stop()


song_file = "./songs/Softly_320(PagalWorld.com.pe).mp3"
play_song(song_file)


def get_files_from_folder(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


cdll = list.CircularDoublyLinkedList()
for song in get_files_from_folder("./songs"):
    cdll.insertAtBeginning(song)


class MusicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music App")
        self.song = cdll.tail
        self.current_song_position = 0
        self.update_seek()

        self.song_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 16))
        self.song_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipady=20)

        songs_folder = "songs"
        self.song_files = [f for f in os.listdir(songs_folder) if os.path.isfile(os.path.join(songs_folder, f))]

        for song_file in self.song_files:
            self.song_listbox.insert(tk.END, song_file)

        self.song_listbox.bind("<<ListboxSelect>>", self.on_song_selected)

        self.player_frame = tk.Frame(root)
        self.player_frame.pack(side=tk.RIGHT, padx=60, pady=20)

        self.current_song_label = tk.Label(self.player_frame, text="Current Song: ")
        self.current_song_label.pack()

        self.play_pause_button = tk.Button(self.player_frame, text="Play", command=self.toggle_play_pause)
        self.play_pause_button.pack(pady=10)

        self.next_button = tk.Button(self.player_frame, text="Next", command=self.play_next)
        self.next_button.pack(pady=10)

        self.prev_button = tk.Button(self.player_frame, text="Previous", command=self.play_previous)
        self.prev_button.pack(pady=10)

        self.currently_playing = None
        self.is_playing = False

    def on_song_selected(self, event):
        selected_index = self.song_listbox.curselection()
        if selected_index:
            selected_song = self.song_listbox.get(selected_index)
            self.current_song_label.config(text="Current Song: " + selected_song)
            self.currently_playing = selected_song
            play_song(f"./songs/{selected_song}")

    def toggle_play_pause(self):
        if self.is_playing:
            self.pause_song()
        else:
            self.play_song()

    def play_song(self):
        play_song(f"./songs/{self.song.data}", self.current_song_position)
        self.is_playing = True
        self.play_pause_button.config(text="Pause")
        print("Play the song", self.current_song_position)

    def pause_song(self):
        self.current_song_position = pygame.mixer.music.get_pos()
        stop_song()
        self.is_playing = False
        self.play_pause_button.config(text="Play")
        print("Pausing the song", self.current_song_position)

    def play_next(self):
        play_song(f"./songs/{self.song.next.data}")
        self.song = self.song.next
        print("Playing Next Song")
        self.current_song_label.config(text=self.song.data)

    def play_previous(self):
        play_song(f"./songs/{self.song.prev.data}")
        self.song = self.song.prev
        print("Playing Previous Song")
        self.current_song_label.config(text=self.song.data)

    def update_seek(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x450")
    app = MusicApp(root)
    root.mainloop()
