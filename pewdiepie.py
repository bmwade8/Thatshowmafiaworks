import requests
import bs4

# TODO: This doesn't even work, Marcy
def get_pewdiepie_subs():
    url = requests.get("https://socialblade.com/youtube/user/pewdiepie%22")
    soup = bs4.BeautifulSoup(url.text, "html.parser")
    sub_count = soup.findAll('span', {"id": "youtube-stats-header-subs"})
    return sub_count[0].get_text()

