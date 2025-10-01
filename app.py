import requests
from bs4 import BeautifulSoup

testing = False

def getLyrics(prompt):
    # create the url for get request and fire said request
    url =  f"https://searx.bndkt.io/search?q=%22site%3Agenius.com%22%20{prompt}%20lyrics&language=all&time_range=&safesearch=0&categories=general"
    response = requests.get(url, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

    # process the raw html with soup so it can be easily modified and selected
    soup = BeautifulSoup(response.text, "html.parser")
    songUrl = soup.find("article", class_="result").find("a", class_="url_header").get("href")

    print(f"\nUrl found. Loading content from {songUrl} ...")

    # get html and process it with soup
    response = requests.get(songUrl, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    soup = BeautifulSoup(response.text, "html.parser")

    # remove header from lyrics
    soup.find("div", {"data-exclude-from-selection": "true"}).decompose()

    # replace all the brs with new line characters so its more readable in the output
    for br in soup.find_all('br'):
        br.replace_with("\n")

    # organise all lyrics into a string
    output = ""
    for verse in soup.find_all("div", {"data-lyrics-container": "true"}):
        output += verse.get_text()

    return output


def main():
    print("\nHello user, please input your search query, the more accurate the better result, this can be name, author and lyrics.")

    # get the search prompt and format it for the search engine
    prompt = input("\nenter song query $ ").replace(" ", "%20")

    output = getLyrics(prompt)

    # output the lyrics to output.txt
    f = open("output.txt", "w")
    f.write(output)
    f.close()

    print("\nlyrics outputted to \"output.txt\" in active directory")

if testing == False:
    main()
