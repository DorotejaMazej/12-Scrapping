from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

csv_file = open("email_list.csv", "w")
url = "https://scrapebook22.appspot.com/"
response = urlopen(url).read()
soup = BeautifulSoup(response)
print soup.html.head.title.string

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        email = person_soup.find("span", attrs={"class": "email"}).string
        full_name = person_soup.find("div", attrs={"class":"col-md-8"}).h1.string
        city = person_soup.find("span", attrs={"data-city": True}).string
        csv_file.write(full_name+ "," + email + "," + city + "\n\n\n")

csv_file.close()



