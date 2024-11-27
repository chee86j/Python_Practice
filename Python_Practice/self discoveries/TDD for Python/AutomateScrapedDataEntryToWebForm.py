#   This demonstrates how to
# Step 3: Extract data from each row of the CSV file and automatically enter it into the corresponding fields on the web form.
# Step 4: Practice automating the form submission for multiple rows of data in the CSV file.

import csv
import time
from selenium import webdriver
# Function to fulfill the form
def fulfill_form(first, last, email, phone, zip, url):
    # Setting parameters for selenium to work
    path = r'chromedriver'  # make sure you insert the path to your driver here!
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(path, options=options)
    driver.get(url)

    # Find the input fields on the web form (Use correct IDs for your form)
    input_first = driver.find_element_by_id('form-first_name')
    input_last = driver.find_element_by_id('form-last_name')
    input_email = driver.find_element_by_id('form-email')
    input_phone = driver.find_element_by_id('form-phone')
    input_zip = driver.find_element_by_id('form-zip_code')

    submit = driver.find_element_by_name('commit')

    # Fill out the form
    driver.delete_all_cookies()
    input_first.send_keys(first)
    time.sleep(1)
    input_last.send_keys(last)
    time.sleep(1)
    input_email.send_keys(email)
    time.sleep(1)
    input_phone.send_keys(phone)
    time.sleep(1)
    input_zip.send_keys(zip)
    time.sleep(1)
    submit.click()
    time.sleep(1)

    driver.close()

# Read data from CSV and automatically enter it into the form
def process_csv_and_submit_form(csv_file, url):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extract values from each row
            first = row['First']
            last = row['Last']
            email = row['Email']
            phone = row['Phone']
            zip_code = row['Zip']

            # Call the fulfill_form function for each row
            fulfill_form(first, last, email, phone, zip_code, url)
            time.sleep(2)  # Adjust the delay between submissions as needed

# Provide the path to the CSV file and the URL of the form
csv_file = 'path_to_your_file.csv'
url = 'https://example.com/form'  # replace with your actual form URL

# Start the process
process_csv_and_submit_form(csv_file, url)
