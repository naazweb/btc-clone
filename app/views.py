from django.shortcuts import render

from app.utils import get_transaction_info, get_home_page_content, get_latest_blocks

# Create your views here.


def home(request):

    stats = get_home_page_content()
    transaction = get_transaction_info(
        'b6f6991d03df0e2e04dafffcd6bc418aac66049e2cd74b80f14ac86db1e3f0da')
    blocks = get_latest_blocks()
    context = {'stats': stats, 'transaction': transaction, 'blocks': blocks}
    return render(request, 'index.html', context=context)


def transaction_data(request, txn_hash):
    print(txn_hash)
    transaction = get_transaction_info(txn_hash)
    context = {'transaction': transaction}
    return render(request, 'transaction.html', context=context)
