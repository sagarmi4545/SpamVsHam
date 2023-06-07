from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Load the BERT model
#import pickle

# Load the BERT model from the pickle file
#with open('spam_bert_model.pkl', 'rb') as f:
#    bert_model = pickle.load(f)


# Define the home route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the text input from the form
        text = request.form['text']

        # Tokenize the text
        k = random.randint(0, 1)
        print("LAbel is: ", k)
        predicted_label = ['spam', 'not spam'][k]

        # Return the prediction result as JSON
        return jsonify({'text': text, 'predicted_label': predicted_label})

    # Render the home template
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
