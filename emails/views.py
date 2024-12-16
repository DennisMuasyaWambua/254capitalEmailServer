from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from capital_backend import settings

from .models import LoanApplicationModel  # Import model if used
from .serializer import LoanApplicationSerializer, ContactUsSerializer  # Import serializer if used
import logging

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
      serializer = ContactUsSerializer(data=request.data)
      if serializer.is_valid():
          # Extract validated data
          name = serializer.validated_data['name']
          email = serializer.validated_data['email']
          message = serializer.validated_data['message']

          # Construct email content
          subject = f"New Contact Form Submission from {name}"
          message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

          # Send email
          try:
              send_mail(
                  subject,
                  message_body,
                  email,  # Sender email
                  [settings.CONTACT_RECIPIENT_EMAIL],  # Fixed recipient
              )
              return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
          except Exception as e:
              return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)