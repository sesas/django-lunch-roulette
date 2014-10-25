from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from . import models


# class DateForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super(DateForm, self).__init__(*args, **kwargs)

#         # If you pass FormHelper constructor a form instance
#         # It builds a default layout with all its fields
#         self.helper = FormHelper(self)

#         # You can dynamically adjust your layout
#         self.helper.layout.append(Submit('save', 'save'))

#     class Meta:
#         # model = models.Participant
#         pass



class ParticipantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = models.Participant
        fields = ['is_participating',]


class LunchGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LunchGroupForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = models.LunchGroup
        fields = ['date',]