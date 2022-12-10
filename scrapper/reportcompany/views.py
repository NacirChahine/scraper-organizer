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

os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")


# from weasyprint import HTML


##############################################################
def getCompanyChilds(request, company_id):
    childs = ChildCompany.objects.filter(company_id=company_id)
    childslist = []

    if childs.count() == 0:
        data = pickle.dumps(childslist).hex()
        request.session['childs'] = data
        return childslist
    for child in childs:
        # print(bid)
        child1 = {
            'id': child.id,
            'city': child.city.name,
            'nbReviews': child.nbReviews,
            'phoneNb': child.phoneNb,
            'ranking': child.ranking,
            'longitude': child.longitude,
            'latitude': child.latitude,
        }
        childslist.append(child1)

        data = pickle.dumps(childslist).hex()

        request.session['childs'] = data

    return childslist


def getAllCompanyChilds(request, ):
    if not request.user.is_authenticated:
        return render(request, "error-page.html", {})
    if 'frmprint' in request.POST:
        response = redirect('chiled_companies_print')
        return response

    elif 'children_of_company' in request.POST:

        if 'company' in request.POST:
            companyID = request.POST['company']
            company = Company.objects.filter(id=int(companyID))[0]
            childs = getCompanyChilds(request, companyID)
        else:
            company = ''
            childs = ''

        companyName = company.name
        request.session['companyName'] = companyName
        # request.session['childs'] = childs

        data = {
            'company': company,
            'childs': childs,
        }

        return render(request, "reports/CompanyChildren/companychildrenresult.html", data)
    else:
        allCompanies = Company.objects.all()
        data = {
            'allCompanies': allCompanies
        }
        return render(request, "reports/CompanyChildren/companychildren.html", data)


class printAllCompanyChildren(LoginRequiredMixin, PDFView):
    template_name = 'reports/CompanyChildren/companychildrenprint.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        childs = pickle.loads(bytes.fromhex(self.request.session['childs']))
        company = self.request.session['companyName']

        cont = {
            'childs': childs,
            'company': company,
        }
        # context['auctions'] = cont

        return cont
