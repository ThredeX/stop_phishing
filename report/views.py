from django.shortcuts import redirect, render

from .models import PhishingUrl
from .forms import PhishingUrlForm


def home(req):
    match req.method:
        case 'GET':
            form = PhishingUrlForm()
        case 'POST':
            form = PhishingUrlForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect('report:success')
    return render(
        req,
        'report/home.html',
        {
            'amount': PhishingUrl.objects.filter(is_verified=True).count(),
            'form': form
        }
    )


def success(req):
    return render(req, 'report/success.html')
