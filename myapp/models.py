from django.db import models

# Create your models here.

'''class person(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)'''


class Blogs(models.Model):
	title=models.CharField(max_length=200)
	description=models.TextField()
	date=models.DateTimeField()
	image=models.ImageField(upload_to="data",blank=True)
	def __str__(self):
		return self.title


class FAQ(models.Model):
	question=models.TextField()
	answer=models.TextField()
	def __str__(self):
		return self.question

class LatestNews(models.Model):
	Heading=models.CharField(max_length=500)
	Description=models.TextField()
	image=models.ImageField(upload_to="data",blank=True)
	def __str__(self):
		return self.heading

class SearchEngine(models.Model):
	title=models.CharField(max_length=200)
	description=models.TextField()
	images=models.ImageField(upload_to="data",blank=True)
	Link=models.URLField()
	def __str__(self):
		return self.title
class user_register(models.Model):
	name=models.CharField(max_length=40)
	email=models.EmailField()
	password=models.CharField(max_length=40)
	'''confirmpassword=models.CharField(max_length=40)'''
	contact=models.CharField(max_length=30,blank=True, null=True)
	DOB=models.CharField(max_length=30,blank=True, null=True)
	pincode=models.CharField(max_length=30,blank=True, null=True)
	address=models.CharField(max_length=100,blank=True, null=True)
	def __str__(self):
		return self.name

class contact_us(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=50)
	phone=models.CharField(max_length=20)
	message=models.TextField(max_length=500)
	def __str__(self):
		return self.name

class review(models.Model):
	title=models.CharField(max_length=100)
	message=models.TextField(max_length=500)
	def __str__(self):
		return self.title

'''class UserChangePassword(models.Model):
	old_pass=models.CharField(max_length=40)
	new_pass=models.CharField(max_length=40)
	def __str__(self):
		return self.new_pass'''

class helpSupport(models.Model):
	heading=models.CharField(max_length=40)
	content=models.TextField(max_length=500)
	def __str__(self):
		return self.heading

