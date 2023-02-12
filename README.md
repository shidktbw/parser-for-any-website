# Web Scrape

It's set up like this. 
> 1. If the site has no security, the parser can easily output the information you need without any extra stuff.
> 2. If the site does have protection, the parser will work through the browser.

## You have to change in the code 
> 1. headers = {'User-Agent': 'your user-agent'}
> 2. driver = webdriver.Edge() (optional. It is possible to change the browser to any)


## Prerequisites
· Python 3
· requests library
· beautifulsoup4 library
· selenium library
· Edge web browser (if using the web driver)

## Built With
Python 3 - The programming language used
requests library - To make HTTP requests
BeautifulSoup4 library - To extract and format text from HTML
Selenium library - To automate web browsing using a web driver

## Running the script
Simply run the script using the command line:

```python parser.py```
