import pygame
import random
import time
import json
import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
DATA_FILE = 'data.json'
BEEP_FILE = 'beep.wav'
BUZZ_FILE = 'buzz.wav'
class ReactionTest:
    def __init__(self, trials=10):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Cognitive Lag Detector")
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        self.trials = trials
        self.reaction_times = []
        self.sound_enabled = False
        try:
            pygame.mixer.init()
            self.beep = pygame.mixer.Sound(BEEP_FILE)
            self.buzz = pygame.mixer.Sound(BUZZ_FILE)
            self.sound_enabled = True
        except:
            print("Sound files missing or audio device unavailable.")

    def draw_text(self, text, y):
        rendered = self.font.render(text, True, (255, 255, 255))
        rect = rendered.get_rect(center=(300, y))
        self.screen.blit(rendered, rect)

    def draw_distraction(self):
        chars = ['$', '#', '@', '*', '%', '&', '!', '?']
        for _ in range(30):
            x = random.randint(0, 600)
            y = random.randint(0, 400)
            char = random.choice(chars)
            distraction_text = self.font.render(char, True, (255, 0, 0))
            self.screen.blit(distraction_text, (x, y))

    def wait_for_space(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return
            self.clock.tick(60)

    def run(self):
        for trial in range(self.trials):
            self.screen.fill((0, 0, 0))
            self.draw_text(f"Trial {trial+1}: Press SPACE when screen turns green", 180)
            pygame.display.flip()
            time.sleep(random.uniform(2, 5))

            self.screen.fill((0, 0, 0))
            self.draw_distraction()
            pygame.display.flip()
            time.sleep(0.3)

            self.screen.fill((0, 255, 0))
            pygame.display.flip()
            if self.sound_enabled: self.beep.play()
            start = time.time()

            self.wait_for_space()
            reaction_time = time.time() - start
            self.reaction_times.append(reaction_time)

            if reaction_time > 0.45 and self.sound_enabled:
                self.buzz.play()

            self.screen.fill((0, 0, 0))
            self.draw_text(f"Reaction time: {reaction_time:.3f} sec", 200)
            pygame.display.flip()
            time.sleep(1)

        pygame.quit()
        return self.reaction_times
