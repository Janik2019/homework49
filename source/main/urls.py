"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('webapp.urls'))
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', IndexView.as_view(), name='index'),
#     path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
#     path('task/add/', TaskCreateView.as_view(), name='task_add'),
#     path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
#     path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
#     path('types/', TypeView.as_view(), name='type'),
#     path('types/add/', TypeCreateView.as_view(), name='type_add'),
#     path('types/update/<int:pk>/', TypeUpdateView.as_view(), name='type_update'),
#     path('types/delete/<int:pk>/', TypeDeleteView.as_view(), name='type_delete'),
#     path('statuses/', StatusView.as_view(), name='status'),
#     path('statuses/add/', StatusCreateView.as_view(), name='status_add'),
#     path('statuses/update/<int:pk>/', StatusUpdateView.as_view(), name='status_update'),
#     path('statuses/delete/<int:pk>/', StatusDeleteView.as_view(), name='status_delete'),
#     path('projects/', ProjectIndex.as_view(), name='project'),
#     path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
#     path('project/add/', ProjectCreateView.as_view(), name='project_add'),
#     path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
#     path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
# ]
