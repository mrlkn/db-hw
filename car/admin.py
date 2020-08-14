from django.contrib import admin

from car.models import (
    CarModel, CarManufacturer, VehicleCategory, CarSale, CarFeatures,
    FeaturesForSaleCars,
    CarLoans,
    InsurancePolicies
)


@admin.register(CarModel)
class CarAdmin(admin.ModelAdmin):
    fields = ('model_code', 'manufacturer_code', 'model_name')


@admin.register(CarManufacturer)
class CarManufacturerAdmin(admin.ModelAdmin):
    fields = ('manufacturer_short_name', 'manufacturer_full_name', 'manufacturer_other_details')


@admin.register(VehicleCategory)
class VehicleCategoryAdmin(admin.ModelAdmin):
    fields = ('vehicle_category_name', 'vehicle_category_description')


@admin.register(CarSale)
class CarSaleAdmin(admin.ModelAdmin):
    fields = (
        'id', 'manufacturer_short_name', 'model_code', 'vehicle_category', 'asking_price',
        'current_km', 'date_acquired', 'other_car_details',
    )


@admin.register(CarFeatures)
class CarFeaturesAdmin(admin.ModelAdmin):
    fields = ('id', 'car_feature_description')


@admin.register(FeaturesForSaleCars)
class FeaturesForSaleCarAdmin(admin.ModelAdmin):
    fields = ('car_for_sale', 'car_features')


@admin.register(CarLoans)
class CarLoansAdmin(admin.ModelAdmin):
    fields = ('id', 'car_sold', 'finance_companies', 'payment_start_date', 'payment_end_date',
              'monthly_payment')


@admin.register(InsurancePolicies)
class InsurancePoliciesAdmin(admin.ModelAdmin):
    fields = ('id', 'insurance_company', 'policy_start_date', 'policy_end_date')
