import requests  
from bs4 import BeautifulSoup  
    
def getdata(url):  
    r = requests.get(url)  
    return r.text  
    
htmldata = getdata("https://www.google.com/")  
soup = BeautifulSoup(htmldata, 'html.parser')  
for item in soup.find_all('img'): 
    print(item['src'])

    '''
    This script will scrape all the images from a given URL using Python and Beautiful Soup library.
    '''