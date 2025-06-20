from django.db import models

class Registration(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100, default='')
    user_pass = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=12)
    user_status = models.IntegerField(default=1)
    
    # ForeignKey to Admin.Role
    role = models.ForeignKey('Admin.Role', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name



class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


