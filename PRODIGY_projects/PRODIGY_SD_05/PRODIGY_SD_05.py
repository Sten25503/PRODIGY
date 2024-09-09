import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Function to perform web scraping
def scrape_data():
    # Get search term from the user input
    search_term = search_entry.get()
    if not search_term:
        messagebox.showwarning("Input Error", "Please enter a search term.")
        return

    # Setup Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)

    # URL of the Flipkart search results page
    url = f"https://www.flipkart.com/search?q={search_term}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

    # Open the page using Selenium
    driver.get(url)

    # Allow the page to load
    time.sleep(10)

    # Extract product names, prices, and ratings
    product_names = []
    product_prices = []
    product_ratings = []

    products = driver.find_elements(By.CLASS_NAME, '_1AtVbE')

    for product in products:
        try:
            # Extract the product name
            name = product.find_element(By.CLASS_NAME, 'IRpwTa').text
        except:
            try:
                name = product.find_element(By.CLASS_NAME, '_4rR01T').text
            except:
                name = "No name"
        
        # Extract the product price
        try:
            price = product.find_element(By.CLASS_NAME, '_30jeq3').text
        except:
            price = "No price"

        # Extract the product rating
        try:
            rating = product.find_element(By.CLASS_NAME, '_3LWZlK').text
        except:
            rating = "No rating"

        product_names.append(name)
        product_prices.append(price)
        product_ratings.append(rating)

    # Store data in a DataFrame
    data = {
        'Product Name': product_names,
        'Price': product_prices,
        'Rating': product_ratings
    }
    df = pd.DataFrame(data)

    # Save data to CSV
    df.to_csv('flipkart_selenium_products.csv', index=False)

    # Close the browser
    driver.quit()

    messagebox.showinfo("Success", "Scraping completed. Data saved to 'flipkart_selenium_products.csv'.")

# Create the main window
root = tk.Tk()
root.title("Flipkart Product Scraper")

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, padx=10, pady=10)

search_label = ttk.Label(frame, text="Enter search term:")
search_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

search_entry = ttk.Entry(frame, width=40)
search_entry.grid(row=0, column=1, padx=5, pady=5)

scrape_button = ttk.Button(frame, text="Scrape Data", command=scrape_data)
scrape_button.grid(row=1, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
