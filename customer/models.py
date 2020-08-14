import uuid

from django.db import models

from car.models import CarSold, CarFeatures
from payment.models import PaymentStatus


class Customer(models.Model):
    """
    Musteri tablosunu olusturan class
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    mobile_phone = models.PositiveIntegerField()
    email_address = models.CharField(max_length=128)
    other_customer_details = models.TextField()


class CustomerPreferences(models.Model):
    """
    Musteri seceneklerini olusturan class
    Musteri tablosuna ForeignKey ile bagli
    Arac Ozellikleri tablosuna Foreign Key ile bagli
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='custormer')
    car_feature = models.ForeignKey(CarFeatures, on_delete=models.CASCADE,
                                    related_name='car_feature')
    customer_preferences_details = models.TextField()


class CustomerAddress(models.Model):
    """
    Musteri Adresi tablosunu olusturan class
    Musteri tablosuna Foreign Key ile bagli
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_adress')
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    address_line3 = models.TextField()
    address_line4 = models.TextField()
    town_city = models.TextField()
    state_province = models.TextField()
    country = models.TextField()
    post_zip_code = models.IntegerField()
    other_address_details = models.TextField()


class CustomerPayments(models.Model):
    """
    Musteri odeme tablosunu olusturan classimiz
    Satilan arac tablosuna Foreign Key ile bagli
    Musteri tablosuna foreign key ile bagli
    Odeme durumu tablosuna foreign key ile bagli

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    car_sold = models.ForeignKey(CarSold, on_delete=models.CASCADE, related_name='car_sold')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    payment_status = models.ForeignKey(PaymentStatus, on_delete=models.CASCADE,
                                       related_name='payment_status')
    customer_payment_date_due = models.DateField()
    customer_payment_date_made = models.DateField()
    actual_payment_amount = models.DecimalField(max_digits=5, decimal_places=4)
