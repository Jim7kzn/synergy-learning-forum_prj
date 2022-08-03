from django.urls import path, include
from rest_framework import routers
from api import views
from api.views import CheckboxViewSet

router = routers.DefaultRouter()
router.register('checkbox', CheckboxViewSet)
# router.register('cb', CheckboxViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('cbl/', views.checkbox_list, name='cbl'),
    # path('cbl/<int:pk>', views.checkbox_detail, name='cbd'),
    # path('cbcr/', views.checkbox_create, name='cbcr'),
    # path('cbup/<int:pk>', views.checkbox_update, name='cbup'),
    # path('cbdel/<int:pk>', views.checkbox_delete, name='cbdel'),
    # path('ul/', views.UserList.as_view(), name='ul'),
    path('data', views.DataView.as_view()),
]

