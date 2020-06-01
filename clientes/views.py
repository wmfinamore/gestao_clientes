from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Person
from .models import Produto
from .models import Venda
from .forms import PersonForm


@login_required
def Persons_list(request):
    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)
    footer_message = 'Desenvolvimento web com Django 2.2.10 - WMF'

    if nome or sobrenome:
        persons = Person.objects.all()
        persons = persons.filter(first_name__icontains=nome, last_name__icontains=sobrenome)
    else:
        persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons, 'footer_message': footer_message})


@login_required
def Persons_new(request):
    form = PersonForm(request.POST, request.FILES, None)
    footer_message = 'Desenvolvimento web com Django 2.2.10 - WMF'
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form, 'footer_message': footer_message})

@login_required
def Persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    footer_message = 'Desenvolvimento web com Django 2.2.10 - WMF'

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form, 'footer_message': footer_message})

@login_required
def Persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_confirm_delete.html', {'person': person})


class PersonList(ListView):
    model = Person


class PersonDetail(DetailView):
    model = Person
    """Overrride de método nativo: forçou o Django realizar um left join
    da tabela documentos, reduzindo um select em tempo de execução."""
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['now'] = timezone.now()
        context['vendas'] = Venda.objects.filter(pessoa_id=self.object.id)
        return context

class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list/'


class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_cbv')


class PersonDelete(DeleteView):
    model = Person
    # success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return reverse_lazy('person_list_cbv')


class ProdutoBulk(View):
    def get(self, request, *args, **kwargs):
        produtos = ['Banana', 'Maça', 'Limão', 'Laranja', 'Pera', 'Melancia']
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)

        Produto.objects.bulk_create(list_produtos)

        return HttpResponse('Funcionou')
