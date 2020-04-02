from django.db import models


SUBMISSION_STATUS = (
	(0, 'Recieved'), 
	(1, 'Under Review'), 
	(2, 'Accepted'), 
	(3, 'Rejected')
	)

# Create your models here.
class Submission(models.Model): 
	submission_date = models.DateTimeField('date submitted')
	author_name = models.CharField(max_length=200)
	author_email = models.EmailField()
	cover_letter = models.TextField()
	submission_file = models.FileField(upload_to='uploads/%Y/%m/')
	editor_notes = models.TextField(blank=True, null=True)
	submission_status = models.CharField(max_length=10,choices=SUBMISSION_STATUS, default='Recieved')
