from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.views.generic import TemplateView
from datetime import datetime

from app.erp.models import Sale


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_graph_sales_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                #se debe validar Coalesce que es una funcion que indica que si el valor es none retorna 0
                #total = Sale.objects.filter(date_joined__year=year, date_joined__month=m).aggregate(r=Coalesce(Sum('total'), 0)).get('r')
                total = Sale.objects.filter(date_joined__year=year,date_joined__month=m).aggregate(r=Sum('total')).get('r')
                if total is None:
                    total = 0
                data.append(float(total))
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['graph_sales_year_month'] = self.get_graph_sales_year_month()
        return context