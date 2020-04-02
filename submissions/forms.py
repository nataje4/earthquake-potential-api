from django.forms import ModelForm
from submissions.models import Submission

class SubmissionForm(ModelForm): 
	class Meta: 
		model = Submission 
		fields = ['author_name', 'author_email', 'cover_letter', 'submission_file']