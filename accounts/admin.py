from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserCreationForm, UserChangeForm


User = get_user_model()


class CustomizeUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    list_display = ('username', 'email', 'is_staff')

    fieldsets = (
        ('ユーザー情報', {'fields': (
            'username',
            'email',
            'password',
            'thumbnail',
            )}),
        ('パーミッション', {'fields': (
            'is_staff',
            'is_active',
            'is_superuser',
        )}),
    )

    add_fieldsets = (
        ('ユーザー情報', {
            'fields': (
                'username',
                'email',
                'password',
                'confirm_password',
            )}),
    )

admin.site.register(User, CustomizeUserAdmin)
