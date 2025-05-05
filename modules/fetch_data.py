import pandas as pd
import random
from datetime import datetime, timedelta

# ----------------------------------
# Sample pools for job data creation
# ----------------------------------
locations = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Al Ain"]
skills = ["Python", "Java", "JavaScript", "SQL", "C#", "Django", "React", "Vue", "Node.js", "AWS"]
titles = ["Data Analyst", "Software Engineer", "Backend Developer", "Data Scientist", "Frontend Developer"]

def generate_mock_data(num_entries=100):
    """
    Generates a list of mock job postings with random titles, locations, skills, and dates.

    Args:
        num_entries (int): Number of job entries to generate.

    Returns:
        pd.DataFrame: DataFrame containing mock job postings.
    """
    data = []
    for _ in range(num_entries):
        job = {
            "Title": random.choice(titles),
            "Location": random.choice(locations),
            "Skills": ", ".join(random.sample(skills, k=random.randint(2, 5))),
            "Date Posted": (datetime.now() - timedelta(days=random.randint(0, 60))).date()
        }
        data.append(job)
    return pd.DataFrame(data)

def save_to_csv(df, path="data/jobs.csv"):
    """
    Saves the DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        path (str): File path to save CSV.
    """
    df.to_csv(path, index=False)
    print(f"Saved mock data to {path}")

# -------------------------------
# Debug usage when run directly
# -------------------------------
if __name__ == "__main__":
    df = generate_mock_data()
    save_to_csv(df)
