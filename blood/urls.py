from django.contrib import admin
from django.urls import path,include
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls')),
    path('home/', include('application.urls')),
    path('about/', include('application.urls')),
    path('doctors/', include('application.urls')),
    path('blog/', include('application.urls')),
    path('contact/', include('application.urls')),
    path('login/', include('application.urls')),
    path('logout/', include('application.urls')),
    path('logincode/', include('application.urls')),
    path('registercode/', include('application.urls')),
    path('user/', include('application.urls')),
    path('admin1/', include('application.urls')),
    path('addblood/', include('application.urls')),
    path('addbloodcode/', include('application.urls')),
    path('showblood/', include('application.urls')),
    path('deleteblood/', include('application.urls')),
	path('addcamp/', include('application.urls')),
    path('addcampcode/', include('application.urls')),
	path('showcamp/', include('application.urls')),
    path('deletecamp/', include('application.urls')),
	path('showuser/', include('application.urls')),
	path('u_showblood/', include('application.urls')),
	path('bloodrequest/', include('application.urls')),
	path('myrequest/', include('application.urls')),
    path('deletemyrequest/', include('application.urls')),
    path('u_showcamp/', include('application.urls')),
    path('changepwd/', include('application.urls')),
    path('mypassword/', include('application.urls')),
    path('showrequest/', include('application.urls')),
]