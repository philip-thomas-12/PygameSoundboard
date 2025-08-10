from pynput import keyboard
import pygame
import os

pygame.mixer.init()

SOUNDS_DIR = "sounds"
key_map = {
    'a': "a.mp3",
    'b': "b.mp3",
    'c': "c.mp3",
    'd': "d.mp3",
    'e': "e.mp3",
    'f': "f.mp3",
    'g': "g.mp3",
    'h': "h.mp3",
    'i': "i.mp3",
    'j': "j.mp3",
    'k': "k.mp3",
    'l': "l.mp3",
    'm': "m.mp3",
    'n': "n.mp3",
    'o': "o.mp3",
    'p': "p.mp3",
    'q': "q.mp3",
    'r': "r.mp3",
    's': "s.mp3",
    't': "t.mp3",
    'u': "u.mp3",
    'v': "v.mp3",
    'w': "w.mp3",
    'x': "x.mp3",
    'y': "y.mp3",
    'z': "z.mp3",
    ',': "comma.wav",
    ' ': "space.wav",
    # Add more keys and sounds here
}

def play_sound_for_key(key_char):
    filename = key_map.get(key_char)
    if filename:
        path = os.path.join(SOUNDS_DIR, filename)
        if os.path.exists(path):
            sound = pygame.mixer.Sound(path)
            sound.play()
        else:
            print(f"Sound file not found: {filename}")

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            play_sound_for_key(key.char)
    except AttributeError:
        pass  # You can handle special keys here if you want

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on ESC key press
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
