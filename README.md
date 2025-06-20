# 🎬 Personalized Recommendation System

A simple and effective content-based movie recommendation system built with Python and Streamlit, using the MovieLens Latest Small dataset. It recommends movies based on the genre similarity of a user-selected movie.

🚀 Live Demo
💡 Coming Soon — Deploy using Streamlit Community Cloud or Render to share a public demo link.

📌 Features
✅ Content-Based Filtering using genres

🧠 TF-IDF Vectorization for text processing

🔎 Cosine Similarity for matching movies

🎥 Interactive and user-friendly Streamlit UI

📁 Uses clean and popular dataset: MovieLens

🧠 How It Works
This project implements a Content-Based Filtering approach, which:

Uses the genres column from the dataset as a textual description.

Applies TF-IDF Vectorization to convert genre text into numerical features.

Uses Cosine Similarity to compare the user-selected movie with all others.

Returns the top N movies with the most similar genres.

🗂️ Dataset Used
MovieLens Latest Small
📥 Download: ml-latest-small.zip

Used File: movies.csv
Contains:

movieId

title

genres

📁 Project Structure

personalized-reco-system/
│
├── app.py                 # Main Streamlit app
├── reco_engine.py         # Recommendation engine logic
├── data/
│   └── movies.csv         # Movie dataset (MovieLens)
├── prepare_movies_csv.py  # (optional) data preprocessing script
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
