import tkinter as tk
from tkinter import messagebox
import os


if not os.path.exists("playlists"):
    os.makedirs("playlists")


def save_playlist():
    playlist_name = entry_name.get().strip()
    songs = text_songs.get("1.0", tk.END).strip().split("\n")

    if not playlist_name:
        messagebox.showwarning("Input Error", "Please enter a playlist name.")
        return

    if not songs or songs == [""]:
        messagebox.showwarning("Input Error", "Please enter at least one song.")
        return

    filename = os.path.join("playlists", f"playlist_{playlist_name}.txt")
    if os.path.exists(filename):
        messagebox.showerror("Duplicate Error", f"Playlist '{playlist_name}' already exists!")
        return

    try:
        f = open(filename, "w", encoding="utf-8")
        f.write("\n".join(songs)) 
        f.close()

        messagebox.showinfo("Success", f"Playlist '{playlist_name}' saved!")
        entry_name.delete(0, tk.END)
        text_songs.delete("1.0", tk.END)
        load_playlists()

    except Exception as e:
        messagebox.showerror("Error", f"Could not save playlist: {e}")


def load_playlists():
    listbox_playlists.delete(0, tk.END)
    for file in os.listdir("playlists"):
        if file.startswith("playlist_") and file.endswith(".txt"):
            listbox_playlists.insert(tk.END, file)


def show_playlist(event):
    try:
        selection = listbox_playlists.get(listbox_playlists.curselection())
        filepath = os.path.join("playlists", selection)
        
        f = open(filepath, "r", encoding="utf-8")
        songs = f.read()
        f.close()

        text_display.delete("1.0", tk.END)
        text_display.insert(tk.END, songs)

    except FileNotFoundError:
        messagebox.showerror("Error", "Selected playlist file not found!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not load playlist: {e}")


root = tk.Tk()
root.title("MusicBox - Playlist Manager")
root.geometry("600x500")


frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

tk.Label(frame_left, text="Create New Playlist", font=("Arial", 14, "bold")).pack(pady=5)

tk.Label(frame_left, text="Playlist Name:").pack(anchor="w")
entry_name = tk.Entry(frame_left, width=30)
entry_name.pack(pady=5)

tk.Label(frame_left, text="Enter Songs (one per line):").pack(anchor="w")
text_songs = tk.Text(frame_left, height=10, width=30)
text_songs.pack(pady=5)

btn_save = tk.Button(frame_left, text="Save Playlist", command=save_playlist, bg="lightblue", font=("Arial", 12))
btn_save.pack(pady=10)


frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

tk.Label(frame_right, text="Existing Playlists", font=("Arial", 14, "bold")).pack(pady=5)

listbox_playlists = tk.Listbox(frame_right, height=10, width=40)
listbox_playlists.pack(pady=5, fill=tk.X)
listbox_playlists.bind("<<ListboxSelect>>", show_playlist)

tk.Label(frame_right, text="Songs in Playlist:").pack(anchor="w")
text_display = tk.Text(frame_right, height=15, width=40, state="normal")
text_display.pack(pady=5, fill=tk.BOTH, expand=True)


load_playlists()

root.mainloop()
