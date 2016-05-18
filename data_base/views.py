#!coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from data_base.models import data_basedata, Pkg, Proglam, Function, Pkg_updated, Proglam_updated, Function_updated
from data_base.forms import PkgForm, ProglamForm, FunctionForm, PkgupdatedForm, ProglamupdatedForm, FunctionupdatedForm
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


def pkgupdated_edit(request, pkg_id, pkgupdated_id=None):
    """proglamの編集"""
    pkg = get_object_or_404(Pkg, pk=pkg_id)  # 親の書籍を読む
    if pkgupdated_id:   # impression_id が指定されている (修正時)
        pkgupdated = get_object_or_404(Pkg_updated, pk=pkgupdated_id)
    else:               # impression_id が指定されていない (追加時)
        pkgupdated = Pkg_updated()

    if request.method == 'POST':
        form = PkgupdatedForm(request.POST, instance=pkgupdated)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            pkgupdated = form.save(commit=False)
            pkgupdated.link = pkg  # この感想の、親の書籍をセット
            pkgupdated.save()
            return redirect('data_base:pkgupdated_list', pkg_id=pkg_id)
    else:    # GET の時
        form = PkgupdatedForm(instance=pkgupdated)  # impression インスタンスからフォームを作成

    return render(request,
                  'data_base/pkgupdated_edit.html',
                  dict(form=form, pkg_id=pkg_id, pkgupdated_id=pkgupdated_id))


class PkgUpdatedList(ListView):
    """proglamの一覧"""
    context_object_name='pkgupdateds'
    template_name='data_base/pkg_updated_list.html'
    paginate_by = 10  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        pkg = get_object_or_404(Pkg, pk=kwargs['pkg_id'])  # 親の書籍を読む
        pkgupdateds = pkg.pkg_updateds.all().order_by('-id')   # 書籍の子供の、感想を読む
        self.object_list = pkgupdateds

        context = self.get_context_data(object_list=self.object_list, pkg=pkg)
        return self.render_to_response(context)

 
def pkgupdated_del(request, pkg_id, pkgupdated_id):
    """proglam"""
    pkgupdated = get_object_or_404(Pkg_updated, pk=pkgupdated_id)
    pkgupdated.delete()
    return redirect('data_base:pkgupdated_list', pkg_id=pkg_id)


def proglamupdated_edit(request, proglam_id, proglamupdated_id=None):
    """proglamの編集"""
    proglam = get_object_or_404(Proglam, pk=proglam_id)  # 親の書籍を読む
    if proglamupdated_id:   # impression_id が指定されている (修正時)
        proglamupdated = get_object_or_404(Proglam_updated, pk=proglamupdated_id)
    else:               # impression_id が指定されていない (追加時)
        proglamupdated = Proglam_updated()

    if request.method == 'POST':
        form = ProglamupdatedForm(request.POST, instance=proglamupdated)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            proglamupdated = form.save(commit=False)
            proglamupdated.link = proglam  # この感想の、親の書籍をセット
            proglamupdated.save()
            return redirect('data_base:proglamupdated_list', proglam_id=proglam_id)
    else:    # GET の時
        form = ProglamupdatedForm(instance=proglamupdated)  # impression インスタンスからフォームを作成

    return render(request,
                  'data_base/proglamupdated_edit.html',
                  dict(form=form, proglam_id=proglam_id, proglamupdated_id=proglamupdated_id))


class ProglamUpdatedList(ListView):
    """proglamの一覧"""
    context_object_name='proglamupdateds'
    template_name='data_base/proglam_updated_list.html'
    paginate_by = 10  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        proglam = get_object_or_404(Proglam, pk=kwargs['proglam_id'])  # 親の書籍を読む
        proglamupdateds = proglam.proglam_updateds.all().order_by('-id')   # 書籍の子供の、感想を読む
        self.object_list = proglamupdateds

        context = self.get_context_data(object_list=self.object_list, proglam=proglam)
        return self.render_to_response(context)

 
def proglamupdated_del(request, proglam_id, proglamupdated_id):
    """proglam"""
    proglamupdated = get_object_or_404(Proglam_updated, pk=proglamupdated_id)
    proglamupdated.delete()
    return redirect('data_base:proglamupdated_list', proglam_id=proglam_id)


def functionupdated_edit(request, function_id, functionupdated_id=None):
    """proglamの編集"""
    function = get_object_or_404(Function, pk=function_id)  # 親の書籍を読む
    if functionupdated_id:   # impression_id が指定されている (修正時)
        functionupdated = get_object_or_404(Function_updated, pk=functionupdated_id)
    else:               # impression_id が指定されていない (追加時)
        functionupdated = Function_updated()

    if request.method == 'POST':
        form = FunctionupdatedForm(request.POST, instance=functionupdated)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            functionupdated = form.save(commit=False)
            functionupdated.link = function  # この感想の、親の書籍をセット
            functionupdated.save()
            return redirect('data_base:functionupdated_list', function_id=function_id)
    else:    # GET の時
        form = FunctionupdatedForm(instance=functionupdated)  # impression インスタンスからフォームを作成

    return render(request,
                  'data_base/functionupdated_edit.html',
                  dict(form=form, function_id=function_id, functionupdated_id=functionupdated_id))


class FunctionUpdatedList(ListView):
    """proglamの一覧"""
    context_object_name='functionupdateds'
    template_name='data_base/function_updated_list.html'
    paginate_by = 10  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        function = get_object_or_404(Function, pk=kwargs['function_id'])  # 親の書籍を読む
        functionupdateds = function.function_updateds.all().order_by('-id')   # 書籍の子供の、感想を読む
        self.object_list = functionupdateds

        context = self.get_context_data(object_list=self.object_list, function=function)
        return self.render_to_response(context)

 
def functionupdated_del(request, function_id, functionupdated_id):
    """proglam"""
    functionupdated = get_object_or_404(Function_updated, pk=functionupdated_id)
    functionupdated.delete()
    return redirect('data_base:functionupdated_list', function_id=function_id)


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


def pkgupdated_del_check(request, target_id, link_id=None):
    return render(request, 'data_base/pkgupdated_del_check.html',dict(target_id=target_id, link_id=link_id))


def proglamupdated_del_check(request, target_id, link_id=None):
    return render(request, 'data_base/proglamupdated_del_check.html',dict(target_id=target_id, link_id=link_id))


def functionupdated_del_check(request, target_id, link_id=None):
    return render(request, 'data_base/functionupdated_del_check.html',dict(target_id=target_id, link_id=link_id))


