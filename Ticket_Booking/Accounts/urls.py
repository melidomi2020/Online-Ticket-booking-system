from django.urls  import path
from .views import SignUpView
from .views import homepage

urlpatterns=[
    path('signup/',SignUpView.as_view(),name='signup'),
    #path('userinformation/',user_info,name='user_info'),
    
    
]