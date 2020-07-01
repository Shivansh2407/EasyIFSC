from django.http import JsonResponse
from django.views import View

from .models import Bank, Branch

from .serializers import BranchSerializer

class DetailView(View):
    def get(self, request, ifsc):
        branch = Branch.objects.filter(ifsc__iexact=ifsc).first()
        serializer = BranchSerializer(branch)
        return JsonResponse(serializer.data, safe=False)


class ListView(View):
    def get(self, request, city, bank):
        branch_group = Branch.objects.filter(
            city__iexact=city, bank__name__icontains=bank
            )
        serializer = BranchSerializer(branch_group, many=True)
        return JsonResponse(serializer.data, safe=False)

