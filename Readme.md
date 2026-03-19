# Movie Review Sentiment Analysis 🎬

## Overview
[cite_start]This project is an end-to-end Natural Language Processing (NLP) and Machine Learning application designed to perform sentiment analysis on movie reviews[cite: 4, 5]. [cite_start]It bridges the gap between raw textual data and a user-facing web application, providing reliable, real-time sentiment detection[cite: 286, 287].

## Features
* [cite_start]**Text Preprocessing:** Cleans raw review text by removing HTML tags, filtering non-alphabetic characters, removing stopwords, and applying stemming[cite: 30, 31, 32].
* [cite_start]**Feature Extraction:** Utilizes a TF-IDF Vectorizer to convert text into numerical vectors, emphasizing the importance of specific words[cite: 34, 85].
* [cite_start]**High-Performance Classification:** Employs a `LinearSVC` model to efficiently separate positive and negative sentiments[cite: 18, 86].
* [cite_start]**Interactive GUI:** Features a clean, interactive web interface built with Streamlit for real-time user predictions[cite: 51, 63, 88].
* [cite_start]**Proven Accuracy:** The deployed model achieves a 90.5% accuracy rate on the IMDB dataset[cite: 22, 270, 287].

## Tech Stack
* [cite_start]**Language:** Python [cite: 8]
* [cite_start]**Libraries:** Scikit-learn, NLTK, Pandas, NumPy, Regular Expressions (re), Pickle [cite: 9, 10, 11, 12, 13, 253, 254]
* [cite_start]**Frontend/Deployment:** Streamlit [cite: 88, 252]

## Project Structure
1. [cite_start]**Model Training (Google Colab):** Handles data ingestion, preprocessing, vectorization, training, and serializing the model using `pickle`[cite: 6, 87].
2. [cite_start]**Web Application (`app.py`):** The Streamlit frontend that loads the serialized `.pkl` files to analyze user-inputted movie reviews instantly[cite: 49, 56, 58].

## Installation & Setup
To run this project locally, ensure you have Python installed, then follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Sumit-Pathrabe/Movie-Review-Sentiment-Analysis.git](https://github.com/Sumit-Pathrabe/Movie-Review-Sentiment-Analysis.git)
   cd Movie-Review-Sentiment-Analysis
