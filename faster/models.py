from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Subject = models.CharField(max_length=100)
    Message = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Name


class Service(models.Model):
    Customer_Name = models.CharField(max_length=50)
    Origin = models.CharField(max_length=100)
    Destination = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_Number = models.IntegerField
    Payment = models.CharField(max_length=1)
    Service = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Customer_Name

class Comment(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Subject = models.CharField(max_length=100)
    Message = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Email


class Sign_In(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=10)
    


    def __str__(self):
        return self.Username

class Sign_Up(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=10)
    Repeat_Password = models.CharField(max_length=100)
    Email = models.EmailField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Username



    

