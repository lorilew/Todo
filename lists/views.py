from django.shortcuts import render

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        print(request.POST)
        new_list_item = request.POST.get('item_text')
        return render(request, 'home.html', {'new_list_item': new_list_item})
    else:
        return render(request, 'home.html', {'new_list_item': ''})

