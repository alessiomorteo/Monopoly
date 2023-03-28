import requests
from bs4 import BeautifulSoup

url = "https://www.nandos.co.uk/restaurants/all"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

restaurant_list = soup.find("ul", class_="nan-locations__list")
'''for restaurant in restaurant_list.find_all("div", class_="nan-rest-info"):
    title = restaurant.find("h3", class_="nan-rest-info__title").get_text()
    address = restaurant.find("div", class_="nan-rest-info__address")
    street_address = address.find("div", class_="address-1").get_text()
    postcode = address.find("span").get_text()
    phone = restaurant.find("a", class_="nan-rest-info__phone").get_text()

    print(title)
    print(street_address)
    print(postcode)
    print(phone)
    print("\n")'''
print(restaurant_list)
