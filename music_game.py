import random
import os
import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
pygame.mixer.init()
root = tk.Tk()
root.withdraw()

directory = askdirectory()
os.chdir(directory)
list_dir = os.listdir(directory)
list_dir.sort()
print(f"\n{directory}\n")

list_of_songs = []
for files in list_dir:
    if files.endswith(".mp3"):
        list_of_songs.append(files)
another_track = True
score = 0
while another_track:
    try:
        three_rand_songs = random.sample(range(len(list_of_songs)), 3)
        rando = random.randint(0, 2)
        rando = int(rando)
        track_num = three_rand_songs[rando]
        choice = 1
        pygame.mixer.music.stop()
        pygame.mixer.init()
        try:
            pygame.mixer.music.load(list_of_songs[int(track_num)])
        except:
            pygame.mixer.music.load(list_of_songs[int(track_num)])

        pygame.mixer.music.play()
        for i in three_rand_songs:
            rand_song_list = i
            print(f"\n{choice}) --- {list_of_songs[rand_song_list]}\n")
            choice += 1

        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load(list_of_songs[int(track_num)])
        pygame.mixer.music.play()
        print("\n..............................\n")
        print("some files cause an error where no sound plays. If that happens just hit enter.\n")
        which_song = input(
            "Which song is playing? 1, 2, or 3? \n\nPress q to quit \n\n")
        rando += 1
        rando = str(rando)
        if which_song == rando:
            print("\n..............................\n")
            print("\nCORRECT!\n")
            score += 1
            print(f"The score is\n\n{score}\n")
            print("\n..............................\n")
        elif which_song == "q":
            print("\n..............................\n")
            print(
                f"Thanks for playing the final score was {score} correct answers")
            print("\n..............................\n")
            break
        else:
            print("\n..............................\n")
            print("\nSorry, that was not the answer.")
            print(f"The correct answer was {list_of_songs[int(track_num)]}\n")
            print(f"The score is\n\n{score}\n")
            print("\n..............................\n")
    except pygame.error:
        continue
