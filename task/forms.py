from django import forms
from django.core.exceptions import ValidationError

from task.models import GroupCourse


class GroupForms(forms.ModelForm):
    class Meta:
        model = GroupCourse
        fields = ('group_name', 'subject', 'member')

    def clean(self):
        members = self.cleaned_data.get('member')
        count = 0
        for group_member in members:
            if group_member.role == 'teacher':
                count += 1
            if count > 2:
                raise ValidationError('A group can have at most 2 teachers')
        return self.cleaned_data

