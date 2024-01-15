from django.urls import path

from .views import DepositMoneyView, WithdrawMoneyView, TransactionRepostView, home, about, services, contact


app_name = 'transactions'


urlpatterns = [
    path("index/", home, name="index"),
    path("about/", about, name= "about"),
    path("services/", services, name= "services"),
    path("contact/", contact, name="contact"),
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionRepostView.as_view(), name="transaction_report"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
]
