from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def calculate(request):
    if request.method == 'POST':
        a = float(request.POST['first'])
        b = float(request.POST['second'])
        sign = request.POST['op']
        result = 0

        match sign:
            case '+': result = a + b
            case '-': result = a - b
            case '*': result = a * b
            case '/':
                if b != 0:
                    result = a / b
                else:
                    result = 'You cannot divide by Zero!'

        context = {
            'first': a,
            'second': b,
            'sign': sign,
            'result': result
        }
        return render(request, 'result.html', context)
