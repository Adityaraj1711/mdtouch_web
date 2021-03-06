# File: urls.py
# Description: This file contains the Django url statements.
# Author(s): Team Suites (1)

# imports
from django.conf.urls import url
from . import views
from django.urls import path

# url statements
app_name = 'MDTouch'
urlpatterns = [
    #url(r'^$',views.index, name='getstarted'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^event/',views.eventpage,name='event'),
    url(r'^appointments/eventdetail/(?P<event_id>[0-9]+)/', views.eventdetailview, name='eventdetail'),
    url(r'^search/hospitaldetail/(?P<hospital_id>[0-9]+)/', views.hospitaldetailview, name='hospitaldetail'),
    url(r'^gallery',views.servicepage,name='gallery'),
    url(r'^about',views.aboutpage,name='about'),
    url(r'^services',views.servicepage,name='services'),
    url(r'^register/$', views.registerP, name='registerP'),
    url(r'^register/create$', views.createPLogIn, name='createPLogIn'),
    url(r'^password/$', views.password, name='password'),
    url(r'^password/changepass/$', views.changePass, name='changepass'),
    url(r'^verify/$', views.verify, name='verify'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/registerDN$', views.registerDN, name='registerDN'),
    url(r'^home/registerDN/createDN$', views.createDNLogIn, name='createDNLogIn'),
    url(r'^information/$', views.information, name='information'),
    url(r'^information/updatePro$', views.updatePro, name='updatePro'),
    url(r'^information/updatePro/updateProInfo$', views.updateProInfo, name='updateProInfo'),
    url(r'^information/updateMed/(?P<pat_id>[0-9]+)/', views.updateMed, name='updateMed'),
    url(r'^information/updateMed/updateMedInfo/(?P<pat_id>[0-9]+)/', views.updateMedInfo, name='updateMedInfo'),
    url(r'^information/export$', views.export, name='export'),
    url(r'^information/tests/(?P<pat_id>[0-9]+)/', views.tests, name='tests'),
    url(r'^information/tests/createTest/(?P<pat_id>[0-9]+)/', views.createTest, name='createTest'),
    url(r'^information/tests/createTest/createTestInfo/(?P<pat_id>[0-9]+)/', views.createTestInfo, name='createTestInfo'),
    url(r'^information/tests/releaseTest/(?P<test_id>[0-9]+)/', views.releaseTest, name='releaseTest'),
    url(r'^information/testDetails/(?P<test_id>[0-9]+)/', views.testDetails, name='testDetails'),
    url(r'^information/discharge/(?P<pat_id>[0-9]+)/', views.discharge, name='discharge'),
    url(r'^information/admission/(?P<pat_id>[0-9]+)/(?P<emp_id>[0-9]+)/', views.admission, name='admission'),
    url(r'^information/transfer/(?P<pat_id>[0-9]+)/(?P<emp_id>[0-9]+)/', views.transfer, name='transfer'),
    url(r'^appointments/$', views.appointments, name='appointments'),
    url(r'^appointments/createAppt$', views.createAppt, name='createAppt'),
    url(r'^appointments/createAppt/createApptInfo$', views.createApptInfo, name="createApptInfo"),
    url(r'^appointments/updateAppt/(?P<appt_id>[0-9]+)/', views.updateAppt, name='updateAppt'),
    url(r'^appointments/updateAppt/updateApptInfo/(?P<appt_id>[0-9]+)/', views.updateApptInfo, name='updateApptInfo'),
    url(r'^appointments/cancelAppt/(?P<appt_id>[0-9]+)/', views.cancelAppt, name='cancelAppt'),
    url(r'^prescriptions/$', views.prescriptions, name='prescriptions'),
    url(r'^prescriptions/createPres$', views.createPres, name='createPres'),
    url(r'^prescriptions/createPres/createPresInfo$', views.createPresInfo, name="createPresInfo"),
    url(r'^prescriptions/updatePres/(?P<pres_id>[0-9]+)/', views.updatePres, name='updatePres'),
    url(r'^prescriptions/updatePres/updatePresInfo/(?P<pres_id>[0-9]+)/', views.updatePresInfo, name='updatePresInfo'),
    url(r'^prescriptions/removePres/(?P<pres_id>[0-9]+)/', views.removePres, name='removePres'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    #url(r'^messages/$', views.messages, name='messages'),
    #url(r'^messages/createMess/$', views.createMess, name='createMess'),
    #url(r'^messages/createMess/createMessInfo/(?P<mess_id>-1)/', views.createMessInfo, name="createMessInfo"),
    #url(r'^messages/replyMess/(?P<mess_id>[0-9]+)/', views.replyMess, name='replyMess'),
    #url(r'^messages/replyMess/createMessInfo/(?P<mess_id>[0-9]+)/', views.createMessInfo, name="createMessInfo"),
    #url(r'^messages/viewMess/(?P<mess_id>[0-9]+)/', views.viewMess, name='viewMess'),
    #url(r'^messages/deleteMess/(?P<mess_id>[0-9]+)/', views.deleteMess, name='deleteMess'),
    url(r'^log/$', views.log, name='log'),
    url(r'^statistics/$', views.statistics, name='statistics'),
    url(r'^logOut/$', views.logOut, name='logOut'),
    url(r'events/$',views.getevents,name='eventinview'),
    #url(r'searchfacilities/$', views.search_facilities, name='searchfacilities'),
    #url(r'^search/$', views.search2, name='sec'),
    url(r'^search/$', views.search, name='query'),
    url(r'^diseasesearch/$', views.diseasesearch, name='diseasequery'),

    ##########API#####################
    path('api/hospital/', views.HospitalList.as_view()),
    path('api/hospital/<int:pk>', views.HospitalDetail.as_view()),
    path('api/emergencycontact/', views.EmergencycontactList.as_view()),
    path('api/emergencycontact/<int:pk>', views.EmergencycontactDetail.as_view()),
    path('api/patient/', views.PatientList.as_view()),
    path('api/patient/<int:pk>', views.PatientDetail.as_view()),
    path('api/specialization/', views.SpecializationList.as_view()),
    path('api/specialization/<int:pk>', views.SpecializationDetail.as_view()),
    path('api/qualification/', views.QualificationList.as_view()),
    path('api/qualification/<int:pk>', views.QualificationDetail.as_view()),
    path('api/doctor/', views.DoctorList.as_view()),
    path('api/doctor/<int:pk>', views.DoctorDetail.as_view()),
    path('api/administrator/', views.AdministratorList.as_view()),
    path('api/administrator/<int:pk>', views.AdministratorDetail.as_view()),
    path('api/prescription/', views.PrescriptionList.as_view()),
    path('api/prescription/<int:pk>', views.PrescriptionDetail.as_view()),
    path('api/test/', views.TestList.as_view()),
    path('api/test/<int:pk>', views.TestDetail.as_view()),
    path('api/appointment/', views.AppointmentList.as_view()),
    path('api/appointment/<int:pk>', views.AppointmentDetail.as_view()),
    path('api/message/', views.MessageList.as_view()),
    path('api/message/<int:pk>', views.MessageDetail.as_view()),
    path('api/logininfo/', views.LogInInfoList.as_view()),
    path('api/logininfo/<int:pk>', views.LogInInfoDetail.as_view()),
    path('api/emergencyservice/', views.EmergencyServicesList.as_view()),
    path('api/emergencyservice/<int:pk>', views.EmergencyServiceDetail.as_view()),
    path('api/ambulance/', views.AmbulanceList.as_view()),
    path('api/ambulance/<int:pk>', views.AmbulanceDetail.as_view()),
    path('api/login/', views.LoginList.as_view()),
    path('api/login/<int:pk>', views.LoginDetail.as_view()),
    path('api/bloodbankcenter/', views.BloodBankCenterList.as_view()),
    path('api/bloodbankcenter/<int:pk>', views.BloodBankCenterDetail.as_view()),
    path('api/dispensaries/', views.DispensaryList.as_view()),
    path('api/dispensaries/<int:pk>', views.DispensaryDetail.as_view()),
    path('api/event/', views.EventList.as_view()),
    path('api/event/<int:pk>', views.EventDetail.as_view()),
    path('api/bloodbilling/', views.BloodBillingList.as_view()),
    path('api/bloodbilling/<int:pk>', views.BloodBillingDetail.as_view()),
    path('api/bloodwaste/', views.BloodWasteList.as_view()),
    path('api/bloodwaste/<int:pk>', views.BloodWasteDetail.as_view()),
    path('api/medicine/', views.MedicineList.as_view()),
    path('api/medicine/<int:pk>', views.MedicineDetail.as_view()),
    path('api/dispensarybilling/', views.DispensaryBillingList.as_view()),
    path('api/dispensarybilling/<int:pk>', views.DispensaryBillingDetail.as_view()),
    path('api/ambulancebilling/', views.AmbulanceBillingList.as_view()),
    path('api/ambulancebilling/<int:pk>', views.AmbulanceBillingDetail.as_view()),
    path('api/testcentre/', views.TestCentreList.as_view()),
    path('api/testcentre/<int:pk>', views.TestCentreDetail.as_view()),
    path('api/testservices/', views.TestServicesList.as_view()),
    path('api/testservices/<int:pk>', views.TestServiceDetail.as_view()),
    path('api/webcarousel/', views.webcarousel_list),
    path('api/webcarousel/<int:pk>', views.webcarousel_detail),
    path('api/notice/', views.NoticeList.as_view()),
    path('api/notice/<int:pk>', views.NoticeDetail.as_view()),
    path('api/ambulancerequest/', views.AmbulanceRequestList.as_view()),
    path('api/ambulancerequest/<int:pk>', views.AmbulanceRequestDetail.as_view()),
    path('api/broadcast/', views.BroadcastList.as_view()),
    path('api/broadcast/<int:pk>', views.BroadcastDetail.as_view()),
    path('api/facilities/', views.HospitalFacilitiesList.as_view()),
    path('api/facilities/<int:pk>', views.HospitalFacilitiesDetail.as_view()),
    path('api/bed/', views.BedList.as_view()),
    path('api/bed/<int:pk>', views.BedDetail.as_view()),
    path('api/bedBilling/', views.BedBillingtList.as_view()),
    path('api/bedbilling/<int:pk>', views.BedBillingDetail.as_view()),
    path('api/maintainencebed/', views.MaintainenceBedList.as_view()),
    path('api/maintainencebed/<int:pk>', views.MaintainenceBedDetail.as_view()),
    path('api/hospitalbilling/', views.HospitalBillingList.as_view()),
    path('api/hospitalbilling/<int:pk>', views.HospitalBillingDetail.as_view()),
    path('api/disease/', views.DiseaseList.as_view()),
    path('api/disease/<int:pk>', views.DiseaseDetail.as_view()),
    path('api/diseasesearch/', views.DiseaseSearchList.as_view()),
    path('api/diseasesearch/<int:pk>', views.DiseaseSearchDetail.as_view()),
    path('api/diseasecured/', views.DiseaseCuredList.as_view()),
    path('api/diseasecured/<int:pk>', views.DiseaseCuredDetail.as_view()),

    #url('^api/(?P<destination>.+)/$', views.AmbulanceBillingFilter.as_view()),

]
