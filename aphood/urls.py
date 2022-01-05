from django.urls import path
from . import views
from .views import (HomePage,
                    ProfilePage,
                    CreateNewPost,
                    SinglePost,
                    CreateBusiness,
                    UpdateProfile,
                    BusinessPage)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'hood'

urlpatterns = [
                  path('', HomePage.as_view(), name='home'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)