**Project Description**

This project is designed to scrape laptops for prices, rating and review count on Amazon. The data will be used to analyze the prices of laptops and their ratings and reviews.

**Installation Steps**

1. Install Python 3.x on your computer.
2. Clone the project repository from GitHub 
    ```git clone origin https://github.com/ericsoi/scrapyamazonlaptops.git```.
3. Open the terminal and navigate to the project directory.
    ```cd scrapyamazonlaptops
    ```
4. Create a virtual environment and activate it 
5. Install requirements
    ```pip install -r requirements.txt
    ```
6. Run the following command to start the scraper:
    
```python
    scrapy crawl laptopsspider -O output.csv
```

That's it! The scraper will start scraping laptops for prices, rating and review count on Amazon.
