from django.db import models
from accounts.models import CustomUser 
from django.utils.translation import gettext_lazy as _

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100 ,null=True, blank=True)
    email = models.EmailField(blank=True, null=True)  # أضفت الإيميل
    phone = models.CharField(max_length=15)  # غيرت الاسم من phone إلى mobile ليتطابق مع الفورم
    medical_history = models.TextField(blank=True, null=True)  # خليتها اختيارية

    def __str__(self):
        return self.name
    
class Department(models.Model):
    specialization = models.CharField(max_length=50)
    details = models.TextField()
    def __str__(self):
        return self.specialization

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE , null=True, blank=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100 ,null=True, blank=True)
    img = models.ImageField(upload_to='doctors/', blank=True, null=True)  # حطيت upload_to
    #specialization = models.CharField(max_length=50)
    specialization= models.ForeignKey(Department,  on_delete=models.CASCADE, null=True, blank=True)
    is_experience = models.BooleanField(_("Has Experience"), default=False)
    phone = models.CharField(max_length=15)
    facebook = models.CharField(max_length=100 , blank=True , null=True)
    twitter  = models.CharField(max_length=100 , blank=True , null=True)
    instagram = models.CharField(max_length=100 , blank=True , null=True)

    def __str__(self):
        return self.firstname

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField()  # هنا التاريخ والوقت مع بعض، أنسب من فصلهم
    problem_description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ],
        default='pending'
    )

    def __str__(self):
        return f"Appointment for {self.patient.name} with {self.doctor.name} on {self.date.strftime('%Y-%m-%d %H:%M')}"

