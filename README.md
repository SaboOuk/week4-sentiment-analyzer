# week4-sentiment-analyzer
# Sentiment Analysis System

## Overview

This project implements sentiment analysis for product reviews using Natural Language Processing (NLP) techniques from Chapter 23.

## Features

- **Two Analysis Methods:**
  - Simple: Word counting based on positive/negative word lists  
  - Advanced: Machine learning using TextBlob
- **REST API** for easy integration
- **Visualization** of sentiment distributions
- **Text preprocessing** including tokenization and stop word removal

## How to Run

### 1. Install Requirements

```bash
pip install -r requirements.txt

## Challenges encountered
One challenge I encountered was installing and configuring the required NLP libraries, particularly NLTK and TextBlob, which required downloading additional datasets before the analyzer would run correctly. I also had to debug issues with the Flask API routes, such as handling missing JSON fields and ensuring appropriate error messages were returned. Understanding how polarity scores translate into positive, negative, or neutral labels took some experimentation, but testing multiple review examples helped clarify how the scoring system works.

## Real-World Applications
Companies use sentiment analysis to monitor product reviews, allowing them to identify common complaints or praise and adjust products accordingly.
Businesses track brand reputation on social media by analyzing large volumes of posts to detect trends, crises, or customer sentiment changes.
Customer service teams apply sentiment analysis to support tickets and chat logs, helping them prioritize dissatisfied users and improve response strategies.

## What I learned 
I learned how fundamental NLP preprocessing steps—such as tokenization and stop-word removal help clean text for more accurate analysis. I also gained a clearer understanding of how polarity and subjectivity scores from TextBlob reflect emotional tone and confidence in text. Implementing both a simple rule based analyzer and an advanced ML-based analyzer helped me see the differences between keyword counting and machine learning approaches. Additionally, building a Flask API taught me how to structure endpoints and return JSON responses for real-world application integration.