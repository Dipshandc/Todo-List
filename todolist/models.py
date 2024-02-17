from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length = 255)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default= False)
    due_date = models.DateTimeField()
    
    def __str__(self):
        return self.task_name