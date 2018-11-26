#Setting up the route to pull information for your webscraper
# urllib is the dependency, request is the module, always remember dependency first, module next. urlopen is the function
from urllib.request import urlopen as uReq


# bs4 stands for Beautiful soup. Beautiful soup is the function.
from bs4 import BeautifulSoup as soup


# my_url is the variable for the webpage we want to pull from 
my_url = 'https://www.newegg.com/Apple-Laptops-Notebooks/BrandSubChat/ID-1759-32'


# when running uReq it will obtain the information from an area, it will download the webpage and this makes it a client. Store the client as a variable.
uClient = uReq(my_url)


# when you read the page it will dump the information and you may not be able to access it again, use a variable to store it.
page_html = uClient.read()
uClient.close()


# call BeautifulSoup to html parse it. Store it as a variable. 
page_soup = soup(page_html, "html.parser")


## use a function (this one we are using the findAll (remember camel case))
##in the function we are calling the first item(div)
##then we are inserting an object(class:item-container)
##this grabs each product
containers = page_soup.findall("div", {"class":"item-container"})

#Generating the File
##We want to generate a filename so that we have something to pull the data from. If we don't generate a file, then the data gets generated into the command prompt 
filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)


# the containers function filters for the information we want to extract and from where. We use the {} to capture objects. Although we cannot capture the physical item such as the literal picture we can capture the other elements such as title product name and such.
for container in containers:
    brand = container.a.img["title"]
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    container.findAll("li", {"class":"price-ship"})
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()
    
    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)
    
    f.write(brand + "," +product_name.replace(",", "|") + "," +shipping + "\n")
    
    
# close the file. If you do not you cannot open or create the file.
f.close()
    