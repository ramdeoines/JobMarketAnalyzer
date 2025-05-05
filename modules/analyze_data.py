import pandas as pd
from collections import Counter
from datetime import datetime

def load_job_data(path="data/jobs.csv"):
    """
    Loads job data from a CSV file and parses the 'Date Posted' column.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded job data.
    """
    return pd.read_csv(path, parse_dates=["Date Posted"])

def get_top_skills(df, top_n=10):
    """
    Extracts and counts the most in-demand skills from the job data.

    Args:
        df (pd.DataFrame): DataFrame containing job listings.
        top_n (int): Number of top skills to return.

    Returns:
        pd.DataFrame: Top skills with their frequencies.
    """
    all_skills = []
    for skills in df["Skills"]:
        all_skills.extend([skill.strip() for skill in skills.split(",")])
    
    skill_counts = Counter(all_skills)
    return pd.DataFrame(skill_counts.most_common(top_n), columns=["Skill", "Count"])

def get_jobs_by_location(df):
    """
    Counts the number of job postings per location.

    Args:
        df (pd.DataFrame): DataFrame containing job listings.

    Returns:
        pd.DataFrame: Job count by location.
    """
    location_counts = df["Location"].value_counts().reset_index()
    location_counts.columns = ["Location", "Count"]
    return location_counts

def get_jobs_over_time(df, freq="W"):
    """
    Aggregates the number of job postings over time.

    Args:
        df (pd.DataFrame): DataFrame with job listings.
        freq (str): Frequency for grouping (e.g., 'W' for weekly, 'M' for monthly).

    Returns:
        pd.DataFrame: Time-series job count.
    """
    df["Date Posted"] = pd.to_datetime(df["Date Posted"])
    trend = df.groupby(pd.Grouper(key="Date Posted", freq=freq)).size().reset_index(name="Job Count")
    return trend
