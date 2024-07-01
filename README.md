# globalFishingWatch
This repo was created in order to play around with Global Fishing Data API

Given a list of countries (by country code)

Output average number of loitering events per vessel by country


### To run application
- `pipenv lock` in terminal
- `pipenv install`
- Add `.env` file (reference .env_template)
- Run `main` file
  - Make changes to `COUNTRY_CODE_LIST` in config.py to analyze different countries


## Sample output

| Country Code | Vessel Sample Size | Avg Loitering Events by Ship |
|--------------|--------------------|------------------------------|
| GRC          | 50                 | 8.00                         |
| FRA          | 50                 | 171.00                       |
| USA          | 50                 | 230.00                       |
| SAU          | 50                 | 87.00                        |
| COL          | 50                 | 106.00                       |
| RUS          | 50                 | 604.00                       |
| JPN          | 50                 | 404.00                       |
| ARG          | 50                 | 325.00                       |
| AUS          | 50                 | 301.00                       |
| ETH          | 14                 | 17.00                        |
| BRA          | 50                 | 418.00                       |
