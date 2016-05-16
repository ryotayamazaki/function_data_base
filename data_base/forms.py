from django.forms import ModelForm
from data_base.models import Pkg, Proglam, Function


class PkgForm(ModelForm):
    """pkgのフォーム"""
    class Meta:
        model = Pkg
        fields = ('name', 'child', 'maker', 'mightiness', 'tag', 'git', )


class ProglamForm(ModelForm):
    """proglamのフォーム"""
    class Meta:
        model = Proglam
        fields = ('name', 'child', 'maker', 'mightiness', 'tag', 'git', )


class FunctionForm(ModelForm):
    """functionのフォーム"""
    class Meta:
        model = Function
        fields = ('name', 'maker', 'mightiness', 'tag', 'git',  )
