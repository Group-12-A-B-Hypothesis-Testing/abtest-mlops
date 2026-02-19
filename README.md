# A/B Testing with MLOps

A/B testing implementation using Machine Learning and MLOps practices to evaluate ad campaign performance and measure brand awareness lift.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Business Objective](#business-objective)
- [Problem Statement](#problem-statement)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Team Members](#team-members)

## 🎯 Project Overview

This repository contains an A/B testing implementation designed to compare different versions of advertising campaigns and determine which performs better. The project uses Machine Learning and MLOps practices to build a reliable hypothesis testing algorithm for measuring the impact of advertising campaigns on brand awareness.

**10 Academy Batch 6 Weekly Challenge: Week 2**

## 💼 Business Objective

An advertising company is running an online ad campaign for a client with the intention of increasing brand awareness. The advertiser earns money by charging the client based on user engagements with the ad it designed and serves via different platforms.

To increase market competitiveness, the advertising company provides a service that quantifies the increase in brand awareness as a result of the ads shown to online users. 

**Main Objective:** Test if the ads that the advertising company runs resulted in a significant lift in brand awareness.

## 🔍 Problem Statement

**SmartAd** is a mobile-first advertiser agency that designs intuitive touch-enabled advertising. They provide brands with an automated advertising experience via machine learning and creative excellence. Their company is based on the principle of voluntary participation, which is proven to increase brand engagement and memorability 10x more than static alternatives.

SmartAd provides an additional service called **Brand Impact Optimiser (BIO)**, a lightweight questionnaire served with every campaign to determine the impact of the creative (the ad they design) on various upper funnel metrics, including memorability and brand sentiment.

**Task:** As a Machine Learning Engineer at SmartAd, design a reliable hypothesis testing algorithm for the BIO service and determine whether a recent advertising campaign resulted in a significant lift in brand awareness.

## 📁 Project Structure

```
abtest-mlops/
│
├── data/                       # Data files (DVC-tracked)
│   ├── raw/                    # Raw datasets
│   └── processed/              # Processed datasets
│
├── notebooks/                  # Jupyter notebooks for analysis
│   ├── exploratory/           # Exploratory data analysis
│   └── final/                  # Final analysis and results
│
├── scripts/                    # Python modules and scripts
│
├── tests/                      # Unit tests
│
├── mlruns/                     # MLflow experiment tracking (gitignored)
│
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
└── README.md
```

## 🚀 Installation

### Prerequisites

- Python 3.6+
- Git
- DVC (for data versioning)

### Setup

1. **Clone the repository**
   ```bash
   git clone git@github.com:Group-12-A-B-Hypothesis-Testing/abtest-mlops.git
   cd abtest-mlops
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Pull data (if using DVC)**
   ```bash
   dvc pull
   ```

## 💻 Usage

1. **Run exploratory analysis:** Navigate to `notebooks/exploratory/` for data exploration and initial hypothesis testing
2. **View final results:** Check `notebooks/final/` for comprehensive analysis and conclusions
3. **Run scripts:** Use modules in `scripts/` for automated testing and model deployment
4. **Run tests:** Execute `pytest tests/` to run unit tests

## 🛠️ Technologies Used

- **Python 3.6+**
- **Data Science:** pandas, numpy, scipy, scikit-learn
- **Visualization:** matplotlib, seaborn
- **MLOps:** MLflow (experiment tracking), DVC (data versioning)
- **Testing:** pytest
- **Web Framework:** Flask, Django
- **NLP:** NLTK, TextBlob, Gensim

## 👥 Team Members

- **Janerose Njogu**
- **Egide Kamuzinzi**
- **Yonas Moges**
- **Nahom Habtemichael**

---

⭐ If you find this project helpful, please consider giving it a star!
