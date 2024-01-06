pip install requests beautifulsoup4


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_mobile_data(url):
    try:
        # Using headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
        }
        # Sending  GET request
        response = requests.get(url, headers=headers)
        # Checking if the response is successful (status code 200)
        response.raise_for_status()
        if response.status_code == 200:
         
            return BeautifulSoup(response.content, 'html.parser')
        else:
            print(f"Failed to fetch the page - Status Code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return None
    except Exception as ex:
        print(f"An error occurred: {ex}")
        return None

def scrape_flipkart_mobiles():
 
    product_name = []
    prices = []
    reviews = []
    description = []

    # Base URL 
    base_url = "https://www.flipkart.com/search?q=iPhone&page="

    for page_num in range(1, 10):
      
        url = base_url + str(page_num)
        e
        soup = get_mobile_data(url)
        
        if soup:
           
            names = soup.find_all("div", class_="_4rR01T")
            for name in names:
                product_name.append(name.text)

           
            price_elements = soup.find_all("div", class_="_30jeq3._1_WHN1")
            for price in price_elements:
                prices.append(price.text)

            desc_elements = soup.find_all("ul", class_="_1xgFaf")
            for desc in desc_elements:
                description.append(desc.text)

           
            review_elements = soup.find_all("div", class_="_3LWZlK")
            for review in review_elements:
                reviews.append(review.text)

        
            time.sleep(2)

    # Creating a DataFrame with the collected data
    df = pd.DataFrame({
        "Product Name": product_name,
        "Prices": prices,
        "Description": description,
        "Review": reviews
    })

    # Displaying the DataFrame in the console
    print(df)
    # Saving the DataFrame as a CSV file
    df.to_csv('/content/flipkart_iphones.csv', index=False)

if __name__ == "__main__":
    # Calling the function to start scraping Flipkart mobiles
    scrape_flipkart_mobiles()





   
