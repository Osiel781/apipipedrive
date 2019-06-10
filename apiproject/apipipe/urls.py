from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('$',views.add_deal_html,name="add_deal_html"),
    path('(?P<pk>\d+)',views.delete_deal_html,name="delete_deal_html"),
    path('$/update_deal/',views.update_deal_html,name="update_deal_html"),

    path('$/addperson',views.add_person_html,name="add_person_html"),
    path('$/deleteperson/(?P<pk>\d+)',views.delete_person_html,name="delete_person_html"),
    path('$/update_person/',views.update_person_html,name="update_person_html"),


    path('$/addactivity',views.add_activity_html,name="add_activity_html"),
    path('$/deleteactivity/(?P<pk>\d+)',views.delete_activity_html,name="delete_activity_html"),
    path('$/update_activity/',views.update_activity_html,name="update_activity_html"),







]
