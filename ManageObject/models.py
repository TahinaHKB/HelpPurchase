from django.db import models
from django.forms import ModelForm, PasswordInput
from django.template.defaultfilters import slugify
from datetime import datetime

# Create your models here.
class Member(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length = 255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, default="")
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs): 
        if not self.slug : 
            self.slug = slugify(self.firstName+"-"+self.lastName)
        super().save(*args, **kwargs)

class MemberSignInForm(ModelForm):
    class Meta: 
        model = Member
        fields  = ['firstName', 'lastName', 'email', 'password']
        widgets = {
            'password' : PasswordInput(attrs={
                # attribut
            }),
        }

class List(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(default=datetime.now)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, default=0)
    slug = models.SlugField(default="", null=False)
    def save(self, *args, **kwargs): 
        if not self.slug : 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ListCreateForm(ModelForm):
    class Meta: 
        model = List
        fields  = ['title']

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    number = models.IntegerField()
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=0)

class AddObjectForm(ModelForm):
    class Meta: 
        model = Product
        fields  = ['name', 'price', 'number']