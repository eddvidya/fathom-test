from django.db import models

class Log(models.Model):
    desc = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"