from storage import ScoreStorage
from test import ReactionTest
import pygame
import random
import time
import json
import os
import matplotlib.pyplot as plt
import numpy as np
import datetime
class ReactionDashboard:
    def __init__(self, data_file):
        self.storage = ScoreStorage(data_file)

    def plot_today(self, today_scores):
        avg = np.mean(today_scores)
        if avg < 0.25:
            snark = "Are you a robot? That was cracked-level reaction time."
        elif avg < 0.35:
            snark = "Not bad. You're still mentally awake."
        elif avg < 0.45:
            snark = "Hmm. You might be fading. Drink water. Touch grass."
        else:
            snark = "Did you fall asleep? Your grandma could've out-clicked you blindfolded."

        plt.figure(figsize=(9, 5))
        plt.plot(today_scores, marker='o', label="Your Reaction Time")
        plt.axhline(y=avg, color='r', linestyle='--', label=f'Avg: {avg:.3f}s')
        plt.title("Reaction Time Today")
        plt.xlabel("Trial")
        plt.ylabel("Seconds")
        plt.grid(True)
        plt.legend()
        plt.subplots_adjust(bottom=0.25)
        plt.figtext(0.5, 0.02, snark, wrap=True, horizontalalignment='center', fontsize=12, color='purple')
        plt.tight_layout()
        plt.show()

    def plot_leaderboard(self):
        leaderboard = self.storage.get_leaderboard()
        if not leaderboard:
            print("No data yet.")
            return
        leaderboard.sort(key=lambda x: x[0])
        dates, averages = zip(*leaderboard)
        plt.figure(figsize=(10, 5))
        plt.plot(dates, averages, marker='o')
        plt.xticks(rotation=45)
        plt.title("Average Reaction Time by Day")
        plt.xlabel("Date")
        plt.ylabel("Avg Time (s)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()