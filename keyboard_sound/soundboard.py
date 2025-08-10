import pygame
import os

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 100))

SOUNDS_DIR = "sounds"
key_to_sound = {
    pygame.K_a: "a.mp3",
    pygame.K_b: "b.mp3",
    pygame.K_c: "c.mp3",
    pygame.K_d: "d.mp3",
    pygame.K_e: "e.mp3",
    pygame.K_f: "f.mp3",
    pygame.K_COMMA: "comma.wav",
    pygame.K_SPACE: "space.wav",
    # Add more as needed
}

def play_sound(filename):
    path = os.path.join(SOUNDS_DIR, filename)
    if os.path.exists(path):
        sound = pygame.mixer.Sound(path)
        sound.play()
    else:
        print(f"No sound for {filename}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in key_to_sound:
                play_sound(key_to_sound[event.key])

pygame.quit()
