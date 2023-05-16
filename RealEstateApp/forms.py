from datetime import datetime, timedelta

from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, \
    YearPickerInput
from django import forms
from .models import TimeSlot




class DateTimeForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['time']

        widgets = {
            'time': DateTimePickerInput(options={
                "showTodayButton": True,
                "locale": "ru",
                "format": "DD.MM.YYYY: HH:mm",
                'minDate': (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d 00:00:00'),
                # 'maxDate': (datetime.today() + timedelta(days=2)).strftime('%Y-%m-%d 23:59:59'),
                'enabledHours': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                'daysOfWeekDisabled': [0, 6],

            })
        }
