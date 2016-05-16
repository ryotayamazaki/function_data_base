#!coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from data_base.models import data_basedata, Pkg, Proglam, Function
from data_base.forms import PkgForm, ProglamForm, FunctionForm
from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView

# Create your views here.
class data_baseform(ModelForm):
    class Meta:
        model = data_basedata
        fields = ('title', 'text', 'date', )

def edit(request):
    data_bases = data_basedata()
    form = None
    if request.method == 'POST':
        form = data_baseform(request.POST, instance=data_bases)
        if form.is_valid():
            data_base = form.save(commit=False)
            data_base.save()
            return redirect('data_bade:show')
        pass
    else:
        form = data_baseform(instance=data_bases)
    return render_to_response('data_base/data_baseedit.html', {'form': form}, context_instance=RequestContext(request))

def show(request):
    data_bases = data_basedata.objects.all()
    return render_to_response('data_base/data_baseshow.html', {'data_bases': data_bases}, context_instance=RequestContext(request))


def pkg_list(request):
    """pkgの一覧"""
#    return HttpResponse('pkgの一覧')
    pkgs = Pkg.objects.all().order_by('id')
    return render(request,
                  'data_base/pkg_list.html',     # 使用するテンプレート
                  {'pkgs': pkgs})         # テンプレートに渡すデータ


def pkg_edit(request, pkg_id=None):
    """pkgの編集"""
#    return HttpResponse('pkgの編集')
    if pkg_id:   # book_id が指定されている (修正時)
        pkg = get_object_or_404(Pkg, pk=pkg_id)
    else:         # book_id が指定されていない (追加時)
        pkg = Pkg()

    if request.method == 'POST':
        form = PkgForm(request.POST, instance=pkg)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            pkg = form.save(commit=False)
            pkg.save()
            return redirect('data_base:pkg_list')
    else:    # GET の時
        form = PkgForm(instance=pkg)  # book インスタンスからフォームを作成

    return render(request, 'data_base/pkg_edit.html', dict(form=form, pkg_id=pkg_id))


def pkg_del(request, pkg_id):
    """pkgの削除"""
#    return HttpResponse('pkgの削除')
    pkg = get_object_or_404(Pkg, pk=pkg_id)
    pkg.delete()
    return redirect('data_base:pkg_list')


class ProglamList(ListView):
    """proglamの一覧"""
    context_object_name='proglams'
    template_name='data_base/proglam_list.html'
    paginate_by = 10  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        pkg = get_object_or_404(Pkg, pk=kwargs['pkg_id'])  # 親の書籍を読む
        proglams = pkg.proglams.all().order_by('id')   # 書籍の子供の、感想を読む
        self.object_list = proglams

        context = self.get_context_data(object_list=self.object_list, pkg=pkg)    
        return self.render_to_response(context)


def proglam_edit(request, pkg_id, proglam_id=None):
    """proglamの編集"""
    pkg = get_object_or_404(Pkg, pk=pkg_id)  # 親の書籍を読む
    if proglam_id:   # impression_id が指定されている (修正時)
        proglam = get_object_or_404(Proglam, pk=proglam_id)
    else:               # impression_id が指定されていない (追加時)
        proglam = Proglam()

    if request.method == 'POST':
        form = ProglamForm(request.POST, instance=proglam)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            proglam = form.save(commit=False)
            proglam.link = pkg  # この感想の、親の書籍をセット
            proglam.save()
            return redirect('data_base:proglam_list', pkg_id=pkg_id)
    else:    # GET の時
        form = ProglamForm(instance=proglam)  # impression インスタンスからフォームを作成

    return render(request,
                  'data_base/proglam_edit.html',
                  dict(form=form, pkg_id=pkg_id, proglam_id=proglam_id))

def proglam_del(request, pkg_id, proglam_id):
    """proglam"""
    proglam = get_object_or_404(Proglam, pk=proglam_id)
    proglam.delete()
    return redirect('data_base:proglam_list', pkg_id=pkg_id)


class FunctionList(ListView):
    """functionの一覧"""
    context_object_name='functions'
    template_name='data_base/function_list.html'
    paginate_by = 10  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        proglam = get_object_or_404(Proglam, pk=kwargs['proglam_id'])  # 親の書籍を読む
        functions = proglam.functions.all().order_by('id')   # 書籍の子供の、感想を読む
        self.object_list = functions

        context = self.get_context_data(object_list=self.object_list, proglam=proglam) 
        return self.render_to_response(context)


def function_edit(request, proglam_id, function_id=None):
    """感想の編集"""
    proglam = get_object_or_404(Proglam, pk=proglam_id)  # 親の書籍を読む
    if function_id:   # impression_id が指定されている (修正時)
        function = get_object_or_404(Function, pk=function_id)
    else:               # impression_id が指定されていない (追加時)
        function = Function()

    if request.method == 'POST':
        form = FunctionForm(request.POST, instance=function)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            function = form.save(commit=False)
            function.link = proglam  # この感想の、親の書籍をセット
            function.save()
            return redirect('data_base:function_list', proglam_id=proglam_id)
    else:    # GET の時
        form = FunctionForm(instance=function)  # impression インスタンスからフォームを作成

    return render(request,
                  'data_base/function_edit.html',
                  dict(form=form, proglam_id=proglam_id, function_id=function_id))


def function_del(request, proglam_id, function_id):
    """functionの削除"""
    function = get_object_or_404(Function, pk=function_id)
    function.delete()
    return redirect('data_base:function_list', proglam_id=proglam_id)
#    return HttpResponse('keseta')


def function_view(request, function_id):
    """function syousai"""
#    return HttpResponse('functionのsyousai')
    function = get_object_or_404(Function, pk=function_id)
    return render(request, 'data_base/function_view.html', dict(function=function))


def pkg_del_check(request, target_id):
    return render(request, 'data_base/pkg_del_check.html',dict(target_id=target_id))


def func_del_check(request, target_id, link_id=None):
    return render(request, 'data_base/func_del_check.html',dict(target_id=target_id, link_id=link_id))


def pro_del_check(request, target_id, link_id=None):
#    return HttpResponse('pkgの一覧')
#    target = get_object_or_404(Function, pk=target_id)
    return render(request, 'data_base/pro_del_check.html',dict(target_id=target_id, link_id=link_id))


