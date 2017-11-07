# coding=utf-8
# created by czc on 2017.7.31
import re

a = "50g"
if re.match(r"\d+\w{0,2}", a):
    print(a, " 无意义。")
a = "500ml"
if re.match(r"\d+\w{0,2}", a):
    print(a, " 无意义。")
a = "13"
if re.match(r"\d+\w{0,2}", a):
    print(a, " 无意义。")
a = "到货"
if re.match(r"\d+\w{0,2}", a):
    print(a, " 无意义。")
a = "24味的糖啊"
if re.match(r"\d+\w{0,2}$", a):
        print(a, " 无意义。")
a = "24ml"
if re.match(r"\d+\w{0,2}$", a):         # $ 完全匹配
        print(a, " 无意义。")
a = "24g*3"
if re.match(r"\d+\w{0,2}\W*\d*$", a):
        print(a, " 无意义。")
a = "13"
if re.match(r"\d+\w{0,2}\W*\d*$", a):
    print(a, " 无意义。")
a = "到货"
if re.match(r"\d+\w{0,2}\W*\d*$", a):
    print(a, " 无意义。")
a = "24味的糖啊"
if re.match(r"\d+\w{0,2}\W*\d*$", a):
        print(a, " 无意义。")
a = "24ml"
if re.match(r"\d+\w{0,2}\W*\d*$", a):         # $ 完全匹配
        print(a, " 无意义。")
a = "50g"
if re.match(r"\d+\w{0,2}\W*\d*$", a):
    print(a, " 无意义。")
a = "UK"
if re.match(r"\d+\w{0,2}\W*\d*$", a):
    print(a, " 无意义。")