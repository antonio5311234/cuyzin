from django import forms

class CustomUserWidget(forms.TextInput):
    def __init__(self, user=None, editable_for=None, readonly_for=None, hidden_for=None, attrs=None):
        """
        - user: el usuario actual (objeto request.user)
        - editable_for: lista de usernames que pueden editar
        - readonly_for: lista de usernames que solo pueden leer
        - hidden_for: lista de usernames para los que el campo se oculta
        """
        self.user = user
        self.editable_for = editable_for or []
        self.readonly_for = readonly_for or []
        self.hidden_for = hidden_for or []
        final_attrs = attrs or {}

        super().__init__(attrs=final_attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if self.user:
            username = self.user.username

            if username in self.hidden_for:
                context["widget"]["type"] = "hidden"
            elif username in self.readonly_for:
                context["widget"]["attrs"]["readonly"] = "readonly"
        return context
