from django.conf.urls  import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
