Here’s how to use the project both manually and with Docker.

---

# 🚀 Next Word Prediction using LSTM

## Overview
This project implements a next-word prediction model using LSTM (Long Short-Term Memory) networks. It trains on the text from `blue_castle.txt` and learns to predict the next word based on the given input sequence.

---

## 🔹 Option 1: Manual Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/harmeshgv/LSTM-NextWordPredictor.git
cd LSTM-NextWordPredictor
```

### 2️⃣ Create and Activate Virtual Environment  
#### ➤ Windows (cmd or PowerShell):
```sh
python -m venv venv
venv\Scripts\activate
```
#### ➤ macOS/Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Train the Model  
Run the training script to generate `next_word.keras`:
```sh
python train_model.py
```

### 5️⃣ Run Predictions  
Once trained, test the next-word prediction:
```sh
python predict.py
```
Try:
```sh
Enter your line: The book was
```
Expected output:
```sh
castle
```
To exit, type `0`.

---

## 🔹 Option 2: Using Docker 🐳

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/harmeshgv/LSTM-NextWordPredictor.git
cd LSTM-NextWordPredictor
```

### 2️⃣ Build the Docker Image  
```sh
docker build -t lstm-nextword-predictor .
```

### 3️⃣ Run the Container  
```sh
docker run --rm -it lstm-nextword-predictor
```

This will automatically train the model and start the prediction script.

---

## 📝 Project Files
- `Next_word_prediction_using_LSTM_walkthrough.ipynb` - Jupyter Notebook with explanations
- `train_model.py` - Preprocesses text, trains the LSTM model, and saves it
- `predict.py` - Loads the trained model and makes predictions
- `requirements.txt` - Required dependencies
- `Dockerfile` - Docker setup for running the project
- `README.md` - This guide

---

## 🔥 Notes
- **For manual setup**, train the model before running predictions.
- **With Docker**, everything is automated! 🚀