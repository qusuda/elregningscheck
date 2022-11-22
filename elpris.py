# Import library for fetching Elspot data
from nordpool import elspot
from pprint import pprint
from pyeloverblik import Eloverblik
from datetime import datetime
from datetime import timedelta
import json
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta

verbose = False

# Token and meetering point
REFRESH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlblR5cGUiOiJDdXN0b21lckFQSV9SZWZyZXNoIiwidG9rZW5pZCI6IjZmNjNlNTUzLWNkNDItNDU3Yi1iYWEzLWFiN2I2MjAyMmVmNyIsIndlYkFwcCI6WyJDdXN0b21lckFwaSIsIkN1c3RvbWVyQXBwQXBpIl0sInZlcnNpb24iOiIyIiwiaWRlbnRpdHlUb2tlbiI6IlYzWXh1SVZhemE0U0loT1dqVkZtK2lRQ1lQaURzYzZVL2wvMnFLam1nNkJ1Yk16VFY5MWNlbzFpQms0NlZDSXF0blJlWXorekk2Wjdibit2UjlNd04xK0VCTVJsaVhPNUoyNmNHY0JKRm1TTFJjcWxHdGpmZFhqR0Z0bHdzL0JySWRpeFJqWDBmTDM0dldYdXRaR2VtcGRjNC9ORG1iNUNpMURWQlBpTG4wOGhyOVczTDgvdmY4ODVRdzRFRFh2K0JPTkk0Rjg5Y3MzdmkyWEt3N0VSUk94NXFSVWptb2NUT0w3VGUvYjAxN0xsQVhUQ0Z1dE4rVG85MWV3R0R2ampTNTZRZ2FBU0xLK2dKNngyTXlZY3lPVmtCOUNQUVZiZGRYbmhKSThhUE8vM29BSS8xTWplWjl5b2xRWkNWTTNKUUxhcVJNSjA5RUgxUE5Id0VhcVN0S29yUDVGTHlPRzljVWFjRWQvVDIyMnhjMlJZWWs0cFZsbC9nb1BXZ0hYbHVpTmxteGV2MkhtSEM0d0h0VFRKS291YnZDRVR3bUpFM0cveVM3R20rSTdqdnhzRGh4eXc4MUdvd2laY2tOTGx1bXplMkxqMlAweExLQnhYNlEzYVJHdGtVU3ozWEM3SWYwZ0lHeEhMZVRqVk4wcXF4VkdnRXBrTlJ1Q3laSHl1WlUxNVdNdGJpR0wxeDlkRkpabU5Taytwa2RxUExRdStpbUZLYVp6YUFicWRtaU1EaEd0Y1FwSDlQbEY3UzI3RE5EYWQ5T0tudXVkK2FoSVIvYkRhOW5ZRVQzK2NqNnBqQS9UUTRMek1UQWh6blVoblFVOVRvM3N0emk1OHROR3hzbnUyNkpUSnhncVlTUUhyb2xnbWdRcFMyRER2dHRxayt6b2lsNFMwdGhiRjF0d05paVRjZExoVjJTZnVDcTNOR2dwVG9QQkk4NUVZeUoxQ0UxZ1V4Vm84Q3ZXMENaVHQzNWt4K2x3b0NMck0veFVMa2tHaSt0Q3FrUW0rWmV1eXc1alJXbVNHK2l5Qzl6NENLVWdjbWk1aGI4NmNBeTRJN2tqckQ5dS9wV2paS0VwUElXVHEzZ2U5K25QYUlYaDRNTkpPdUJBM0MzLzJzRUNKcEFvV0d1QXBHRUl6UWVmdGhCTmo3c0tpdEVkN2l6Y0ZaZGNFd0dqRHZ4czVpUWNoNm51N09xTk1hVGYrc2g3UUNDYmRRb0gyQTVyVDRyR2JjN1kyTitGazZwS3ZYMHhoWnJNZUpXbEw3VlR2d2JQeDJnQkJHV0Vlb2J2VVBWbnlrV25JeGN1QWZoN2lhc29rSWJ6bkN4ZDJmR2RxVldxejlIN0dLS2JWSjc0VkwxUW1xNnh3ajh0S3VFVDhNSUJzMWVCbytvOTAwYUc3SmQ2dHgxQ3hGc09sREhaazh6UFk5eVN0NVhsNFF5NkYvTW00VnJrdHdwMGEzM050SmZUYXU5SEFIc1IyTG9MMXRCYW0yeTFjZ3ppUEtjZWFxbXo3NVB5ODVHdHdxcEZsUDl5dTErZHBzZExIYjZVd2ZKREczaVdiaTRNeTA1V3dWLzlTelRkTitpNVQvTGxxNzRLTldUYjRsbkJhSklPWWt1UEJPNTd1YXZ3OU5xemJVSjRaUW55VW5vYmliSEtkblZaaXhDVUNBeVJ1MDIrL21weWdWd2QvUm5TTTdSQURhbHFneDBVWUZlYTFYZ1NDaklRV3VtdDczUjA1YWlJSDRZK1dSMERFdTdBK0YrR3VDODM5NlR0UExWME91Nncwald3bEFzN3ZDWTlZbXNuei9tT3hmemIrYmFONStsenlmazlDaWVXUEpjd0ZXNEZ4SlpKeHVQM3pLL05oamZlRStKdzIvTVl0V2t4NVhDTnljOEsxQlFYWU1UaTIwdEQ4dU42bTQrbndmUFRrZVlRcEp2NGZjUzVrRVZsM2JBK1FPaU9FTmVzVStGSHlNZGlBZXd6SUkvMzFuTjJ2TmVtTGFxWnJNcnhkSE9FM0Q5eGFYbkhUd1lsVmlsc1VabkpLelJQNlBzWEwyM09FaDJubmx2QzdUeks3U1h0UEFTdzR5S2dMVWJ4dFBSWXl3RjYyWXQvdHJVMzJob1lJODZ0eXMwK1g1bW5UbjdWQjFNYVRaem9hNU1PUjRYN1FVSEU4V0RyN0RYS2lta2hQdkRvcFA2UUR4Nk9qOTFINm5QVFQxVGZHRWM5SFdkSy9Zc205dUNSZnZLcTgrSGNWaGNNc1hYQlZnQ0FZNTF6U08rSlZkK3NwbkluNEZZMmhiU0F6TGUyVzhKdHpTZnJPUCtyUTZBci9TbnlMLzFiUm53SDRFNzBpVFJMTThWNU9UT1FHTW0vbHJZTU0veFBYMVdJWW5XTWNaV0h1ZE1XNGY2TE9JeUpQYklaRUNiSWtIWVhZNUJCRUVwTkFQMGF3OVBEVWdDK2FCNFlhYlhobEFoTEo4SHJ4MU9ZSkNCWUVOMGx2QXJ5dS9DNk5wd0VIaUhoZUJIb3FWNmtheTZIUkZNZVNCNk9SdW9aVWtzS05MaGZIeEI2NCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWVpZGVudGlmaWVyIjoiUElEOjkyMDgtMjAwMi0yLTI0MjA3NzA5NTMwNiIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2dpdmVubmFtZSI6IkFuZGVycyBFc2JlbnNlbiIsImxvZ2luVHlwZSI6IktleUNhcmQiLCJwaWQiOiI5MjA4LTIwMDItMi0yNDIwNzcwOTUzMDYiLCJiM2YiOiJxQzYydTJ2aG0yYlhrY1c2anVEczJpaXowekdlbnh6bHdqaGtnNjBidzJVPSIsInVzZXJJZCI6IjExODQ5MyIsImV4cCI6MTY5ODM0OTExOCwiaXNzIjoiRW5lcmdpbmV0IiwianRpIjoiNmY2M2U1NTMtY2Q0Mi00NTdiLWJhYTMtYWI3YjYyMDIyZWY3IiwidG9rZW5OYW1lIjoiUHl0aG9uIiwiYXVkIjoiRW5lcmdpbmV0In0.gyFADIPrT_1hdYi7qVEvsTFXzD9f2M2bpidEQR2eTGQ"
METERING_POINT = "571313104402775569"

# Initialize class for fetching Elspot prices
prices_elspot = elspot.Prices()

# Fetch hourly Elspot prices for DK1 and print the resulting dictionary
#Elafgift 965 kWh à 0,7630 kr./kWh 736,05 kr.
#Nettarif C 965 kWh à 0,2849 kr./kWh 274,83 kr.
#Rabat på nettarif N1 A/S 965 kWh à -0,0202 kr./kWh -19,49 kr.
#Tariffer, skatter og afgifter 965 kWh à 0,1123 kr./kWh


VAT = 0.25 
tarif_h = 28.49 - 2.02  #101.6
tarif_l = tarif_h #31 #40.8

tarif = [tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_l,tarif_h,tarif_h,tarif_h,tarif_l,tarif_l,tarif_l,tarif_l] # Øre
tax = 76.3 #83.2 # Øre
tax2 = 11.23
currency = 744 # Øre pr Euro

hours = range(0,24)

# Date loop
date_start = datetime(2022, 7, 1)
date_end = date_start + relativedelta(months=3)
#d = date_start
# delta time
delta = timedelta(days=1)
date = date_start

print("Periode {} -> {}".format(date_start, date_end))

day_prices = [] 
day_kwhs = []
days = []
day = 1

while(date < date_end):
    print("Request spot prices for {}...". format(date))
    prices_spot = prices_elspot.hourly(end_date=date, areas=['DK1'])

    if verbose:
        pprint(prices_spot)

    # Filter out values
    prices = prices_spot['areas']['DK1']['values']

    price_data = []
    for i in prices:
        price_data.append(
        float(i['value']))

    if verbose:
        print(price_data)

    #plt.bar(hours, price_data)
    #plt.title("Rå elpris timepris EUR/MWh excl. moms")
    ##plt.show()

    print("Request consumption from Eloverblik...")

    client = Eloverblik(REFRESH_TOKEN)
    cons = client.get_time_series(METERING_POINT, from_date=date-timedelta(days=1), to_date=date, aggregation='Hour')

    if verbose:
        print(cons.body)

    # Load result into json object
    response = json.loads(cons.body)

    # Locate data points  
    point = response["result"][0]["MyEnergyData_MarketDocument"]["TimeSeries"][0]["Period"][0]["Point"]

    # Convert into list
    metering_data = []
    for i in point:
        metering_data.append(
        float(i['out_Quantity.quantity']))

    if verbose:
        print(metering_data)

    #plt.bar(hours, metering_data)
    #plt.title("Forbrug kWh pr. time ({})".format(date))
    #plt.show()


    print("Calculate...")
    # Calculate total pric for given  day
    #day_price_sum = 0.0
    #day_kwh_sum = 0.0
    hour_prices = []
    hour_prices_kwh = []
    day_kwh = 0.0
    day_price = 0.0

    for h in range(0,24):
        # Calculate price in øre
        price_kwh = (tarif[h] + tax + tax2 + price_data[h]*currency/(1000))*(1+VAT)
        hour_prices_kwh.append(price_kwh) 
        hour_prices.append(price_kwh * metering_data[h])
        day_kwh = day_kwh + metering_data[h]
        day_price = day_price + price_kwh * metering_data[h]

    #period_price_sum = period_price_sum + day_price
    #period_kwh_sum = period_kwh_sum + day_kwh

    print("Forbrug {:.2f}kWh pris {:.2f} DKK ".format(day_kwh, day_price/100))

    #plt.bar(hours, hour_price)
    #plt.title("Time priser Øre/KWH incl afgift tarif og moms ({})".format(date.strftime("%x")))
    #plt.show()

    #plt.bar(hours, price_hour_sum)
    #plt.title("Forbrugspris Øre/KWH incl afgift tarif og moms ({})".format(date.strftime("%x")))
    #plt.suptitle("Dagspris {:.2f} DKK".format(price_day_sum/100))
    #plt.show()

    if verbose:
        print(hour_prices)
        print("Pris for {0}  {1:.2f} DKK".format(date, day_price/100))
    

    day_prices.append(day_price/100)
    day_kwhs.append(day_kwh)
    days.append(day)
    day = day +1
    # Move on to next day
    date = date+timedelta(days=1)

plt.bar(days, day_prices)
plt.suptitle("Forbrugspris pr dag. incl. afgift tarif og moms ({}->{})".format(date_start.strftime("%x"), date_end.strftime("%x")))
plt.title("Total forbrug {0:.2f} kWh - Pris {1:.2f} DKK".format(sum(day_kwhs), sum(day_prices)))
plt.show()



#4518