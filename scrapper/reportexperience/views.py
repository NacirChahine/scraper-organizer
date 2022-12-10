from django.shortcuts import render
from django.db.models import Q
from datetime import timedelta, datetime
from django_renderpdf.views import PDFView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_renderpdf import helpers
from django.shortcuts import redirect
import pickle
from Sector.models import Company, ChildCompany
import os
from Worker.models import Experience

os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")


# from weasyprint import HTML


##############################################################
def getCompanyExperience(request, company_id):
    expes = Experience.objects.filter(company_id=company_id)
    expeslist = []

    if expes.count() == 0:
        data = pickle.dumps(expeslist).hex()
        request.session['expes'] = data
        return expeslist
    for expe in expes:
        expe1 = {
            'id': expe.id,
            'company': expe.company.name,
            'contact': expe.contact.name,
            'fromDate': expe.fromDate,
            'toDate': expe.toDate,
            'role': expe.role,
        }
        expeslist.append(expe1)

        data = pickle.dumps(expeslist).hex()

        request.session['expes'] = data

    return expeslist


def getAllCompanyexpes(request, ):
    if not request.user.is_authenticated:
        return render(request, "error-page.html", {})
    if 'frmprint' in request.POST:
        response = redirect('company_experiences_print')
        return response

    elif 'experiences_of_company' in request.POST:

        if 'company' in request.POST:
            company = request.POST['company']

            company = Company.objects.filter(id=int(company))[0]
            expes = getCompanyExperience(request, company)

        else:
            company = ''
            expes = ''

        companyName = company.name
        request.session['companyName'] = companyName
        # request.session['childs'] = childs

        data = {
            'company': company,
            'expes': expes,
        }

        return render(request, "reports/CompanyExperience/companyexperienceresult.html", data)
    else:
        allCompanies = Company.objects.all()
        data = {
            'allCompanies': allCompanies
        }
        return render(request, "reports/CompanyExperience/companyexperience.html", data)


class printAllCompanyChildren(LoginRequiredMixin, PDFView):
    template_name = 'reports/CompanyExperience/companyexperienceprint.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        expes = pickle.loads(bytes.fromhex(self.request.session['expes']))
        company = self.request.session['companyName']

        cont = {
            'expes': expes,
            'company': company,
        }
        # context['auctions'] = cont

        return cont
