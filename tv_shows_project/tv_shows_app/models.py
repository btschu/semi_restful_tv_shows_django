from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 1:
            errors["title"] = "Please enter a TITLE"
        if len(postData['network']) < 1:
            errors["network"] = "Please enter a NETWORK"
        if len(postData['release_date']) < 1:
            errors["release_date"] = "Please enter a RELEASE DATE"
        if len(postData['description']) < 1:
            errors["description"] = "Please enter a DESCRIPTION"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()