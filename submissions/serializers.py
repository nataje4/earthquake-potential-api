from rest_framework import serializers
from submissions.models import Submission

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        exclude = [	'editor_notes', 'submission_status', 'submission_file']
