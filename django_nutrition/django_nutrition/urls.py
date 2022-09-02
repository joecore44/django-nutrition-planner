from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from trainer import views as trainer_views
from website import views as website_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')), #sends the request to the website application's url.py
    path('customer/', include('customer.urls')),
    path('trainer/', include('trainer.urls')),
    path('profile/', trainer_views.profile, name='profile'),
    path('trainer/register', trainer_views.register, name='trainer-register'),
    path('login/', auth_views.LoginView.as_view(template_name='website/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='website/logout.html'),
         name='logout'),

    #path('trainer/profile', trainer_views.profile, name='trainer-profile'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)