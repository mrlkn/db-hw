from django.contrib import admin

from customer.models import Customer, CustomerPreferences, CustomerAddress, CustomerPayments


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('id', 'mobile_phone', 'email_address', 'other_customer_detail')


@admin.register(CustomerPreferences)
class CustomerPreferencesAdmin(admin.ModelAdmin):
    fields = ('id', 'customer', 'car_feature', 'customer_preferences_details')


@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    fields = (
        'id', 'customer', 'address_line1', 'address_line2', 'address_line3', 'address_line4',
        'town_city', 'state_province', 'country', 'post_zip_code', 'other_address_details'
    )


@admin.register(CustomerPayments)
class CustomerPaymentAdmin(admin.ModelAdmin):
    fields = (
        'id', 'car_sold', 'customer', 'payment_status', 'customer_payment_date_due',
        'customer_payment_date_made', 'actual_payment_amount'
    )
