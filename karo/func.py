from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import KaroModel
from django.urls import reverse_lazy

from django.db.models import Count, Avg, Sum, Max, Min

def defo():
    last_order = KaroModel.objects.order_by("id").last()

    return last_order.goleKcol