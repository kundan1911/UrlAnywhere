from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    # path(endpointname,renderthisfunctionforresponse)
    path('hello',views.hw),
    path('',views.login_page),
    path('home',views.home_page),
    path('all-analytics',views.allAnalyticsPage),
     # the below is the path whose end point will be anything that is typed by the user on the url
    # the request for rendering will be send to a view function
    path("<slug:dynamicEndPnt>",views.redirect_view),
    path('redirect/<slug:dynamicEndPnt>',views.specificAnalytic)
   
]                                                                                                                                                                                      
                                                       