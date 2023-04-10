# Task №3. Movie list parsing.
from time import sleep
from bs4 import BeautifulSoup
import requests
import pandas as pd


def movies_list():
    # The function parses information about movies

    movies = []

    try:
        for p in range(1, 48):  # Looping through all the movie pages
            # print(p)
            url = f'https://vip.x-film.sbs/istoricheskie/page/{p}/'
            response = requests.get(url)

            if response.status_code == 200:
                sleep(3)  # We put a pause so as not to overload the server with requests.
                # Get ready to wait a lo-o-o-ong time ))) about 3 minutes
                soup = BeautifulSoup(response.text, "html.parser")
                films = soup.find_all(class_='short clearfix with-mask')

                for film in films:
                    # Choose the information you need about the movie
                    movie_title = film.find('a', class_='short-title').text.split(' (')[0]
                    year_of_issue = film.find_all(class_='sd-line')[0].text.split('Гoд выпуcka: ')[1]
                    country = film.find_all(class_='sd-line')[3].text.split('Cтpaнa: ')[1]
                    description = film.find('div', class_='sd-line sd-text').text.split('Oпиcaниe: ')[1]
                    movies.append([movie_title, year_of_issue, country, description])
    except Exception as error:
        print(f'Oops, error! {error}')

    # Create DataFrame
    header = ['movie_title', 'year_of_issue', 'country', 'description']
    df = pd.DataFrame(movies, columns=header)
    df.to_csv('movies_data.csv', encoding='utf-8', index=False)

    print(f'File "movies_data.csv" was successfully written')


if __name__ == "__main__":
    movies_list()
