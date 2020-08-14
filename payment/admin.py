from django.contrib import admin

from payment.models import PaymentStatus, FinanceCompany, InsuranceCompany


@admin.register(PaymentStatus)
class PaymentStatusAdmin(admin.ModelAdmin):
    fields = ('payment_status_code', 'payment_status_description')


@admin.register(FinanceCompany)
class FinanceCompanyAdmin(admin.ModelAdmin):
    fields = ('id', 'name')


@admin.register(InsuranceCompany)
class InsuranceCompanyAdmin(admin.ModelAdmin):
    fields = ('id', 'name')
