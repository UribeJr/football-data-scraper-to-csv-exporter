# Football Data Scraper to CSV Converter
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/> <img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white"/>

## Interested in Football Analytics?

I've started my journey diving into football analytics and have created a sample python program that references https://understat.com/ to scrape single game shot data

## How To
- Import all necssary packages/modules `requests`, `pandas`, `BeautifulSoup`
- Go to https://understat.com/ and go to any match that you want specific shot data for. Match URL should look like the following `https://understat.com/match/{match-id}`
- Execute `data_scraping.py` and input the match-id

### Congratulations!
The program then scrapes the shot data from the match and converts each Home and Away's team data into a separate Data Frame. The Data Frame's are then export as separate CSV Files for reference.

### Data Frame:
![Screenshot 2024-09-13 at 11 18 58 AM](https://github.com/user-attachments/assets/e11b9531-b6ef-43c4-9d99-f878ab43d87f)

### CSV: 
![Screenshot 2024-09-13 at 11 21 52 AM](https://github.com/user-attachments/assets/1150bd33-c449-4b4d-b270-7a96aed3056d)
