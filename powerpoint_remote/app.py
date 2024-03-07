from pathlib import Path
import pyautogui
from flask import Flask, render_template

TEMPLATE_FOLDER = Path(__file__).parent / 'templates'

app = Flask(__name__, template_folder=TEMPLATE_FOLDER)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next')
def next_slide():
    pyautogui.press('right')
    return render_template('index.html')

@app.route('/previous') 
def previous_slide():
    pyautogui.press('left')
    return render_template('index.html')

@app.route('/first')
def first_slide():
    pyautogui.hotkey('ctrl', 'home')
    return render_template('index.html')

@app.route('/last')
def last_slide(): 
    pyautogui.hotkey('ctrl', 'end')
    return render_template('index.html')

