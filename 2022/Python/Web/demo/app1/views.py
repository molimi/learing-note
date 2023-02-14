from django.shortcuts import render
from django.http import HttpResponse

from random import sample

# Create your views here.
def show_index(request):
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Blueberry', 
        'Grape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    selected_fruits = sample(fruits, 3)
    return render(request, 'index.html', {'fruits': selected_fruits})
    '''
    content = '<h3>今天推荐的水果是：</h3>'
    content += '<hr>'
    content += '<ul>'
    for fruit in selected_fruits:
        content += f'<li>{fruit}</li>'
    content += '</ul>'
    return HttpResponse(content)
    '''