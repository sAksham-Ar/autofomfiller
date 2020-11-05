import urllib,urllib.request
from datetime import date
import random
today = date.today()
data = "" #Text you have to fill in the form. You can also read a file and fill its content in a google form.
name=["Bob"]
interest=["Cricket","IPL","Star Wars","Percy Jackson"]
mid=["He helped me with my assignments.","He helped me during tests.","He helped my in doing my lab reports."]
end=["Hope we can hangout again after the pandemic.","I hope we can have more fun after college reopens.","I wish that institute reopens soon so we can have more fun.","We will have more fun after we come back to college."]
grat="I am grateful for my friend "+name[0]+".We became friends in first year."+"We both love "+random.choice(interest)+".We both have lots of fun talking about it."+"I have fun hanging out with him."+random.choice(mid)+random.choice(end)
num=random.randint(5,10)
url="https://docs.google.com/forms/d/e/1FAIpQLSdNN3reQre0R6BL4CchFjm20SmujvXPDN15M_rBPwhe1ZkUhw/formResponse"
 #URL to the form you want to fill. FormResponse should be used instead of ViewForm
urlout="https://docs.google.com/forms/d/e/1FAIpQLSdNN3reQre0R6BL4CchFjm20SmujvXPDN15M_rBPwhe1ZkUhw/viewform?"
text_entry_field={'entry.1489767559':num,'emailAddress':"aryasaksham@gmail.com",'entry.271596398_year':today.year,'entry.271596398_month':today.month,'entry.271596398_day':today.day,'entry.868228904':"Saksham Arya",'entry.1867348459':"19CH10043",'entry.1405267709':grat} #Specify the Field Name here

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
