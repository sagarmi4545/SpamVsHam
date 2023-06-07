# BERT Spam vs Ham Classifier

This project implements a BERT-based spam vs ham classifier. It uses a pre-trained BERT model to classify text messages as either spam or ham (non-spam). The classifier is built using Python, Flask, and a trained BERT model.

## Project Structure

The project has the following structure:

- `app.py`: The Flask application script that serves the classifier API and UI.
- `spam_bert_model.pkl`: The trained BERT model serialized as a pickle file.
- `templates/`: Directory containing the HTML templates for the user interface.
  - `index.html`: The main HTML template for the classifier UI.
- `bert_model_training.ipynb`: A python jupytor note book to train the model.
## Dataset

The dataset used for training the classifier was imbalanced, with a significantly larger number of ham (non-spam) messages compared to spam messages. Dealing with imbalanced datasets can be a challenge as it can lead to biased models. To address this issue, the following techniques were applied:

- **Oversampling**: Synthetic spam samples were generated to balance the classes. This involved replicating existing spam samples or using techniques like SMOTE (Synthetic Minority Over-sampling Technique) to create new synthetic samples.

- **Undersampling**: Random subsampling was performed on the majority class (ham) to reduce its dominance in the dataset. This helped to create a more balanced training set.

- **Weighted Loss Function**: A weighted loss function was used during training to assign higher weights to misclassified spam samples. This helped to prioritize the correct classification of spam messages.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:
   - git clone https://github.com/sagarmi4545/SpamVsHam.git
3. Install the required packages:
   - pip install -r requirements.txt
5. Import the trained BERT model:
   - Ensure that you have the trained BERT model serialized as a `spam_bert_model.pkl` file.
   - Place the `spam_bert_model.pkl` file in the root directory of the project.
6. Run the Flask application:
   - python app.py
7. Access the classifier UI:
   - Open a web browser and visit `http://localhost:5000` to access the classifier UI.
   - Enter a text message in the input field and click the "Classify" button to see the predicted label.

## Customization

You can customize and extend the project as needed:

- **Training your own BERT model**: If you want to train your own BERT model, you can use Google Colab or any other platform that supports BERT training. Once you have the trained model, you can export it and replace the `spam_bert_model.pkl` file in the project.

- **UI Enhancements**: The UI templates are located in the `templates/` directory. You can modify the HTML and CSS files to change the appearance or add additional features to the classifier UI.

- **API Endpoints**: The Flask application script `app.py` contains the API endpoints for the classifier. You can modify or add new endpoints to suit your requirements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.


