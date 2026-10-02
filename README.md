# Twitter Sentiment Analysis Machine Learning Model

This project trains and uses a machine learning model to classify tweets as positive or negative.

## Project Structure

- `Collab File notebook/` - notebook used for model development and experimentation
- `Our_Trained_Model/` - saved trained model and vectorizer
- `Model_Use_Case_Inside_Application/` - Streamlit application used to predict sentiment from user input

## Requirements

- Python 3.10+
- scikit-learn
- streamlit

## Install dependencies

```bash
python -m pip install scikit-learn streamlit
```

## Run the web app

```bash
cd "Model_Use_Case_Inside_Application"
python -m streamlit run app.py
```

## Model usage

The app loads:

- `Our_Trained_Model/vectorizer.sav`
- `Our_Trained_Model/trained_model.sav`

Then it predicts whether a tweet is positive or negative.

## Author

Created by GABSIWAEL for a Twitter sentiment analysis use case in a machine learning project.
