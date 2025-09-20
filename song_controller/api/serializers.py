
"""
Will take our model like Room that has all of this Python related code
and turn them into JSON response to make it easier for frontend to interact with backend.
It'll take the keys like "code" or "host" and turn them into string and then it'll add a colon
and the actual value that's stored there
"""

from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room # The room model in models.py
        # Strings will match what we have in models.
        # Each model will have a PK and the PK is some unique int that identifies the model
        # This is automatically created when we have a new model or insert and we could see it with 'id' here.
        fields = ('id', 'code', 'host', 
                  'guest_can_pause', 'votes_to_skip', 'created_at')
        

