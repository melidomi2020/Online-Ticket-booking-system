from django.urls  import path
from .views import ticket_detail
from .views import ticket_no

urlpatterns=[
    path('',ticket_detail,name='ticket_detail'),
    path('information/',ticket_no,name='ticket_no'),
]