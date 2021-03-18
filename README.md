# Getting_Notification_For_Price_Drop-in_Flight
This Project includes an application which will notify whenever price will get dropped in flight ticket
In this project i used following modules
1. smtplib
2. requests
3. datetime
In this project i used following API
1. Sheety.co for getting data from google sheets and storing data to google sheet
2. Taquela api for getting flight information such as price and searching flight an all

how this project works
I created 2 google sheets 
in 1 st sheet i stored only places where i want to visit and their all time low price
and in 1st i am getting iata data from taquila api and storing to sheet using sheety api

then i created 2nd sheet in which i taking user data such as name is email id and all
and after that i will seach current price and all time low price if current price is lower than all time low price
then this application gonna send email via smtplib module

TO UNDERSTAND BETTER I WILL RECOMEND TO READ DOCUMENTATION OF ALL API AND MODULES
Sheety: https://sheety.co/
Taquila: https://tequila.kiwi.com/portal/docs/tequila_api/search_api
