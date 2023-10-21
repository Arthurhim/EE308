from django.shortcuts import render
from django.http import JsonResponse
import math
import re

from .models import calData
from .models import calHistory

# Create your views here.

rad_deg = "deg"
inv = 0
count = 0


def handler(request):  # 打开计算器页
    return render(request, 'server.html')


def history(request):  # 打开历史记录页
    return render(request, 'history.html')


def calculation(request):
    global count
    if request.method == 'POST':
        formula = request.POST.get('sendFormula', '')
        record_formula = formula

        if rad_deg == "rad":
            # 正函数
            formula = formula.replace("sin(", "math.sin(")
            formula = formula.replace("cos(", "math.cos(")
            formula = formula.replace("tan(", "math.tan(")
            # 反函数
            formula = formula.replace("sin⁻¹(", "math.asin(")
            formula = formula.replace("cos⁻¹(", "math.acos(")
            formula = formula.replace("tan⁻¹(", "math.atan(")
        elif rad_deg == "deg":
            # 正函数
            formula = formula.replace("sin(", "math.sin(math.pi * (1/180) * ")
            formula = formula.replace("cos(", "math.cos(math.pi * (1/180) * ")
            formula = formula.replace("tan(", "math.tan(math.pi * (1/180) * ")
            # 反函数
            formula = formula.replace("sin⁻¹(", "180/math.pi * math.asin( ")
            formula = formula.replace("cos⁻¹(", "180/math.pi * math.acos( ")
            formula = formula.replace("tan⁻¹(", "180/math.pi * math.atan( ")

        formula = formula.replace("log(", "math.log10(")
        formula = formula.replace("ln(", "math.log(")

        formula = formula.replace("×", "*")
        formula = formula.replace("÷", "/")
        formula = formula.replace("^", "**")
        formula = formula.replace("%", "*0.01")

        formula = formula.replace("π", "math.pi")
        formula = formula.replace("e", "math.e")

        formula = factorial(formula)
        formula = square_root(formula)

        try:
            result_num = eval(formula)
            result = (str(round(result_num, 14)))  # 去掉最后一位，以纠正浮点型误差
        except Exception as e:
            result = "error!"

        # 插入历史记录到数据库
        if count < 10:  # 记录不到十条，直接加入
            count += 1
            new_history = calHistory(id=count, formula=record_formula, result=result)
            new_history.save()
        else:
            for i in range(9):  # 将二到十位置的历史记录前移一格，将新历史记录插在第十格以实现新增
                j = i+1
                next_history = calHistory.objects.get(id=j+1)
                new_formula = next_history.formula
                new_result = next_history.result
                current_history = calHistory(id=j, formula=new_formula, result=new_result)
                current_history.save()
            new_history = calHistory(id=count, formula=record_formula, result=result)
            new_history.save()

        return JsonResponse({'result': result})
    return JsonResponse({'error': 'Invalid request'})


def factorial(s):
    count_fac = s.count("!")
    if count_fac == 0:
        return s

    pattern = r'\b\d+!?\b'
    matches = re.findall(pattern, s)
    for match in matches:
        num = int(match)
        num = math.factorial(num)
        s = s.replace(match + "!", str(num), 1)
    return s


def square_root(s):
    count_squ = s.count("√")
    if count_squ == 0:
        return s

    pattern = r'\b\√?+\d\b'
    matches = re.findall(pattern, s)
    for match in matches:
        num = int(match)
        num = math.sqrt(num)
        s = s.replace("√" + match, str(num), 1)
    return s


# 设置rad_deg, inv
def set_mode(request):
    global rad_deg
    global inv
    if request.method == 'POST':
        mode_check = calData.objects.filter(id=1)
        if mode_check.exists():
            mode = mode_check.get()
            rad_deg = mode.rad_deg
            inv = mode.inv
            return JsonResponse({'rad_deg': rad_deg, 'inv': inv})
        else:
            tri_mode = calData(id=1, rad_deg="deg", inv=0)
            tri_mode.save()
            return JsonResponse({'rad_deg': rad_deg, 'inv': inv})
    return JsonResponse({'error': 'Invalid request'})


def change_tri_mode(request):
    global rad_deg
    if request.method == 'POST':
        rad_deg = request.POST.get('rad_deg', '')
        mode = calData.objects.get(id=1)
        mode.rad_deg = rad_deg
        mode.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'error': 'Invalid request'})


def change_inv_mode(request):
    global inv
    if request.method == 'POST':
        inv = request.POST.get('inv', '')
        mode = calData.objects.get(id=1)
        mode.inv = inv
        mode.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'error': 'Invalid request'})


def clear_history(request):
    if request.method == 'POST':
        for i in range(10):
            j = i + 1
            check_history = calHistory.objects.filter(id=j)
            if check_history.exists():
                find_history = check_history.get()
                find_history.delete()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'error': 'Invalid request'})


def get_history(request):
    formula_list = [None]*10
    result_list = [None]*10
    if request.method == 'POST':
        for i in range(10):
            j = i+1
            default = "/"
            check_history = calHistory.objects.filter(id=j)
            if check_history.exists():
                find_history = check_history.get()
                formula_list[i] = find_history.formula
                result_list[i] = find_history.result
            else:
                formula_list[i] = default
                result_list[i] = default
        return JsonResponse({'formula_list': formula_list, 'result_list': result_list})
    return JsonResponse({'error': 'Invalid request'})
