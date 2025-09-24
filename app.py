import requests
from bs4 import BeautifulSoup

print("Hello user, please input your search query, the more accurate the better result, this can be name, author and lyrics.")

prompt = input("\nenter song query $ ").replace(" ", "%20")

url =  f"https://searx.bndkt.io/search?q=%22site%3Agenius.com%22%20{prompt}&language=all&time_range=&safesearch=0&categories=general"
response = requests.get(url, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

soup = BeautifulSoup(response.text, "html.parser")
songUrl = soup.find("article", class_="result").find("a", class_="url_header").get("href")

f = open("output.txt", "w")

response = requests.get(songUrl, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
soup = BeautifulSoup(response.text, "html.parser")

soup.find("div", "LyricsHeader__Container-sc-5e4b7146-1").decompose()

for br in soup.find_all('br'):
    br.replace_with("\n")

f.write(soup.find("div", class_="Lyrics__Container-sc-a49d8432-1").get_text())

print("lyrics outputted to \"output.txt\"")