import django_filters
from .models import Index, Discipline
import datetime
from django import forms


def year_choices():
    return [(r,r) for r in range(2018, datetime.date.today().year+5)]


def current_year():
    return datetime.date.today().year


# class IndexFilter(django_filters.FilterSet):
#     # data = django_filters.DateFilter(lookup_expr='date__year')
#     print(current_year)
#     data = django_filters.TypedChoiceFilter(coerce=int, choices=year_choices, initial=current_year)
#
#
#     # def form(self):
#     #     form = ProductFilterForm
#     #     return
#
#     class Meta:
#         model = Index
#         fields = {'data', 'indexes__data'}

class IndexFilter(django_filters.FilterSet):
    indexes__data = django_filters.TypedChoiceFilter(coerce=int, choices=year_choices, initial=current_year)

    class Meta:
        model = Discipline
        fields = ['indexes__data',]
        widgets = {
            'indexes__data': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Название'}),
        }
    #
    # @property
    # def qs(self):
    #     parent = super().qs
    #     user = self.request.user
    #     ed
    #     return parent.filter(teacher=user)