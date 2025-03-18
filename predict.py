import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer

# Load the trained model and tokenizer
model = load_model('next_word.keras')
tokenizer = pickle.load(open('token.pkl', 'rb'))

def predict_next_word(text):
    sequence = tokenizer.texts_to_sequences([text])
    sequence = np.array(sequence)
    preds = np.argmax(model.predict(sequence))
    predicted_word = ""
    
    for key, value in tokenizer.word_index.items():
        if value == preds:
            predicted_word = key
            break
    
    return predicted_word

if __name__ == "__main__":
    while True:
        text = input("Enter your line (or type 0 to exit): ")
        
        if text == "0":
            print("Execution completed....")
            break
        
        try:
            text = text.split(" ")[-3:]
            text = " ".join(text)
            print("Predicted next word:", predict_next_word(text))
        
        except Exception as e:
            print("Error occurred:", e)
            continue
