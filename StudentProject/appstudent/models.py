from django.db import models


class Application(models.Model):
    email = models.EmailField(max_length=100, primary_key=True)
    fullname = models.CharField(max_length=100)
    marks_ssc = models.IntegerField()
    marks_inter = models.IntegerField()

    # is_verified = models.BooleanField(default=False)

    def is_verified(self):
        return 850 <= self.marks_inter

    is_verified.boolean = True


class Register(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    DEPART_CHOICES = (
        ('CSE', 'CS'),
        ('IT', 'IT'),
        ('ECE', 'EC'),
        ('EEE', 'EE'),
        ('CIVIL', 'CVL'),
        ('MECH', 'ME')
    )
    department = models.CharField(max_length=10, choices=DEPART_CHOICES)
    nantionality = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    photo = models.ImageField(blank=True, upload_to='images/')

    def fullname(self):
        return self.firstname + ' ' + self.lastname
