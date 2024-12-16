from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class LoanApplicationModel(models.Model):
  name = models.CharField(max_length=255)
  id_number = models.CharField(max_length=255)
  email = models.EmailField()
  loan_type = models.CharField(max_length=255)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  security_type = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  attachment = models.FileField( null=True,blank=True,validators=[
            # Optional: Limit file extensions
            FileExtensionValidator(
                allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']
            )
        ],
        max_length=255  
        )

  def __str__(self):
    return f"{self.name} - {self.loan_type}"
  

class ContactUsModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=255)

    def __str__(self):
       return f"{self.name}\n {self.email}\n{self.message}"