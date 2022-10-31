from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from cairo import Device
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from twilio.rest import Client
from Task.settings import GMAIL_ID, GMAIL_PASS, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from task import main
from django.core.mail import send_mail
from django.db import transaction


class User_data(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    Age = models.IntegerField(null=False, blank=False)
    Location = models.CharField(max_length=100)
    Device = models.CharField(max_length=100)
    Income = models.IntegerField(null=False, blank=False)
    Balance = models.IntegerField(null=False, blank=False)
    Products = models.CharField(max_length=100)


@receiver(pre_save, sender=User_data)
def on_change(sender, instance: User_data, **kwargs):
    if instance.CustomerId is None:  # new object will be created
        pass  # write your code here
    else:
        previous = User_data.objects.get(CustomerId=instance.CustomerId)
        if previous.Balance != instance.Balance:  # field will be updated
            transact = instance.Balance - previous.Balance
            reco(previous.CustomerId)
            sms(transact=transact, flag=0)
            mail(previous.CustomerId)


@receiver(post_save, sender=User_data)
def add(sender, instance: User_data, **kwargs):
    if kwargs["created"] == True:
        print("Added")
        sms(flag=1, pk=instance.CustomerId)
        mail(pk=instance.CustomerId, flag=1)


def reco(pk):
    Location = User_data.objects.filter(CustomerId=pk).values("Location")
    Device = User_data.objects.filter(CustomerId=pk).values("Device")
    main.user_data["location"] = Location[0]["Location"]
    main.user_data["device"] = Device[0]["Device"]
    print(Location)
    print(Device)
    main.user_data["recommended_cards"] = []
    main.user_data["recommended_loans"] = []
    main.user_data["recommended_packages"] = []
    main.user_data["recommended_privilege_banking"] = []
    main.user_data["recommended_deposit_accounts"] = []
    main.user_data["recommended_bank_accounts"] = []
    main.append_persona()
    main.reco_product()
    product = []
    product = (
        main.user_data["recommended_cards"]
        + main.user_data["recommended_loans"]
        + main.user_data["recommended_packages"]
        + main.user_data["recommended_privilege_banking"]
        + main.user_data["recommended_deposit_accounts"]
        + main.user_data["recommended_bank_accounts"]
    )
    message = ""
    message = ",".join(product)
    print(message)
    return message


def mail(pk, flag=0):
    message = f"We would like to recommend some products that may benefit you more,some of whcih are:\n{reco(pk)}\nTo learn more about these products, please visit our website or contact our agents and you can also make use of our chatbots for assistance"
    if flag == 1:
        message = f"Thank you for registering with our Bank.We would like to recommend some products that may benefit you more,some of which are:\n{reco(pk)}\nTo learn more about these products, please visit our website or contact our agents and you can also make use of our chatbots for assistance"
    subject = f"Product Recommendation from CBQ for Customer {pk}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [
        "abhinav.nair@affinsys.com",
    ]
    send_mail(subject, message, email_from, recipient_list)


def sms(flag, pk=0, transact=0):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    if flag == 0:
        if transact > 0:
            out = f"{abs(transact)} QAR is credited to your account"
        else:
            out = f"Your account is debited by {abs(transact)} QAR"
        message = client.messages.create(
            body=out, from_="+19203521105", to="+917827598718"
        )

        print(message.sid)
    else:
        prod = reco(pk)
        out = f"Thank you for registering with us, additionally we would recommend checking these products as they may be beneficial to you {prod}\nTo learn more about these products, please visit our website or contact our agents and you can also make use of our chatbots for assistance"
        message = client.messages.create(
            body=out, from_="+19203521105", to="+917827598718"
        )

        print(message.sid)
