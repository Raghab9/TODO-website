from django.urls import path

from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('complete/',complete,name='complete'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),

    path('update/<int:pk>',update,name='update'),
    path('delete/<int:pk>',delete,name='delete'),#home page delete button
    path('complete_/<int:pk>',complete_,name='complete_'),
    path('delete_all/',delete_all,name='delete_all'),
    path('complete_all/',complete_all,name='complete_all'),
    path('complete_deleteAll/',complete_deleteAll,name='complete_deleteAll'),
    path('crestore/<int:pk>',crestore,name='crestore'),
    path('crstoreall/',crstoreall,name='crstoreall'),
    path('cdelete/<int:pk>',cdelete,name='cdelete'),
    path('trestore/<int:pk>',trestore,name='trestore'),
    path('trestoreall/>',trestoreall,name='trestoreall'),
    path('tdeleteall/>',tdeleteall,name='tdeleteall'),
    path('tdelete/<int:pk>',tdelete,name='tdelete')
]
