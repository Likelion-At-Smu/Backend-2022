from django import forms

class SearchForm(forms.Form):
# 검색할 수 있는 form을 만들었다
    search = forms.CharField(label='Search For Movies..', max_length=100)
    # 문자를 받을 것이므로 CharField를 쓰고 문자열 최대 길이는 100으로 고정