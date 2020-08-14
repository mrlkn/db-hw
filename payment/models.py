import uuid

from django.db import models


class PaymentStatus(models.Model):
    """
    Odeme Statusu tablosunu olusturan class
    """
    payment_status_code = models.UUIDField(primary_key=True, default=uuid.uuid4)
    payment_status_description = models.TextField()


class FinanceCompany(models.Model):
    """
    Finans sirketi tablosunu olusturan class
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.TextField()


class InsuranceCompany(models.Model):
    """
    Sigorta sirketi tablosunu olusturan class
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.TextField()
