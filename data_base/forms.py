from django.forms import ModelForm
from data_base.models import Pkg, Proglam, Function, Pkg_updated, Function_updated, Proglam_updated


class PkgForm(ModelForm):
    """pkgのフォーム"""
    class Meta:
        model = Pkg
        fields = ('name', 'child', 'maker', 'mightiness', 'tag', 'git', )


class PkgupdatedForm(ModelForm):
    class Meta:
        model = Pkg_updated
        fields = ('date', 'maker', 'content', 'reason', )


class ProglamForm(ModelForm):
    """proglamのフォーム"""
    class Meta:
        model = Proglam
        fields = ('name', 'child', 'maker', 'mightiness', 'tag', 'git', )


class ProglamupdatedForm(ModelForm):
    class Meta:
        model = Proglam_updated
        fields = ('date', 'maker', 'content', 'reason', )


class FunctionForm(ModelForm):
    """functionのフォーム"""
    class Meta:
        model = Function
        fields = ('name', 'maker', 'mightiness', 'tag', 'git', )


class FunctionupdatedForm(ModelForm):
    class Meta:
        model = Function_updated
        fields = ('date', 'maker', 'content', 'reason', )
