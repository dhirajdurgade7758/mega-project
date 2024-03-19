from django.db import models

# Create your models here.


class Semisters(models.Model):
    sem = models.IntegerField()
    def __str__(self):
        return str(self.sem)

class StudyMaterialTypes(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Department(models.Model):
    dep_name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='icons')
    
    def __str__(self):
        return self.dep_name
    
class Subject(models.Model):
    sub_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semister = models.ForeignKey(Semisters, on_delete=models.CASCADE)
    def __str__(self):
        return self.sub_name

class StudyMaterial(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,default=None)
    semister = models.ForeignKey(Semisters,on_delete=models.CASCADE,default=None)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    type = models.ForeignKey(StudyMaterialTypes,on_delete=models.CASCADE,default=None)
    file = models.FileField(upload_to='files')
    
    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
