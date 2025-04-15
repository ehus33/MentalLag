import pygame
import random
import time
import json
import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
class ScoreStorage:
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                json.dump({}, f)

    def load(self):
        with open(self.filepath, 'r') as f:
            return json.load(f)

    def save_score(self, date_str, score_list):
        data = self.load()
        data[date_str] = score_list
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def get_leaderboard(self):
        data = self.load()
        return [(day, np.mean(times)) for day, times in data.items() if times]
