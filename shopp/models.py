from django.db import models

class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'shopp'

class Guard(models.Model):
    id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, related_name='guards', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'shopp'

class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, related_name='sellers', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'shopp'

class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    shops = models.ManyToManyField(Shop, related_name='buyers')
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'shopp'

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    shops = models.ManyToManyField(Shop, related_name='products')
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveIntegerField()

    class Meta:
        app_label = 'shopp'

    def str(self):
        return self.name
