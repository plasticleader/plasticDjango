"""strauss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]




from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout_then_login
# from material.frontend import urls as frontend_urls

urlpatterns = [
	url(r'cargueArchivos/', include('app.cargueArchivos.urls')),
    url(r'inicial/', include('app.inicial.urls')),
    # url(r'', include(frontend_urls)),
    # url(r'^$', include('app.cargueArchivos.urls',namespace='cargueArchivos')),
    url('admin/', admin.site.urls),
    url(r'^accounts/login/',login,{'template_name':'login.html'}, name='login'),
    # url(r'^',login,{'template_name':'login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)