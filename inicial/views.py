from django.shortcuts import render
from django.views.generic import View, TemplateView
from operacoes.models import RegistroSaida, RegistroEntrada


class HomeView(View):
    template_name = "home.html"
    def get(self, request):        
        saidas = RegistroSaida.objects.order_by('-diahora')[:3]
        entradas = RegistroEntrada.objects.order_by('-diahora')[:3]
        context = {            
            'saidas'     : saidas,
            'entradas' : entradas
        }
        return render(request, self.template_name, context)

class AboutView(TemplateView):
    template_name = "about.html"