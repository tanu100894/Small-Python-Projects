import streamlit as st
import plotly.express as px
import glob
from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path

filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

dates = []
positivity = []
negativity = []

for filepath in filepaths:
    with open(filepath, "r") as file:
        content = file.read()
        pos = analyzer.polarity_scores(content)["pos"]
        neg = analyzer.polarity_scores(content)["neg"]
        date = Path(filepath).stem
        positivity.append(pos)
        negativity.append(neg)
        dates.append(date)

# Title for the App
st.title("Diary Tone")

# Create Positivity plot
st.subheader("Positivity")
pos_plot = px.line(x=dates, y=positivity,
                   labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_plot)

# Create Negativity plot
st.subheader("Negativity")
neg_plot = px.line(x=dates, y=negativity,
                   labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_plot)



