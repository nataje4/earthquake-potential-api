from django.db import models

# Create your models here.

class Issue(models.Model): 
	publish_date=models.DateField('date submitted')
	title = models.CharField(max_length=200)
	color = models.CharField(max_length=7)

	def __str__(self):
		return self.title


class Author(models.Model): 
	name = models.CharField(max_length=50)
	bio = models.TextField()
	website = models.URLField(null=True)
	twitter = models.URLField(null=True)
	instagram = models.URLField(null=True)
	facebook = models.URLField(null=True)

	def __str__(self):
		return self.name

class Piece(models.Model): 
	issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	position = models.IntegerField()
	title = models.CharField(max_length=200)
	text = models.TextField() 
	media_file = models.FileField(upload_to='issue_media/%Y/%m/', null=True, blank=True)
	layout_type = models.CharField(max_length=20)
	# custom_css = models.CharField(max_length=200)

	def to_dict(self): 
		data = {}

		data['author'] = self.author.name
		data['position'] = self.position
		data['title'] = self.title
		data['text'] = self.text
		# data['media_file'] = self.media_file
		data['layout_type'] = self.layout_type

		return data




	def __str__(self):
		return self.title
		