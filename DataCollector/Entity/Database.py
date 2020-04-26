from sqlalchemy import Table, MetaData, Column, Integer, create_engine, inspect
import urllib.parse
from sqlalchemy.orm import Session

connectionString = r'Driver={SQL Server};Server=.;Database=stock-test;Trusted_Connection=yes;'
engine = create_engine('mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(connectionString))

metaData = MetaData()
tradeTable = Table('trade', metaData,
                   Column('id', Integer, primary_key=True),
                   Column('Code', Integer),
                   Column('Open', Integer),
                   Column('Close', Integer),
                   Column('High', Integer),
                   Column('Low', Integer),
                   )

metaData.create_all(engine)

# engine.execute(t.insert(), {'id': 1, 'x': 5}, {'id': 2, 'x': 53}, {'id': 3, 'x': 15}, {'id': 4, 'x': 55},
#                {'id': 5, 'x': 48})

dataSession = Session(engine)
print(dataSession.query(tradeTable))

u1 = dataSession.query(tradeTable).all()
# u1 = s.query(t).filter(t.id==3).all()
print(u1)
