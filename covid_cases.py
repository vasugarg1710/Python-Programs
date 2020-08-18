import requests
from bs4 import BeautifulSoup
from plyer import notification

def notification2(title,msg,time_out,icon):
    notification.notify(
        title=title,
        message=msg,
        app_icon=icon,  # e.g. 'C:\\icon_32x32.ico'
        timeout=time_out,  # seconds
    )

url = "https://www.mygov.in/corona-data/covid19-statewise-status/"
r = requests.get(url)
content = r.text
# print(content)
soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())
mydivs = soup.findAll("div", {"class": "field-item even"})
final_list = []
for div in mydivs:
    final_list.append(list(div))

Passenger_screened_on_Airport = final_list[1][0]
Active_Cases = final_list[2][0]
Cured_Discharged = final_list[3][0]
Migrated = final_list[4][0]
Deaths = final_list[5][0]
# print(Passenger_screened_on_Airport,Active_Cases,Cured_Discharged,Migrated,Deaths)
notification2("Covid-19 Cases",f"Passenger screened on Airport - {Passenger_screened_on_Airport} , Active cases - {Active_Cases} , Cured/Discharge - {Cured_Discharged} , Migrated - {Migrated} , Deaths - {Deaths} ",20, "icon.ico")

