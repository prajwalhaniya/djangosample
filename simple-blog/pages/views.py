# from django.http import HttpResponse
from typing import Any
from django.views.generic import TemplateView
from django.utils import timezone
from django.shortcuts import render

def home_page_view(request):
    now = timezone.now()
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 2"],
        "greeting": "Thank you for visiting",
        "now": now
    }
    return render(request, 'pages/home.html', context)

def about_page_view(request):
    context = { "name": "Prajwal" }
    return render(request, 'pages/about.html', context)

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["company_address"] = "123 main street"
        context["phone_number"] = "12341234124"
        return context