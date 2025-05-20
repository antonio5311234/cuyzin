from django import forms

class CustomUserWidget(forms.TextInput):
    def __init__(self, user=None, guardar_historial=False, attrs=None):
        """
        - user: El usuario actual (objeto request.user)
        - guardar_historial: True si el usuario marcó el checkbox
        """
        self.user = user
        self.guardar_historial = guardar_historial
        final_attrs = attrs or {}

        super().__init__(attrs=final_attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        if self.user:
            username = self.user.username

            # 🔹 Bloquear edición de TODOS los campos si el checkbox está marcado
            if self.guardar_historial:
               if name not in ['comentario', 'nota']:
                    context["widget"]["attrs"]["readonly"] = "readonly"


            # 🔹 Comentario solo editable por Marilyn
            if name == "comentario":
                if username != "marilyn":
                    context["widget"]["attrs"]["readonly"] = "readonly"

            # 🔹 Nota solo editable por Antonio
            if name == "nota":
                if username != "antonio":
                    context["widget"]["attrs"]["readonly"] = "readonly"

        return context
