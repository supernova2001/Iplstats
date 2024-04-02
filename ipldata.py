import requests 
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://y20india.in/ipl-player-stats/#google_vignette"
url1 = "https://www.cricketworld.com/cricket/series/indian-premier-league-2023/stats/batting-most-runs/127579"
response = requests.get(url)
response1 = requests.get(url1)
html_content = response.content
html_content2 = response1.content

soup = BeautifulSoup(html_content,"html.parser")
soup1 = BeautifulSoup(html_content2,"html.parser")

print(soup1)
season_tables = soup.find_all("table", {"class": "orangPurleTbl"})

highestscore_tables = soup1.find_all("table",{"class": "rankingTable batting_highest_strikerate"})

wb = Workbook()
ws = wb.active

# Find all rows in the first table (assuming there's only one table)
rows = highestscore_tables[0].find_all('tr')

# Write table data to Excel
for i, row in enumerate(rows, start=1):  
    cells = row.find_all(['th', 'td'])
    for j, cell in enumerate(cells, start=1):
        # Extract text content from each cell
        cell_text = cell.get_text(strip=True)
        # Replace "-" with "0"
        cell_text = cell_text.replace("-", "0")
        # Push text content into Excel
        ws.cell(row=i, column=j, value=cell_text)

# Save the workbook
path = "second_table.xlsx"
wb.save(path)
