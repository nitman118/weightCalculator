from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, "converter/converter_home.html")

def convert(request):

    input_weight = float(request.GET.get('input-weight') or 0)
    weight_from = str(request.GET.get('weight-from'))
    weight_to = str(request.GET.get('weight-to'))
    weight = input_weight

    if weight_from == 'kg' and weight_to == 'lb':
        weight = input_weight * 2.20462

    elif weight_from == 'lb' and weight_to == 'kg':
        weight = input_weight * (1/2.20462)

    else:
        weight = weight


    return render(request, "converter/converted.html", {'input_weight':input_weight, 'weight':round(weight,2), 'weight_from':weight_from, 'weight_to':weight_to})
