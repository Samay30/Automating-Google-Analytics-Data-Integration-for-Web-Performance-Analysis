import pandas as pd

def load_csv(file_path):
    """
    Load a CSV file into a Pandas DataFrame.
    Tries different encodings to handle potential errors.
    """
    try:
        df = pd.read_csv(file_path, encoding="ISO-8859-1")
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding="latin1")
    return df

def normalize_text(text):
    """
    Normalize text by stripping whitespace and converting to lowercase.
    This helps ensure accurate matching between CSV titles and analytics data.
    """
    return text.strip().lower() if isinstance(text, str) else text

def extract_analytics_data():
    """
    Define a dictionary containing page titles and their corresponding page views.
    The titles should match the first part of the title before ' | ' in Google Analytics.
    This dictionary should be manually updated based on extracted analytics data.
    """
    return {
        "page title 1": 500,
        "page title 2": 300,
        "page title 3": 150,
        # Add more extracted Google Analytics data here...
    }

def update_page_views(df, analytics_data):
    """
    Update the 'Page Views' column in the CSV file based on Google Analytics data.
    It matches the first part of the page title before ' | '.
    """
    # Normalize the analytics data for easier matching
    analytics_data_cleaned = {normalize_text(title): views for title, views in analytics_data.items()}
    
    # Normalize CSV titles and match with analytics data
    df["Title"] = df["Title"].apply(normalize_text)
    df["Page Views"] = df["Title"].apply(lambda x: analytics_data_cleaned.get(x, "N/A"))

    return df

def save_updated_csv(df, output_path):
    """
    Save the updated DataFrame to a new CSV file.
    """
    df.to_csv(output_path, index=False)
    print(f"Updated CSV saved at: {output_path}")

def main(input_csv_path, output_csv_path):
    """
    Main function that orchestrates the full process of:
    1. Loading the CSV file
    2. Extracting analytics data
    3. Updating page views
    4. Saving the updated CSV file
    """
    df = load_csv(input_csv_path)
    analytics_data = extract_analytics_data()
    df_updated = update_page_views(df, analytics_data)
    save_updated_csv(df_updated, output_csv_path)

# Example usage
input_csv_path = "path/to/input.csv"  # Replace with actual CSV file path
output_csv_path = "path/to/output.csv"  # Replace with desired output file path
main(input_csv_path, output_csv_path)
