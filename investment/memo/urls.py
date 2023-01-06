from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^stock-memo/create[/]?$", views.create_stock_memo),
    re_path(r"^stock-memo/read[/]?$", views.read_stock_memo),
    re_path(r"^stock-memo/update[/]?$", views.update_stock_memo),
    re_path(r"^stock-memo/delete[/]?$", views.delete_stock_memo),
    re_path(r"^trade-plan/create[/]?$", views.create_trade_plan),
    re_path(r"^trade-plan/read[/]?$", views.read_trade_plan),
    re_path(r"^trade-plan/update[/]?$", views.update_trade_plan),
    re_path(r"^trade-plan/delete[/]?$", views.delete_trade_plan),
]
