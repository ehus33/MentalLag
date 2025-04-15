# ⚡ Reaction Time Tracker

Tired? Distracted? Brain turned to soup after 4 hours of scrolling LinkedIn?  
This little desktop app checks your **cognitive reflexes** using real-time reaction tests, visual distractions, and audio feedback. It tracks your scores daily, roasts you when you’re slow, and charts your decline into burnout with beautiful graphs.

---

## 🧪 What It Does

- 🎯 Press SPACE when the screen turns green — simple.
- 🤯 Random distractions mess with your focus.
- 📉 Reaction times are logged & saved per day.
- 📊 Leaderboard charts your best/worst days.
- 💀 If you’re slow, you get roasted.

---

## 📦 Installation

1. **Clone this repo**
```bash
git clone https://github.com/ehus33/MentalLag.git
cd reaction-tracker
```

2. **Install dependencies**
```bash
pip install pygame matplotlib numpy
```

3. **(Optional) Add sounds**
Put `beep.wav` and `buzz.wav` in the same folder if you want audio feedback.

---

## 🚀 Usage

```bash
python main.py
```

- The test will start.
- Press **SPACE** as fast as possible when the screen goes green.
- At the end, you’ll see:
  - A chart of your reaction times
  - A roast (based on how cooked your brain is)
  - A leaderboard of your past performance

---

## 🧠 Example Output

```
Trial 1: 0.341s
Trial 2: 0.289s
Trial 3: 0.503s
🔥 Roast: "Did you fall asleep? Your grandma could’ve out-clicked you blindfolded."

## 💾 Data Format

All results are saved to `data.json`:
```json
{
  "2025-04-14": [0.402, 0.387, 0.433, 0.381],
  "2025-04-15": [0.345, 0.369, 0.310, 0.298]
}
```

---

## 🛠️ Future Ideas

- GUI version with buttons
- High score tracking
- Online leaderboard (for science)
- Fatigue detection with webcam + blinking rate

---

## ⚠️ Disclaimer

This does not replace a neurologist.  
But it *will* call you out when your reaction time dips below “potato.”

---
## 🪲 Current Issues

- A person can click before the light shines to get really high scores
- App gives me epilepsy
- Sometimes clicks don't register

## 🧑‍💻 Author

Created with ❤️ by [Ethan](https://github.com/ehus33)  
Feel free to fork, modify, or add cursed features.
