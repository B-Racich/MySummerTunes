# img_viewer.py

import PySimpleGUI as sg
import os.path
import threading
import pygame

from classes.MusicManager import MusicManager

mm = MusicManager()
pygame.init()
pygame.mixer.init()
sound = pygame.mixer
song_thread = threading
volume_level = 0.25
# First the window layout in 2 columns

def playSong(fileName):
    print(fileName)
    global song
    global stop_song
    stop_song = False
    song = sound.Sound(fileName)
    song.set_volume(volume_level)
    while True:
        song.play()
        if stop_song:
            song.stop()
            break
  
def adjustVolume(value):
    global volume_level
    volume_level = value
    try:
        song.set_volume(volume_level)
    except:
        print("No song selected")
    
def stopSong():
    song.stop()

file_list_column = [
    [
        sg.Text("Music Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Song URL"),
        sg.In(size=(25, 1), enable_events=True, key="-URL-"),
        sg.Button("Download")
    ],
    [
        sg.Slider(orientation ='horizontal', enable_events=True, key='-VOLUME-', range=(1,100), default_value=50),
        sg.Button("Stop")
    ],
    [
        sg.Listbox(
            values=os.listdir('Tracks'), enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose a track from the list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("MySummerTunes", layout)

while True:
    event, values = window.read()
    print(event, values)

    if event == "Download":
        mm.download(values['-URL-'])

    if event == "-FILE LIST-":
        filename = "Tracks/"+values['-FILE LIST-'].pop()
        stop_song = True
        song_thread = threading.Thread(target=playSong, args=(filename,))
        song_thread.start()
        
    
    if event == "-VOLUME-":
        adjustVolume(values["-VOLUME-"]/100.0)
        
    if event == "Stop":
        stop_song = True
        stopSong()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break