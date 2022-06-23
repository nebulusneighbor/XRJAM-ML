import os
import mido
import time

from mido import MidiFile, MidiTrack

# A port needs to be opened here to send it
port = mido.open_output('loopMIDI Port 1')# new line to open virtual port, check to see if loopmidi changed names if it doesnt work


def playMIDI():
    #n=0
    mid=MidiFile(full_path)

    #mid.tracks[1] = mid.tracks[1][1385:] #deletes first two messages in track 1

    for msg in mid:
        if not msg.is_meta:
            time.sleep(msg.time)#time.sleep(.1) fixes loop, but plays weird
            port.send(msg)




while time.time() > 0:
    ## read from folder in SPECIFIC directory
    rootdir = r'C:\Users\ptgyo\OneDrive\Documents\XRJAM\ML\ML_Drummer\generated_Drums'
    all_files = os.listdir(rootdir) # gets all files in the directory
    txt_files = filter(lambda x: x[-4:] == '.mid', all_files) # filters for only midi files
    full_path = os.path.join(rootdir, max(txt_files)) # gets the absolute path to the most recently created file
    print(full_path)
    #timer= time.sleep(1)
    playMIDI()
    #playMIDI()
    #playMIDI()
    # can always make the time to create new MIDI a little longer in Ableton, but this ensures it plays musically relevant time (to some degree)
