# 📊 Job Market Analyzer

A **Python-based Streamlit web app** that analyzes **mock job market trends** using generated job postings.  
It extracts insights on **top tech skills**, **hiring locations**, and **posting trends over time**.

---

## 🚀 Features

- 🔹 **Generates mock job postings** with random skills, locations, and dates  
- 🔹 **Analyzes demand** for top skills in the job market  
- 🔹 **Visualizes hiring trends** using interactive charts  
- 🔹 **Built with:** `Python`, `pandas`, `matplotlib`, `Streamlit`  

---

## 🛠️ Installation & Usage

1️⃣ **Clone this repository**  
```bash
git clone https://github.com/ramdeoines/JobMarketAnalyzer.git
cd JobMarketAnalyzer

2️⃣ Create a virtual environment & install dependencies
python -m venv venv
venv\Scripts\activate  # (On Windows)
pip install -r requirements.txt

3️⃣ Run the app
streamlit run app.py

4️⃣ Open the app in your browser
(http://localhost:8501)

📂 Project Structure
JobMarketAnalyzer/
│
├── app.py                   # Main Streamlit app
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
│
├── data/                     # Stores mock job data
│   └── jobs.csv
│
├── modules/                  # Processing logic
│   ├── fetch_data.py         # Generates mock job postings
│   ├── analyze_data.py       # Extracts skill & location trends
│   ├── visualize.py          # Creates bar charts & time-series plots
│
└── venv/                     # Virtual environment (ignored in Git)