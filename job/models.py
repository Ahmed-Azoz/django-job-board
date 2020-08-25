from django.db import models
from django.utils.text import slugify
JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)


def image_upload(instance, file_name):
    imagename, extension = file_name.split(".")
    return "jobs/%s.%s"%(instance.id, extension)


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
    image = models.ImageField(upload_to = image_upload)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(job, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(job, related_name='apply_ob', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    cv = models.FileField(upload_to='apply/')
    website = models.URLField()
    cover_letter = models.CharField(max_length=500)
    cearted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
