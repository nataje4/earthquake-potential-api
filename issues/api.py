from issues.models import * 
from issues.serializers import * 
from rest_framework import viewsets, response
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.
class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class IssueViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.order_by('-publish_date')

@api_view(['GET'])
def full_issue_info(self, pk):
    issue = Issue.objects.get(pk=pk)
    pieces = Piece.objects.filter(issue=issue)
    data = {}
    data['issue_title'] = issue.title
    data['publish_date'] = str(issue.publish_date)
    data['color'] = issue.color
    data['pieces_data'] = [p.to_dict() for p in pieces]
    return response.Response(data)

class PieceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PieceSerializer
    queryset = Piece.objects.order_by('-position')

