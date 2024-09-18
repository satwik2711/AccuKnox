from django.db import models

class LogEntry(models.Model):
    message = models.CharField(max_length=255)
    
    def __str__(self):
        return self.message
