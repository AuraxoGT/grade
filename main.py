import cloudscraper

scraper = cloudscraper.create_scraper()
url = "https://www.manodienynas.lt/1/lt/ajax/popup/dplus_ratio_marks"

response = scraper.get(url)
print(response.text)  # Should return your grades
