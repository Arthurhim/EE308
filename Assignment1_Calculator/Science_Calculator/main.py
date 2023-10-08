import re
import tkinter as tk
import math

root = tk.Tk()
root.title('Calculator v2.0')
root.geometry('380x336+700+400')

root.attributes("-alpha", 0.9)
root["background"] = "#ffffff"

font_result = ('楷体', 21)
font_key = ('楷体', 15)

# 初始化变量
result_num = tk.StringVar()
result_num.set('0')
calculate_done = False
#
tk.Label(root,
         textvariable=result_num, font=font_result, height=2,
         width=26, justify=tk.LEFT, anchor=tk.SE
         ).grid(row=1, column=1, columnspan=5)
#
button_sin = tk.Button(root, text="sin", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_cos = tk.Button(root, text="cos", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_tan = tk.Button(root, text="tan", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_rad = tk.Button(root, text="rad", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_deg = tk.Button(root, text="deg", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')


button_sin.grid(row=2, column=1, padx=3, pady=2)
button_cos.grid(row=2, column=2, padx=3, pady=2)
button_tan.grid(row=2, column=3, padx=3, pady=2)
button_rad.grid(row=2, column=4, padx=3, pady=2)
button_deg.grid(row=2, column=5, padx=3, pady=2)

# 按钮第一行

#
button_log = tk.Button(root, text="log", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_ln = tk.Button(root, text="ln", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_left_bracket = tk.Button(root, text="(", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_right_bracket = tk.Button(root, text=")", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_inv = tk.Button(root, text="inv", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')


button_log.grid(row=3, column=1, padx=3, pady=2)
button_ln.grid(row=3, column=2, padx=3, pady=2)
button_left_bracket.grid(row=3, column=3, padx=3, pady=2)
button_right_bracket.grid(row=3, column=4, padx=3, pady=2)
button_inv.grid(row=3, column=5, padx=3, pady=2)

# 按钮第二行

#
button_factorial = tk.Button(root, text="!", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_clear = tk.Button(root, text="C", width=6, font=font_key, relief=tk.FLAT, bg='#b1b2b2')
button_percent = tk.Button(root, text="%", width=6, font=font_key, relief=tk.FLAT, bg='#b1b2b2')
button_back = tk.Button(root, text="←", width=6, font=font_key, relief=tk.FLAT, bg='#b1b2b2')
button_division = tk.Button(root, text="÷", width=6, font=font_key, relief=tk.FLAT, bg='#b1b2b2')


button_factorial.grid(row=4, column=1, padx=3, pady=2)
button_clear.grid(row=4, column=2, padx=3, pady=2)
button_percent.grid(row=4, column=3, padx=3, pady=2)
button_back.grid(row=4, column=4, padx=3, pady=2)
button_division.grid(row=4, column=5, padx=3, pady=2)

# 按钮第三行

#
button_power = tk.Button(root, text="^", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_seven = tk.Button(root, text="7", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_eight = tk.Button(root, text="8", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_nine = tk.Button(root, text="9", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_multiplication = tk.Button(root, text="×", width=6, font=font_key, relief=tk.FLAT, bg='#b1b2b2')


button_power.grid(row=5, column=1, padx=3, pady=2)
button_seven.grid(row=5, column=2, padx=3, pady=2)
button_eight.grid(row=5, column=3, padx=3, pady=2)
button_nine.grid(row=5, column=4, padx=3, pady=2)
button_multiplication.grid(row=5, column=5, padx=3, pady=2)

# 按钮第四行

#
button_square_root = tk.Button(root, text="√￣", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_four = tk.Button(root, text="4", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_five = tk.Button(root, text="5", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_six = tk.Button(root, text="6", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_subtraction = tk.Button(root, text="-", width=6, font=font_key, relief=tk.FLAT, bg='#b1b2b2')


button_square_root.grid(row=6, column=1, padx=3, pady=2)
button_four.grid(row=6, column=2, padx=3, pady=2)
button_five.grid(row=6, column=3, padx=3, pady=2)
button_six.grid(row=6, column=4, padx=3, pady=2)
button_subtraction.grid(row=6, column=5, padx=3, pady=2)
# 按钮第五行

#
button_pi = tk.Button(root, text="π", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_one = tk.Button(root, text="1", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_two = tk.Button(root, text="2", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_three = tk.Button(root, text="3", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_addition = tk.Button(root, text="+", width=6, font=font_key, relief=tk.FLAT, bg='#b1b2b2')


button_pi.grid(row=7, column=1, padx=3, pady=2)
button_one.grid(row=7, column=2, padx=3, pady=2)
button_two.grid(row=7, column=3, padx=3, pady=2)
button_three.grid(row=7, column=4, padx=3, pady=2)
button_addition.grid(row=7, column=5, padx=3, pady=2)
# 按钮第六行

#
button_e = tk.Button(root, text="e", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_D_zero = tk.Button(root, text="00", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_zero = tk.Button(root, text="0", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_dot = tk.Button(root, text=".", width=6, font=font_key, relief=tk.FLAT, bg='#eacda1')
button_equivalence = tk.Button(root, text="=", width=6, font=font_key, relief=tk.FLAT, bg='#faa755')


button_e.grid(row=8, column=1, padx=3, pady=2)
button_D_zero.grid(row=8, column=2, padx=3, pady=2)
button_zero.grid(row=8, column=3, padx=3, pady=2)
button_dot.grid(row=8, column=4, padx=3, pady=2)
button_equivalence.grid(row=8, column=5, padx=3, pady=2)


# 按钮第七行

with open('rad_deg.txt', 'a+') as File:
    File.seek(0)
    content = File.read()
    if content == "":
        content = "deg"
    if content == "deg":
        button_deg.config(fg="red")
    if content == "rad":
        button_rad.config(fg="red")
    File.close()

with open('inv_config.txt', 'a+') as File:
    File.seek(0)
    mode = File.read()
    if mode == "":
        mode = "1"
    if mode == "-1":
        button_inv.config(fg="red")
        button_sin.config(text="sin⁻¹")
        button_cos.config(text="cos⁻¹")
        button_tan.config(text="tan⁻¹")
        button_ln.config(text="e^")
        button_log.config(text="10^")
        button_square_root.config(text="x²")
    File.close()


def click_button(x):
    global calculate_done
    if result_num.get() == '0':
        result_num.set(x)
        calculate_done = False
    elif calculate_done:
        if x == '+' or x == "-" or x == "*" or x == "/":
            result_num.set(result_num.get() + x)
        else:
            result_num.set(x)
        calculate_done = False
    else:
        result_num.set(result_num.get()+x)


def calculation():
    opt_str = result_num.get()

    if content == "rad":
        # 正函数
        opt_str = opt_str.replace("sin(", "math.sin(")
        opt_str = opt_str.replace("cos(", "math.cos(")
        opt_str = opt_str.replace("tan(", "math.tan(")
        # 反函数
        opt_str = opt_str.replace("sin⁻¹(", "math.asin(")
        opt_str = opt_str.replace("cos⁻¹(", "math.acos(")
        opt_str = opt_str.replace("tan⁻¹(", "math.atan(")
    elif content == "deg":
        # 正函数
        opt_str = opt_str.replace("sin(", "math.sin(math.pi * (1/180) * ")
        opt_str = opt_str.replace("cos(", "math.cos(math.pi * (1/180) * ")
        opt_str = opt_str.replace("tan(", "math.tan(math.pi * (1/180) * ")
        # 反函数
        opt_str = opt_str.replace("sin⁻¹(", "math.asin(math.pi * (1/180) * ")
        opt_str = opt_str.replace("cos⁻¹(", "math.acos(math.pi * (1/180) * ")
        opt_str = opt_str.replace("tan⁻¹(", "math.atan(math.pi * (1/180) * ")

    opt_str = opt_str.replace("log(", "math.log10(")
    opt_str = opt_str.replace("ln(", "math.log(")

    opt_str = opt_str.replace("×", "*")
    opt_str = opt_str.replace("÷", "/")
    opt_str = opt_str.replace("^", "**")
    opt_str = opt_str.replace("%", "*0.01")

    opt_str = opt_str.replace("π", "math.pi")
    opt_str = opt_str.replace("e", "math.e")

    opt_str = factorial(opt_str)
    opt_str = square_root(opt_str)
    # print(opt_str)  # debug

    try:
        result = eval(opt_str)
        result_num.set(str(round(result, 14)))  # 去掉最后一位，以纠正浮点型误差
    except Exception as e:
        result_num.set("error")

    global calculate_done  # 标记计算完毕（若下一次计算开始，则清屏）
    calculate_done = True


def change_tri_mode(s):
    global content
    with open('rad_deg.txt', 'a+')as file:
        file.seek(0)
        file.truncate(0)
        if s == "rad":
            content = "rad"
            file.write("rad")
            button_rad.config(fg="red")
            button_deg.config(fg="black")
        elif s == "deg":
            content = "deg"
            file.write("deg")
            button_rad.config(fg="black")
            button_deg.config(fg="red")
        file.close()


def change_inv_mode():
    global mode
    with open('inv_config.txt', 'a+')as file:
        file.seek(0)
        file.truncate(0)
        if mode == "1":
            mode = "-1"
            file.write("-1")
            button_inv.config(fg="red")
            button_sin.config(text="sin⁻¹", command=lambda: click_button('sin⁻¹('))
            button_cos.config(text="cos⁻¹", command=lambda: click_button('cos⁻¹('))
            button_tan.config(text="tan⁻¹", command=lambda: click_button('tan⁻¹('))
            button_ln.config(text="e^", command=lambda: click_button('e^'))
            button_log.config(text="10^", command=lambda: click_button('10^'))
            button_square_root.config(text="x²", command=lambda: click_button('^2'))
        elif mode == "-1":
            mode = "1"
            file.write("1")
            button_inv.config(fg="black")
            button_sin.config(text="sin", command=lambda: click_button('sin('))
            button_cos.config(text="cos", command=lambda: click_button('cos('))
            button_tan.config(text="tan", command=lambda: click_button('tan('))
            button_ln.config(text="ln", command=lambda: click_button('ln('))
            button_log.config(text="log", command=lambda: click_button('log('))
            button_square_root.config(text="√￣", command=lambda: click_button('√'))
        file.close()


def factorial(s):
    count_fac = s.count("!")
    if count_fac == 0:
        return s

    pattern = r'\b\d+!?\b'
    matches = re.findall(pattern, s)
    for match in matches:
        num = int(match)
        num = math.factorial(num)
        s = s.replace(match+"!", str(num), 1)
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


def clear():
    result_num.set('0')


def back():
    global calculate_done

    result_num.set(result_num.get()[:-1])
    calculate_done = False


button_one.config(command=lambda: click_button('1'))
button_two.config(command=lambda: click_button('2'))
button_three.config(command=lambda: click_button('3'))
button_four.config(command=lambda: click_button('4'))
button_five.config(command=lambda: click_button('5'))
button_six.config(command=lambda: click_button('6'))
button_seven.config(command=lambda: click_button('7'))
button_eight.config(command=lambda: click_button('8'))
button_nine.config(command=lambda: click_button('9'))
button_zero.config(command=lambda: click_button('0'))
button_D_zero.config(command=lambda: click_button('00'))
button_pi.config(command=lambda: click_button('π'))
button_e.config(command=lambda: click_button('e'))

button_addition.config(command=lambda: click_button('+'))
button_subtraction.config(command=lambda: click_button('-'))
button_multiplication.config(command=lambda: click_button('×'))
button_division.config(command=lambda: click_button('÷'))
button_power.config(command=lambda: click_button('^'))
button_square_root.config(command=lambda: click_button('√'))
button_factorial.config(command=lambda: click_button('!'))

button_sin.config(command=lambda: click_button('sin('))
button_cos.config(command=lambda: click_button('cos('))
button_tan.config(command=lambda: click_button('tan('))
button_rad.config(command=lambda: change_tri_mode("rad"))
button_deg.config(command=lambda: change_tri_mode("deg"))

button_log.config(command=lambda: click_button('log('))
button_ln.config(command=lambda: click_button('ln('))

if mode == "-1":
    button_sin.config(command=lambda: click_button('sin⁻¹('))
    button_cos.config(command=lambda: click_button('cos⁻¹('))
    button_tan.config(command=lambda: click_button('tan⁻¹('))
    button_log.config(command=lambda: click_button('10^'))
    button_ln.config(command=lambda: click_button('e^'))
    button_square_root.config(command=lambda: click_button('^2'))

button_left_bracket.config(command=lambda: click_button('('))
button_right_bracket.config(command=lambda: click_button(')'))
button_dot.config(command=lambda: click_button('.'))
button_percent.config(command=lambda: click_button('%'))


button_inv.config(command=change_inv_mode)
button_clear.config(command=clear)
button_equivalence.config(command=calculation)
button_back.config(command=back)

root.mainloop()
