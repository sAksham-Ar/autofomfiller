import urllib,urllib.request
from datetime import date
import random
today = date.today()
num=random.randint(5,10)
url="https://docs.google.com/forms/d/e/XXXXXXXXXXXXXXXXX/formResponse"
urlout="https://docs.google.com/forms/d/e/XXXXXXXXXXXXXXXXX/viewform?"
text_entry_field={'entry.1489767559':num,'emailAddress':"",'entry.271596398_year':today.year,'entry.271596398_month':today.month,'entry.271596398_day':today.day,'entry.868228904':"",'entry.1867348459':"",'entry.1405267709':""}

try:
	dataenc=urllib.parse.urlencode(text_entry_field).encode('utf_8')
	print(urlout+str(dataenc)[2:-1])
except Exception as e:
	print(e)
