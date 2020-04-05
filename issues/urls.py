from issues import api, views

from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'author', api.AuthorViewSet)
router.register(r'issue', api.IssueViewSet)
router.register(r'piece', api.PieceViewSet)

urlpatterns = [
	url(r'^api/', include(router.urls)), 
	url(r'^info/(?P<pk>\d+)/$', views.full_issue_info, name='full_issue_info')
	]