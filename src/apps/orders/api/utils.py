from rest_framework import serializers


class BaseSaveSerializer(serializers.ModelSerializer):
    """
    A base serializer to handle saving logic for models with a user field.
    """

    def save(self):
        """
        Saves service data, specifically attaching the user from the request context.
        """
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            self.validated_data["user"] = user
        super().save()
