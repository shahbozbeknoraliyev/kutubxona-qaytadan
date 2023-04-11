
from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bosh_sahifa/', bosh_sahifa),
    path('kitob/', kitoblar),
    path('muallif/', mualliflar),
    path('talaba/', talabalar),
    path('adminlar/', adminlar),
    path('record/', recordlar),
    path('bitta_talaba/<int:son>', bitta_talaba),
    path('bitta_kitob/<int:son>', bitta_kitob),
    path('bitta_record/<int:son>', bitta_record),
    path('bitta_muallif/<int:son>', bitta_muallif),
    path('talaba_edit/<int:son>', talaba_edit),
    path('record_edit/<int:son>', record_edit),
    path('kitob_edit/<int:son>', kitob_edit),
    path('kitob_ochir/<int:son>', kitob_ochir),
    path('muallif_ochir/<int:son>', muallif_ochir),
    path('muallif_edit/<int:son>', muallif_edit),
    path('', loginview),
    path('logout/', logoutview),
    path('register/', register),
]
