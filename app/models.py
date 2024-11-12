from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Skill(models.Model):
  name = models.CharField(max_length=200)
  def __str__(self):
    return self.name
  
class Social(models.Model):
  name = models.CharField(max_length=200,null=True)
  icon = models.ImageField(upload_to='socials/')
  url = models.URLField(null=True)
  
  def __str__(self):
    return self.name

class AboutMe(models.Model):
  name = models.CharField(max_length=200)
  short_desc = models.CharField(max_length=5000)
  skills = models.ManyToManyField(Skill,related_name='skills')
  socials = models.ManyToManyField(Social,related_name='socials')
  image = models.ImageField(null=True)

  def __str__(self):
    return self.name
  

class Contact(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField()
  message = models.TextField()

  def __str__(self):
    return f"{self.message[:50]}"
  

class Project(models.Model):
  name = models.CharField(max_length=200)
  about = models.TextField()
  overview = RichTextField()
  live_link = models.URLField(null=True,blank=True)
  link = models.URLField(null=True,blank=True)
  image = models.ImageField(upload_to='projects/')
  tools = models.ManyToManyField(Skill,related_name='project')

  def __str__(self):
    return self.name

