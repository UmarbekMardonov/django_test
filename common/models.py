from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=220)
    price = models.DecimalField(max_digits=220, decimal_places=2)
    discount_price = models.DecimalField(max_digits=220, decimal_places=2)
    count = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def active(self):
        if self.is_active:
            return self.count


"""

Product
    - title
    - price 80 
    - discount price 100
    - count - 15 ta bor
    - is active - True
  
    - function active
    - function can buy ( count )  

    Product active bo'ladi qachonki is active bo'lsa va count >0

    Product ni sotib olib bo'ladimi (count) 
    Tugalmagan, yoki Paymentda bo'lgan productlarni hold qilib turishi kerak.
    
    Product sotib olingandan so'ng canceled bo'lsa countlarini joyiga qaytirishi kerak.

Cart
    - user
    - product
    - quantity
    - is active

    update quantity
    create order

    agar berilgan miqdorda productni sotib olish mumkin bo'lsa cart countni yangilash kerak.

Order
    - total price
    - user
    - total discount
    - status - INITIAL, PAYMENT, ACCEPTED, CANCELED, DELIVERED

    Order accepted bo'lsa product count dan ayrilishi kerak.
    canceled bo'lsa qo'shilishi kerak.


Order Product
    - product
    - order
    - price
    - quantity
    """