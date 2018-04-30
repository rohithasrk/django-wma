from django.shortcuts import get_object_or_404, render_to_response
from django.views import View
from django_wma.models import Container, WaterQuality, WaterQuantity


class ContainerListView(View):
    def get(self, request):
        containers = Container.objects.all()
        return render_to_response('wma/list.html', {'containers': containers})


class ContainerDetailView(View):
    def get(self, request, pk):
        container = Container.objects.get(pk=pk)
        water_quality = WaterQuality.objects.get(container=container)
        water_quantity = WaterQuantity.objects.get(container=container)
        return render_to_response('wma/detail.html', {
            'container': container,
            'water_quality': water_quality,
            'water_quantity': water_quantity
        })

container_list = ContainerListView.as_view()
container_detail = ContainerDetailView.as_view()