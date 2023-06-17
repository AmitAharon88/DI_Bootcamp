from django.db import models

# Create your models here.
class RoomType(models.Model) :
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()
    price = models.FloatField()
    
    def __str__(self) :
       return self.name 

class Room(models.Model) :
    number =  models.CharField(max_length=10, unique=True)
    room_type = models.ForeignKey(RoomType, on_delete = models.CASCADE)
    vacancy = models.BooleanField(default=True)

    def __str__(self) :
       return self.number
   
class Booking(models.Model) :
    guest_name = models.CharField(max_length=100)
    num_guests = models.PositiveIntegerField()
    room = models.ForeignKey(RoomType, on_delete = models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    
    def __str__(self) :
       return f'{self.guest_name} checking in on {self.check_in_date}'
    
