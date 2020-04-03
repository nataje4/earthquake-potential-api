from issues import api


from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'author', api.AuthorViewSet)
router.register(r'issue', api.IssueViewSet)
router.register(r'piece', api.PieceViewSet)