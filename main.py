import datetime
from datetime import datetime
from test import ReactionTest
from storage import ScoreStorage
from dashboard import ReactionDashboard

DATA_FILE = 'data.json'
BEEP_FILE = 'beep.wav'
BUZZ_FILE = 'buzz.wav'

if __name__ == "__main__":
    test = ReactionTest()
    scores = test.run()

    today = datetime.now().strftime("%Y-%m-%d")
    storage = ScoreStorage(DATA_FILE)
    storage.save_score(today, scores)

    dashboard = ReactionDashboard(DATA_FILE)
    dashboard.plot_today(scores)
    dashboard.plot_leaderboard()