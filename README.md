# Python-guess-the-song-game  
# 🎶 Rock Your Decades – Guess the Song  

## Description
Rock Your Decades is a Python-based game built with Tkinter where players guess the original English song titles from their Hindi translations. The game starts with a timer of 30 seconds, and each correct guess increases your score and adds bonus time, while wrong guesses reduce your remaining time. It uses Google Translate (via `googletrans`) to generate Hindi translations, a large song list stored in `Songs.txt`, and a leaderboard saved in `scores.csv` to keep track of scores.  

**## Features**  
- 🕹️ Fun and interactive Tkinter-based UI  
- ⏳ Countdown timer with bonus/penalty mechanics  
- 🌐 Google Translate integration for Hindi translations  
- 🎵 100+ songs provided in `Songs.txt`  
- 🏆 Leaderboard to save and view high scores  

## Installation
1. Clone the repository.  
2. Make sure Python 3.8+ is installed.  
3. Install dependencies with:  
   ```bash
   pip install -r requirements.txt
**##Run the game with:**
bash
python game.py

## Files Included
game.py → Main Python game file
Songs.txt → Contains list of songs
scores.csv → Leaderboard file (auto-generated after first play)
requirements.txt → Python dependencies
README.md → Project documentation

## Future Improvements
Integration with Spotify or YouTube APIs for endless random songs
Multi-language support
Enhanced GUI with themes and animations

## Author
👩‍💻 Developed with ❤️ by Bhavni Chhabra
