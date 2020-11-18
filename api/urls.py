from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, QuizViewSet, ResultViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('quizzes', QuizViewSet)
router.register('result', ResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
]
