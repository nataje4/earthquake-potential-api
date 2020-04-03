from django.db import models

# Create your models here.

class Issue(models.Model): 
	publish_date=models.DateField('date submitted')
	title = models.CharField(max_length=200)
	color = models.CharField(max_length=7)


class Author(models.Model): 
	name = models.CharField(max_length=50)
	bio = models.TextField()
	website = models.URLField(null=True)
	twitter = models.URLField(null=True)
	instagram = models.URLField(null=True)
	facebook = models.URLField(null=True)

class Piece(models.Model): 
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
	position = models.IntegerField()
	text = models.TextField() 
	media_file = models.FileField(upload_to='issue_media/%Y/%m/')
	layout_type = models.CharField(max_length=20)
	# custom_css = models.CharField(max_length=200)


