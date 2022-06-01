from .models import ExtraInfo
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
import logging


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['nationality'].required = True
        self.fields['age'].required = True
        self.fields['phone_number'].required = True
        self.fields['institution_name'].required = True
        self.fields['class_name'].required = True
        

    class Meta(object):
        model = ExtraInfo
        fields = ('nationality','age','phone_number','institution_name','class_name',)
        labels = {'nationality': _("Nationality"),'age': _("Age"),'phone_number': _("Phone number"),'institution_name':_("Institution Name"),'class_name':_("Class Name"),}
        help_text = {'nationality': _("Please enter your Nationality"),'age': _("Please enter your Age"),'phone_number': _("Please enter your phone number"),'institution_name': _("Please enter your Institution name"),'class_name': _("Please enter your Class name"),}
