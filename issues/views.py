from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.
def full_issue_info(request, pk):
	if request.method == 'GET':
		issue = Issue.objects.get(pk=pk)

		pieces = Piece.objects.filter(issue=issue)


		data = {}

		data['issue_title'] = issue.title
		data['publish_date'] = str(issue.publish_date)
		data['color'] = issue.color

		data['pieces_data'] = [p.to_dict() for p in pieces]

		return JsonResponse(json.dumps(data), safe=False)

	else: 
		return HttpResponse("this endpoint only responds to POST requests")