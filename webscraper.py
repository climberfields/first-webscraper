# urllib is the dependency, request is the module, always remember dependency first, module next. urlopen is the function
from urllib.request import urlopen as uReq
# bs4 stands for Beautiful soup. Beautiful soup is the function.
from bs4 import BeautifulSoup as soup
# my_url is the variable
my_url = 'https://www.newegg.com/Apple-Laptops-Notebooks/BrandSubChat/ID-1759-32'
# when running uReq it will obtain the information from an area, it will download the webpage and this makes it a client. Store the client as a variable.
uClient = uReq(my_url)
# when you read the page it will dump the information and you may not be able to access it again, use a variable to store it.
page_html = uClient.read()
uClient.close()
# call BeautifulSoup to html parse it. Store it as a variable. 
page_soup = soup(page_html, "html.parser")
# use a function (this one we are using the findAll (remember camel case))
#in the function we are calling the first item(div)
#then we are inserting an object(class:item-container)
#this grabs each product
containers = page_soup.findall("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)