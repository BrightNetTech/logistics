from django.urls import path
from faster import views
app_name="faster"

urlpatterns = [
    path('', views.Home, name='Home'),
    path('About', views.About, name="About"),
    path('Base', views.Base, name="Base"),
    path('Blog', views.Blog, name="Blog"),
    path('Contact', views.Contact, name="Contact"),
    path('Price', views.Price, name="Price"),
    path('Service', views.Service, name="Service"),
    path('Single', views.Single, name="Single"),
    path('Tracking', views.Tracking, name="Tracking"),
    path('Team', views.Team, name="Team"),
    path('Account', views.Account, name="Account"),
    path('Thankyou', views.Thankyou, name="Thankyou"),
]