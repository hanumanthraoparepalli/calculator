
from django.urls import path

from . import views



urlpatterns = [
    
    path('', views.home, name = 'home'),

    path('add', views.add, name = 'add'),
    
    path('sub', views.sub, name = 'sub'),

    path('mul', views.mul, name = 'mul'),

    path('div', views.div, name = 'div'),

    path('lcm', views.lcm, name = 'lcm'),

    path('gcd', views.gcd, name = 'gcd'),

    path('fact', views.fact, name = 'fact'),

    path('fib', views.fib, name = 'fib'),

    path('mean', views.mean, name = 'mean'),

    path('median', views.median, name = 'median'),

    path('mode', views.mode, name = 'mode'),

    path('std', views.std, name = 'std'),

    path('avg', views.avg, name = 'avg'),

    path('power', views.power, name = 'power'),






]

