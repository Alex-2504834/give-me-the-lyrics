import requests
from bs4 import BeautifulSoup

def getLyrics(prompt, source="genius"):
    # create the url for get request and fire said request
    if source == "genius":
        url =  f"https://searx.bndkt.io/search?q=%22site%3Agenius.com%22%20{prompt}%20lyrics&language=all&time_range=&safesearch=0&categories=general"
    elif source == "lyricadvisor":
        url =  f"https://searx.bndkt.io/search?q=%22site%3Astreetdirectory.com%22%20{prompt}&language=all&time_range=&safesearch=0&categories=general"
    
    response = requests.get(url, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

    # process the raw html with soup so it can be easily modified and selected
    soup = BeautifulSoup(response.text, "html.parser")

    # check for no results
    if soup.find("article", class_="result") == None:
        return "not found"

    # select the first result and get the url from it
    songUrl = soup.find("article", class_="result").find("a", class_="url_header").get("href")

    # get html and process it with soup
    response = requests.get(songUrl, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    soup = BeautifulSoup(response.text, "html.parser")

    if source == "genius":
        # check is valid lyrics
        if soup.find("div", {"data-lyrics-container": "true"}) is None:
            return "not found"
        
        # remove meta data header from lyrics
        soup.find("div", {"data-exclude-from-selection": "true"}).decompose()
        
        # replace all the brs with new line characters so its more readable in the output
        for br in soup.find_all("br"):
            br.replace_with("\n")
    
    elif source == "lyricadvisor":
        # check is valid lyrics
        if soup.find("div", {"id": "content_lyric_clean"}) is None:
            return "not found"
        
    # organise all lyrics into a string and return it
    output = ""
    if source == "genius":
        # genius has multiple divs for verses so we need to loop through them all
        for verse in soup.find_all("div", {"data-lyrics-container": "true"}):
            output += verse.get_text()
            
        return output
    elif source == "lyricadvisor":
        output = soup.find("div", {"id": "content_lyric_clean"}).text
        
        # Remove leading whitespace (including tabs) from each line
        output = "\n".join(line.lstrip() for line in output.splitlines())
        return output


def main():
    print("\nHello user, please input your search query, the more accurate the better result, this can be name, author and lyrics.")

    # get the search prompt and format it for the search engine
    prompt = requests.utils.quote(input("\nenter song query $ "))
    
    source = input("\nchoose a source 1.genius (more songs), 2.lyricadvisor (faster) $ ")

    if source == "1":
        source = "genius"
    elif source == "2":
        source = "lyricadvisor"

    output = getLyrics(prompt, source)
    #output = getLyrics(prompt, source="lyricadvisor")

    # output the lyrics to output.txt
    f = open("output.txt", "w")
    f.write(str(output))
    f.close()

    if output == "not found":
        print("\nno results found")
    else:
        print("\nlyrics outputted to \"output.txt\" in active directory")

if __name__ == '__main__':
    main()
