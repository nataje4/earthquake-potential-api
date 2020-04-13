from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from submissions import api


router = SimpleRouter()
router.register(r'submit', api.SubmissionViewSet)


urlpatterns = [
	url(r'^api/', include(router.urls))
]