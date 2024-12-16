from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from capital_backend import settings

from .models import LoanApplicationModel  # Import model if used
from .serializer import LoanApplicationSerializer, ContactUsSerializer  # Import serializer if used
import logging

class LoanApplicationView(APIView):
  serializer_class = LoanApplicationSerializer
  def post(self, request):
    data = request.data
    serializer = self.serializer_class(data=data)  # Use serializer if used
    
    if not serializer.is_valid():
       return Response({
                'status': False,
                'message': "Invalid data provided",
                'error': serializer.errors
        }, status=HTTP_400_BAD_REQUEST)
     
       
   
      # Save data to database if using models
      # application = serializer.save()

      # Extract data for email
    data = serializer.validated_data  # Use data directly if not using models
    name = data.get('name')
    id_number = data.get('id_number')
    email = data.get('email')
    loan_type = data.get('loan_type')
    amount = data.get('amount')
    security_type = data.get('security_type')

    logging.info(f'{name}, {id_number},{email},{loan_type},{amount},{security_type}')

    # Send email content
    subject = f"Loan Application from {name}"
    message = f"""
    Name: {name}
    Id_number:{id_number}
    Email: {email}
    Loan Type: {loan_type}
    Amount: {amount}
    Security Type: {security_type}
    """
    try:
      send_mail(
          subject,
          message,
          email,  # Replace with your email
          [settings.LOAN_RECEPIENT_EMAIL],  # Recipient email
          fail_silently=False,
      )

      return Response({'message': 'Loan application submitted successfully!'}, status=status.HTTP_201_CREATED)
    except:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ContactFormView(APIView):
  serializer_class = ContactUsSerializer
  def post(self, request):
      data = request.data
      serializer = self.serializer_class(data = data)
      if not serializer.is_valid():
        return Response({
                'status': False,
                'message': "Invalid data provided",
                'error': serializer.errors
        }, status=HTTP_400_BAD_REQUEST)
     
      # Extract validated data
      validated_data = serializer.validated_data
      
      name = validated_data.get('name')
      email = validated_data.get('email')
      message = validated_data.get('message')

      logging.info(f'{name}\n{email}\n{message}')

      # Construct email content
      subject = f"New message for 254 capital from {name}"
      message_body = f"{message}"

      logging.info(message_body)

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