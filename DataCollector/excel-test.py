from datetime import datetime, timedelta
from Entity.Database import update
from Entity.SymbolsDaily import SymbolsDaily
import requests
import pandas as pd
import time
import xlrd
import os

startTime = time.time()

dateRange = pd.date_range(start="2020-04-01", end="2020-04-30")

for currentDate in dateRange:
    link = f'http://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d={currentDate.year}{currentDate.month:02}{currentDate.day:02}&format=0'

    # print(link)
    response = requests.get(link)

    excelData = pd.read_excel(response.content, 0, 3)

    # output = open('test.xls', 'wb')
    # output.write(resp.content)
    # output.close()
    # f = pd.ExcelFile('test.xls')

    finalList = []
    for i in range((excelData.shape[0])):
        finalList.append(list(excelData.iloc[i, :]))

    print(f'Date:{currentDate} - Count:{len(finalList)}')
    mappedData = map(lambda x: SymbolsDaily(x, datetime.date(currentDate)).props(), finalList)
    # print([*gg])
    update([*mappedData])

endTime = time.time()
elapsedTime = endTime - startTime

print(elapsedTime)
print(timedelta(seconds=elapsedTime))
