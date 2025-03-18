# Next Word Prediction using LSTM

## Overview
This project implements a next-word prediction model using LSTM (Long Short-Term Memory) networks. It trains on the text from `blue_castle.txt` and learns to predict the next word based on the given input sequence.

## Setup Instructions
### 1. Create and Activate Virtual Environment
#### On Windows (cmd or PowerShell):
```sh
python -m venv venv
venv\Scripts\activate
```
#### On macOS/Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

## Training the Model
Before making predictions, ensure the model is trained and saved.
```sh
python train_model.py
```
This will generate the `next_word.keras` model file.

## Running Predictions
After training, you can test the next-word prediction using:
```sh
python predict.py
```
Enter a phrase, and the model will predict the next word.

## Project Files
- `Next_word_prediction_using_LSTM_walkthrough.ipynb` - Jupyter Notebook with detailed explanations
- `train_model.py` - Script to preprocess text, train the LSTM model, and save it
- `predict.py` - Script to load the trained model and make predictions
- `requirements.txt` - List of required dependencies
- `README.md` - This file with setup instructions

## Notes
Ensure that you run `train_model.py` before running `predict.py`, as the trained model file `next_word.keras` must be created first.

