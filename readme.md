**Project Description**

This project is designed to scrape items for prices, ratings, and review counts on Amazon. The data will be used to analyze the prices of items and their ratings and reviews.

**Installation Steps**

1. Install Python 3.x on your computer.
2. Clone the project repository from GitHub 
    ```python
        git clone origin https://github.com/ericsoi/scrapyamazonitems.git```.
3. Open the terminal and navigate to the project directory.
    ```python
        cd scrapyamazonitems
    ```
4. Create a virtual environment and activate it 
5. Install requirements
    ```python
        pip install -r requirements.txt
    ```
6. Run the following command to start the scraper:
    
```python
    scrapy crawl laptopsspider -O output.csv
```
