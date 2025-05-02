from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('done', 'Done'),
        ('not_done', 'Not Done'),
        ('in_work', 'In Work'),
    ]
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='not_done')

    def __str__(self):
        return self.name
