from django.db import models


class CSV(models.Model):
    csv = models.FileField(upload_to="csvs/")
