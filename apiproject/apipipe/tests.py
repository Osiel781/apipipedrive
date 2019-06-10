from django.test import TestCase
from api import ApiPipedrive
api = ApiPipedrive(api_base_url='https://osieltorres.pipedrive.com/')


# Create your tests here.

title = 'TEST UNITARIO DEAL'
value = '100'
currency = 'USD'
status = 'open'
api.add_deal(title=title,value=value,currency=currency,status=status)


name = 'TEST UNITARIO PERSON'
email = 'email@test.com'
phone = '77777777777'
api.add_person(name=name,email=email,phone=phone)


subject = 'TEST UNITARIO ACTIVIDAD'
type = 'call'
due_date = '2019-10-10'
api.add_activity(subject=subject,type=type,due_date=due_date)

"""OBTENER DEALS PARA VERIFICAR QUE SE INTRODUCIERON"""
api.get_deals()
api.get_activities()
api.get_persons()
