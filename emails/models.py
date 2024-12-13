from django.db import models

# Create your models here.
class LoanApplicationModel(models.Model):
  name = models.CharField(max_length=255)
  id_number = models.CharField(max_length=255)
  email = models.EmailField()
  loan_type = models.CharField(max_length=255)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  security_type = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name} - {self.loan_type}"