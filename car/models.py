import uuid

from django.db import models

from payment.models import FinanceCompany, InsuranceCompany


class CarModel(models.Model):
    """
    Araba modelleri tablosunu yarattigimiz class
    """
    model_code = models.UUIDField(primary_key=True, default=uuid.uuid4)
    manufacturer_code = models.SmallIntegerField()
    model_name = models.CharField(max_length=64)


class CarManufacturer(models.Model):
    """
    Araba ureticileri tablosunu yarattigimiz class
    """
    manufacturer_short_name = models.CharField(primary_key=True, max_length=128)
    manufacturer_full_name = models.TextField()
    manufacturer_other_details = models.TextField()


class VehicleCategory(models.Model):
    """
    Araba kategorileri tablosunu yarattigimiz class
    """
    vehicle_category_name = models.CharField(primary_key=True, max_length=128)
    vehicle_category_description = models.TextField()


class CarSale(models.Model):
    """
    Satilik olan araclar tablosunun classi
    Arac ureticisi tablosuna Foreign Key ile bagli
    Arac kategori tablosuna Foreign Key ile bagli
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    manufacturer_short_name = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE,
                                                related_name='CarManufacturer')
    model_code = models.ForeignKey(CarModel, on_delete=models.CASCADE, default=uuid.uuid4)
    vehicle_category = models.ForeignKey(VehicleCategory, on_delete=models.CASCADE,
                                         default=uuid.uuid4)
    asking_price = models.DecimalField(decimal_places=2, max_digits=5)
    current_km = models.DecimalField(decimal_places=2, max_digits=5)
    date_acquired = models.DateField()
    other_car_details = models.TextField()


class CarFeatures(models.Model):
    """
    Arac ozellikleri tablosunu yarattigimiz class
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    car_feature_description = models.TextField()


class FeaturesForSaleCars(models.Model):
    """
    Arac ozelliklerini, Satilik olan arac tablosuna baglayan ara bir tablo
    """
    car_for_sale = models.ForeignKey(CarSale, on_delete=models.CASCADE, default=uuid.uuid4)
    car_features = models.ForeignKey(CarFeatures, on_delete=models.CASCADE, default=uuid.uuid4)


class CarSold(models.Model):
    """
    Satilan araclarimizin tablosu
    Satilacak olan arac tablosuna FK ile bagli
    Finans Sirketi tablosuna FK ile bagli
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    car_for_sale = models.ForeignKey(CarSale, on_delete=models.CASCADE, related_name='carsale')
    finance_companies = models.ForeignKey(FinanceCompany, on_delete=models.CASCADE,
                                          related_name='finance_company')
    agreed_price = models.DecimalField(decimal_places=2, max_digits=5)
    date_sold = models.DateField()


class CarLoans(models.Model):
    """
    Kiralik araclarimizin tablosu
    Satilan arac tablosuna FK ile bagli
    Finans Sirketi tablosuna FK ile bagli
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    car_sold = models.ForeignKey(CarSold, on_delete=models.CASCADE, related_name='carsolds')
    finance_companies = models.ForeignKey(FinanceCompany, on_delete=models.CASCADE,
                                          related_name='finance_companies')
    payment_start_date = models.DateField()
    payment_end_date = models.DateField()
    monthly_payments = models.DecimalField(decimal_places=2, max_digits=5)


class InsurancePolicies(models.Model):
    """
    Sigorta Policesi tablosunu olusturan class'imiz
    Sigorta Sirketi tablosuna Foreign Key ile bagli
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE,
                                          related_name='insurance_companies')
    policy_start_date = models.DateField()
    policy_end_date = models.DateField()
