from issues.models import * 
from issues.serializers import * 
from rest_framework import viewsets

# Create your views here.
class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class IssueViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()

class PieceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PieceSerializer
    queryset = Piece.objects.all()