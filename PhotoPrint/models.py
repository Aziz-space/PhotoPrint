from django.db import models


class Service(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги' 
    
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/')
    description = models.TextField()

    def __str__(self):
        return self.title

class SI(models.Model):
    class Meta:
        verbose_name = 'Размер услуги'
        verbose_name_plural = 'Размеры услуги'
        
        
    service = models.ForeignKey(Service, related_name='sizes', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    width = models.PositiveIntegerField()  
    height = models.PositiveIntegerField()  

    def __str__(self):
        return f"{self.width}x{self.height} см - {self.price}"


class Status(models.Model):
    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'
        
        
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client_data = models.TextField()  

    def __str__(self):
        return f"Order #{self.id} - {self.status.name}"


class OI(models.Model):
    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
        
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    service_item = models.ForeignKey(SI, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='order_images/', null=True, blank=True)  # Поле для хранения изображений

    def __str__(self):
        return f"{self.quantity} x {self.service_item.name} ({self.order.id})"