import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import os
from pathlib import Path

# Function to scrape data from the given URL
def scrape_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        messagebox.showerror("Error", "Failed to retrieve the web page.")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Scraping table data (modify based on the structure of the web page)
    # Adjust the selector based on your specific use case
    table = soup.find('table')  
    if not table:
        messagebox.showerror("Error", "No table found on the web page.")
        return None

    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)

    return data

# Function to save data to a CSV file in the Downloads directory
def save_to_csv(data, filename):
    try:
        downloads_path = str(Path.home() / "Downloads")
        file_path = os.path.join(downloads_path, filename)

        # Debug: Print the file path to verify
        print(f"Saving file to: {file_path}")

        # Check if Downloads directory exists
        if not os.path.exists(downloads_path):
            raise Exception(f"Downloads directory does not exist: {downloads_path}")

        # Check if Downloads directory is writable
        if not os.access(downloads_path, os.W_OK):
            raise Exception(f"Downloads directory is not writable: {downloads_path}")

        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Success", f"Data saved to {file_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the file: {str(e)}")
        print(f"An error occurred while saving the file: {str(e)}")

# Function to run the scraper and save data
def run_scraper(url_entry, filename_entry):
    url = url_entry.get()
    filename = filename_entry.get()
    data = scrape_data(url)
    if data:
        save_to_csv(data, filename)

# Main function to create GUI
def main():
    root = tk.Tk()
    root.title("Web Scraper")

    # Create and place URL input
    ttk.Label(root, text="Enter the URL to scrape:").grid(column=0, row=0, padx=10, pady=5)
    url_entry = ttk.Entry(root, width=40)
    url_entry.grid(column=0, row=1, padx=10, pady=5)

    # Create and place filename input
    ttk.Label(root, text="Enter the filename to save the data (e.g., output.csv):").grid(column=0, row=2, padx=10, pady=5)
    filename_entry = ttk.Entry(root, width=40)
    filename_entry.grid(column=0, row=3, padx=10, pady=5)

    # Add a label to inform the user that the file will be saved in the Downloads directory
    ttk.Label(root, text="Note: The file will be saved in the Downloads directory.").grid(column=0, row=4, padx=10, pady=5)

    # Create and place submit button
    submit_button = ttk.Button(root, text="Run", command=lambda: run_scraper(url_entry, filename_entry))
    submit_button.grid(column=0, row=5, padx=10, pady=10)

    root.mainloop()

def test_write_to_downloads():
    try:
        downloads_path = str(Path.home() / "Downloads")
        test_file_path = os.path.join(downloads_path, "test_file.txt")
        with open(test_file_path, 'w') as test_file:
            test_file.write("This is a test file.")
        print(f"Test file created successfully at {test_file_path}")
    except Exception as e:
        print(f"An error occurred while writing the test file: {str(e)}")

test_write_to_downloads()

if __name__ == "__main__":
    main()
