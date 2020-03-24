
def check_build(champion):
    import requests
    from bs4 import BeautifulSoup
    url = "https://rankedboost.com/league-of-legends/build/{}/#item-build".format(champion)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    headers = soup.findAll("span", {"class": "rb-item-img-text obt-css"})
    return headers
