# Task №2. Create an easygui app to view holidays in different countries
import json
import requests
from easygui import *


def get_list_countries():
    # Create a list of countries where you can view holidays
    url = 'https://date.nager.at/api/v3/AvailableCountries'
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        countries_list = []
        for i in result:
            countries_list.append(f"{i['countryCode']} - {i['name']}")
        return countries_list


def get_holidays_for_country(year, country_code):
    # We write the holidays of the selected country in the
    url = f'https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}'
    response = requests.get(url)
    if response.status_code == 200:
        with open('holiday_days.txt', 'w') as file:
            result = response.json()
            holiday_list = []
            for i in result:
                holiday_list.append(f"{i['date']} - {i['name']}")
            res = json.dumps(holiday_list, indent=0)
            file.write(res)


def holidays_countries():
    # Customizing the graphical interface
    title = "Holidays in different countries"
    msg = "Want to see holidays in different countries?"
    reply = ynbox(msg, title)
    try:
        while True:
            if reply:
                msg_country = "Holidays of which country do you want to see?"
                choices = get_list_countries()
                choose_country = choicebox(msg_country, title, choices)

                if choose_country:
                    msg_year = "Holidays for which year do you want to see? Enter the year:"
                    enter_year = integerbox(msg_year, title, upperbound=2023)

                    if enter_year:
                        get_holidays_for_country(enter_year, choose_country[:2])
                        msg_holiday = f'Holidays in {enter_year} in {choose_country[5:]}'
                        with open('holiday_days.txt', 'r') as f:
                            answer = textbox(msg_holiday, title, text=f.read())

                        if answer:
                            continue
                        break

                    else:
                        break
                else:
                    break
            else:
                break
    except Exception as error:
        print(f'Oops, error! {error}')


if __name__ == "__main__":
    holidays_countries()

