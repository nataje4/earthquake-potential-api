from django.shortcuts import render
from django.http import HttpResponse
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


class SubmissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
