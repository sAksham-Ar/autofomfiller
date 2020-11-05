import urllib,urllib.request
from datetime import date
import random
today = date.today()
data = "" #Text you have to fill in the form. You can also read a file and fill its content in a google form.
num=random.randint(5,10)
url="https://docs.google.com/forms/d/e/1FAIpQLSdNN3reQre0R6BL4CchFjm20SmujvXPDN15M_rBPwhe1ZkUhw/formResponse"
 #URL to the form you want to fill. FormResponse should be used instead of ViewForm
urlout="https://docs.google.com/forms/d/e/1FAIpQLSdNN3reQre0R6BL4CchFjm20SmujvXPDN15M_rBPwhe1ZkUhw/viewform?"
text_entry_field={'entry.1489767559':num,'emailAddress':"",'entry.271596398_year':today.year,'entry.271596398_month':today.month,'entry.271596398_day':today.day,'entry.868228904':"",'entry.1867348459':"",'entry.1405267709':""} #Specify the Field Name here

"""
Hop to your form page, and click Responses > Get pre-filled URL. It'll ask you to do a sample fill-out of your form. I'd suggest putting in responses that easily let you see what question you're answering. Once you hit submit, it's going to give you a URL in the form of...
https://docs.google.com/forms/d/<form_id>/viewform?entry.XXXXXXX=____&entry.YYYYYY=____...
Now, change viewform to formResponse within the URL.
"""

try:
	dataenc=urllib.parse.urlencode(text_entry_field).encode('utf_8')
	print(urlout+str(dataenc)[2:-1])
except Exception as e:
	print(e)
