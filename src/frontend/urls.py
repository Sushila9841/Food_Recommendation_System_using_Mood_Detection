from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('about', About.as_view(), name='about'),
    path('footer', Footer.as_view(), name='footer'),
    path('contact', Contact.as_view(), name='contact'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('blog/<int:pk>', BlogView.as_view(), name='blog'),
    # path('load_more_blogs', load_more_blogs.as_view(), name="load_more_blogs"),
    path('camera', Camera.as_view(), name='camera'),
    path('questions', QuestionsView.as_view(), name='questions'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
