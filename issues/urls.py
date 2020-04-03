from issues import api

from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'author', api.AuthorViewSet)
router.register(r'issue', api.IssueViewSet)
router.register(r'piece', api.PieceViewSet)

urlpatterns = [
	url(r'^api/', include(router.urls))
	]