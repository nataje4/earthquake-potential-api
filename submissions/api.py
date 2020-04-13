from submissions.models import * 
from submissions.serializers import * 
from rest_framework import viewsets, response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.
class SubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()

    def create(self, request):
        data=request.data
        serializer = SubmissionSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

        print('you\'ve posted')

    def partial_update(self, request, pk):
        profile = self.get_object(pk)
        serializer = SubmissionSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=201)
        else:
            return response.Response(serializer.errors, status=403)