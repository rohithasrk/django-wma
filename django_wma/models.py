from .base.models import (AbstractContainer, AbstractWaterQuantity,
                         AbstractWaterQuality)
import swapper

class Container(AbstractContainer):
    class Meta(AbstractContainer.Meta):
        swappable = swapper.swappable_setting('django_wma', 'Container')
        abstract = False


class WaterQuantity(AbstractWaterQuantity):
    class Meta(AbstractWaterQuantity.Meta):
        swappable = swapper.swappable_setting('django_wma', 'WaterQuantity')
        abstract = False


class WaterQuality(AbstractWaterQuality):
    class Meta(AbstractWaterQuality.Meta):
        swappable = swapper.swappable_setting('django_wma', 'WaterQuality')
        abstract = False