from django.db import models
import string
import random
# Where database models will go.
# Create your models here.

# Everytime we create a code we must generate a code for a room
def generate_unique_code():
    length = 6
    while True:
        # Will generate random code that is k letter length (6) and can only generate uppercase letters
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        # Make sure the code is unique
        if Room.objects.filter(code=code).count() == 0: # If it doesn't exist yet
            break

    return code 

# Instead of creating a table like in SQL, we'll create a model instead which will
# let us write Python code

# Think Room table
# The model will automatically have a PK here.
class Room(models.Model): # Param will tell us this will be a model (defined above)
    code = models.CharField(max_length=8, default="", unique=True) # The unique code that identifies the room 
    host = models.CharField(max_length=50, unique=True) 
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    # We could also have methods for this model using methods
    #def isHostThis(host):



