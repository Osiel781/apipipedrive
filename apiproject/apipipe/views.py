from django.shortcuts import render,redirect
from django.http import HttpResponse
from .api import ApiPipedrive
import dict_digger
from django.core.files.storage import FileSystemStorage
import base64
import os
import json
api = ApiPipedrive(api_base_url='https://osieltorres.pipedrive.com/')



def home(request):
    contador_deals = 0
    dict_deals = api.get_deals()


    list_deals_id = []
    list_deals_title = []
    list_deals_owner_name = []
    list_deals_value = []
    list_deals_add_time = []

    if(dict_deals['data'] == None):
        list=zip(list_deals_title,list_deals_owner_name,list_deals_value,list_deals_add_time,list_deals_id)
    else:

        for v in enumerate(dict_deals['data']):

            contador_deals = contador_deals+1



        for i in range(0,contador_deals):
            list_deals_id.append(dict_deals['data'][i]['id'])
            list_deals_title.append(dict_deals['data'][i]['title'])
            list_deals_owner_name.append(dict_deals['data'][i]['owner_name'])
            list_deals_value.append(dict_deals['data'][i]['value'])
            list_deals_add_time.append(dict_deals['data'][i]['add_time'])

        list=zip(list_deals_title,list_deals_owner_name,list_deals_value,list_deals_add_time,list_deals_id)





    contador_persons = 0
    dict_persons= api.get_persons()

    list_persons_id = []
    list_persons_name = []
    list_persons_email = []
    list_persons_phone = []
    if(dict_persons['data'] == None):
        list_persons=zip(list_persons_id,list_persons_name,list_persons_email,list_persons_phone)
    else:
        for v in enumerate(dict_persons['data']):

            contador_persons = contador_persons+1



        for i in range(0,contador_persons):
            list_persons_id.append(dict_persons['data'][i]['id'])
            list_persons_name.append(dict_persons['data'][i]['name'])
            list_persons_email.append(dict_persons['data'][i]['email'][0]['value'])
            list_persons_phone.append(dict_persons['data'][i]['phone'][0]['value'])


        list_persons=zip(list_persons_id,list_persons_name,list_persons_email,list_persons_phone)


    contador_activities = 0
    dict_activities= api.get_activities()

    list_activities_id = []
    list_activities_type = []
    list_activities_due = []
    list_activities_done = []
    if(dict_activities['data'] == None):
        list_activities=zip(list_activities_id,list_activities_type,list_activities_due,list_activities_done)
    else:
        for v in enumerate(dict_activities['data']):

            contador_activities = contador_activities+1



        for i in range(0,contador_activities):
            list_activities_id.append(dict_activities['data'][i]['id'])
            list_activities_type.append(dict_activities['data'][i]['type'])
            list_activities_due.append(dict_activities['data'][i]['due_date'])
            list_activities_done.append(dict_activities['data'][i]['done'])


        list_activities=zip(list_activities_id,list_activities_type,list_activities_due,list_activities_done)


    contador_files = 0
    dict_files= api.get_files()

    list_files_id = []
    list_files_name = []
    list_file_type = []
    list_file_add_time = []

    if(dict_files['data'] == None):
        list_files=zip(list_files_id,list_files_name,list_file_type,list_file_add_time)
    else:
        for v in enumerate(dict_files['data']):

            contador_files = contador_files+1



        for i in range(0,contador_files):
            list_files_id.append(dict_files['data'][i]['id'])
            list_files_name.append(dict_files['data'][i]['file_name'])
            list_file_type.append(dict_files['data'][i]['file_type'])
            list_file_add_time.append(dict_files['data'][i]['add_time'])



        list_files=zip(list_files_id,list_files_name,list_file_type,list_file_add_time)
    context = {'list_persons':list_persons,'contador_persons':contador_persons,'list':list,'contador_deals':contador_deals,'list_activities':list_activities,'contador_activities':contador_activities,'list_files':list_files,'contador_files':contador_files}


    return render(request,'crud.html',context=context)


def add_file_html(request):

    file = request.GET['file']
    deal_id = request.GET['deal_id']
    api.add_files_to_deal(deal_id=deal_id,file=file)

    return redirect('home')




def delete_deal_html(request,pk=None):
    if pk:
        api.delete_deal(pk)
    return redirect('home')



def add_deal_html(request):
    title = request.GET['title_deal']
    value = request.GET['value_deal']
    currency = request.GET['currency_deal']
    status = request.GET['status_deal']
    api.add_deal(title=title,value=value,currency=currency,status=status)
    return redirect('home')


def update_deal_html(request):
    id = request.GET['id_deal']
    title = request.GET['title_deal']
    value = request.GET['value_deal']
    currency = request.GET['currency_deal']
    status = request.GET['status_deal']
    api.update_deal(deal_id=id,title=title,value=value,currency=currency,status=status)
    return redirect('home')

def add_person_html(request):
    name = request.GET['name_person']
    email = request.GET['email_person']
    phone = request.GET['phone_person']

    api.add_person(name=name,email=email,phone=phone)
    return redirect('home')

def delete_person_html(request,pk=None):
    if pk:
        api.delete_person(pk)
    return redirect('home')

def update_person_html(request):
    data_id = request.GET['id_person']
    name = request.GET['name_person']
    email = request.GET['email_person']
    phone = request.GET['phone_person']
    api.update_person(data_id=data_id,name=name,email=email,phone=phone)
    return redirect('home')


def add_activity_html(request):
    subject = request.GET['subject_activity']
    type = request.GET['type_activity']
    due_date = request.GET['due_date_activity']

    api.add_activity(subject=subject,type=type,due_date=due_date)
    return redirect('home')

def delete_activity_html(request,pk=None):
    if pk:
        api.delete_activity(pk)
    return redirect('home')

def update_activity_html(request):
    activity_id = request.GET['id_activity']
    subject = request.GET['subject_activity']
    type = request.GET['type_activity']
    due_date = request.GET['due_date_activity']
    api.update_activity(activity_id=activity_id,subject=subject,type=type,due_date=due_date)
    return redirect('home')
