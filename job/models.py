from django.db import models
JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

class job(models.Model):
    title = models.CharField(max_length=100)
    #location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE )
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary =  models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('category', on_delete=models.CASCADE) #ben double '' 3shan l category class gia b3dha w l cascde 3shan law ms7t l category yms7 kol l jobs l gwaha

    
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
