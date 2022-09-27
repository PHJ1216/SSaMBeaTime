from django.db import models


class ssam(models.Model):
    content = models.TextField(max_length=2000)
    board_name = models.CharField(max_length=100)
