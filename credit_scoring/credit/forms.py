from django import forms

class CreditForm(forms.Form):
    ru = forms.IntegerField(label="RevolvingUtilizationOfUnsecuredLines")
    age = forms.IntegerField(label="Age")
    times30 = forms.IntegerField(label="NumberOfTime30-59DaysPastDueNotWorse")
    dr = forms.IntegerField(label="DebtRatio")
    mi = forms.IntegerField(label="MonthlyIncome")
    loans = forms.IntegerField(label="NumberOfOpenCreditLinesAndLoans")
    late = forms.IntegerField(label="NumberOfTimes90DaysLate")
    lines = forms.IntegerField(label="NumberRealEstateLoansOrLines ")
    times60 = forms.IntegerField(label="NumberOfTime60-89DaysPastDueNotWorse")
    nd = forms.IntegerField(label="NumberOfDependents ")
