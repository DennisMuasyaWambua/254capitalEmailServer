from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import LoanApplicationModel  # Import model if used
from .serializer import LoanApplicationSerializer  # Import serializer if used

class LoanApplicationView(APIView):
  def post(self, request):
    serializer = LoanApplicationSerializer(data=request.data)  # Use serializer if used

    if serializer.is_valid():
      # Save data to database if using models
      # application = serializer.save()

      # Extract data for email
      data = serializer.validated_data  # Use data directly if not using models
      name = data['name']
      email = data['email']
      loan_type = data['loan_type']
      amount = data['amount']
      security_type = data['security_type']

      # Send email content
      subject = f"Loan Application from {name}"
      message = f"""
      Name: {name}
      Email: {email}
      Loan Type: {loan_type}
      Amount: {amount}
      Security Type: {security_type}
      """
      send_mail(
          subject,
          message,
          f'{email}',  # Replace with your email
          ['loans@254-capital.com'],  # Recipient email
          fail_silently=False,
      )

      return Response({'message': 'Loan application submitted successfully!'}, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ContactFormView(APIView):
  def post(self, request):
    data = request.data  # Extract data from request body
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if name and email and message:  # Basic validation
      subject = f"Contact from {name}"
      message_content = f"""
      Name: {name}
      Email: {email}
      Message: {message}
      """
      send_mail(
          subject,
          message_content,
          f'{email}',  # Replace with your email
          ['info@254-capital.com'],  # Recipient email
          fail_silently=False,
      )

      return Response({'message': 'Message sent successfully!'}, status=status.HTTP_201_CREATED)
    else:
      return Response({'message': 'Please fill out all required fields.'}, status=status.HTTP_400_BAD_REQUEST)