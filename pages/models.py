from django.db import models

class Page(models.Model):
    title=models.CharField(max_length=60, null=True, blank=True )
    permalink=models.CharField(max_length=60, null=True, blank=True, unique=True )
    update_date=models.DateTimeField('Last Updated',auto_now=True)
    bodytext = models.TextField('Page Content',blank=True,null=True)

    
    def __str__(self):
        return self.title  
