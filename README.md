# Business Leads Scraper

This project is a Python-based web scraper that extracts business listing information from a directory-style website and exports the results into an Excel spreadsheet.

The goal of this project is to demonstrate how web scraping can be used for lead generation and market research.

## Features

* Scrapes business names
* Extracts website links
* Collects business categories
* Exports data into Excel

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* OpenPyXL

## Installation

Clone the repository:

```
git clone https://github.com/ExcelsKennedy2/Business-Leads-Scraper.git
```

Navigate to the project folder:

```
cd business-leads-scraper
```

Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the script:

```
python scraper.py
```

After running the script, an Excel file will be generated:

```
business_leads.xlsx
```

This file contains the scraped business listing data.

## Example Output

| Business Name | Category | Website      | Location |
| ------------- | -------- | ------------ | -------- |
| Example Store | Retail   | website link | Online   |

## Learning Objectives

This project demonstrates:

* Extracting structured data from listing pages
* Organizing scraped data using Pandas
* Exporting data to Excel
* Basic lead generation scraping

## Disclaimer

This project is for educational purposes only. Always ensure that you respect the terms of service of websites before scraping their data.
