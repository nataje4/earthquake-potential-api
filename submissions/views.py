from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from submissions.forms import SubmissionForm
from submissions.models import Submission  
from rest_framework import viewsets
from submissions.serializers import SubmissionSerializer


from django.template import loader

# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubmissionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubmissionForm()

    template = loader.get_template('submissions/index.html')
    context = {'form': form}

    return HttpResponse(template.render(context, request))



def post_submission(request): 
    if request.method == 'POST': 
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

        print('you\'ve posted')
    else: 
        return HttpResponse("this endpoint only responds to POST requests")