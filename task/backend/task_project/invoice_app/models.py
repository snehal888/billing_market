from django.db import models


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20)
    total_cost = models.FloatField(default=0.0, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.invoice_number}'
    
class Products(models.Model):
    product_name = models.CharField(max_length=20)
    product_quantity = models.FloatField()
    product_price = models.FloatField()
    product_total_cost = models.FloatField(default=0.0, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='products')

    def __str__(self) -> str:
        return f'{self.product_name}'

