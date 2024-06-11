# Web-Scraper-GUI-with-CSV-Export

<p>This project provides a simple yet effective tool to scrape data from any user-specified URL and save the extracted data into a CSV file. The application leverages the <code>requests</code> and <code>BeautifulSoup</code> libraries for web scraping, while the <code>Tkinter</code> library is used to create a user-friendly graphical interface. This tool is particularly useful for extracting tabular data from web pages and storing it in a structured format for further analysis.</p>

<p>Here's a brief breakdown of the program:</p>

1. <b>User-Friendly Interface</b>: Easy-to-use GUI for inputting the URL and specifying the output file name.
2. <b>Data Extraction</b>: Efficient scraping of table data from web pages.
3. <b>CSV Export</b>: Saves the extracted data into a CSV file in the Downloads directory.
4. <b>Error Handling</b>: Robust error handling with user notifications for common issues like invalid URLs or missing tables.
5. <b>Cross-Platform</b>: Compatible with Windows, macOS, and Linux.

# Install the Package

## pip install requests beautifulsoup4 pandas
<p>In the terminal of the Python environment.</p>

# Usage

<p>1. <b>Run the Application</b>:</p>
<pre><code>python Webscraper.py</code></pre>

<p>or install and run the exe version on release section of this respository</p>

<p>2. <b>Enter Details</b>:</p>
<ul>
    <li>Input the URL you wish to scrape data from.</li>
    <li>Specify the desired filename for the output CSV (e.g., output.csv).</li>
</ul>

<p>3. <b>Save Data</b>:</p>
<ul>
    <li>Click "Run" to start the scraping process.</li>
    <li>The data will be saved in the Downloads directory, and a success message will be displayed upon completion.</li>
</ul>

# Contributor

<p>Lawrence Menegus</p>

# License

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
