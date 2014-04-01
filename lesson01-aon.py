__author__ = 'madeira'
def decode(code):
    decodeString = ""
    string = ""
    flag = False
    for i in code:
        if string == "":
            string += i
        elif string == i:
            if decodeString == "":
                if i != '#':
                    decodeString += i
                    string = i
                    flag = False
            elif i == "#":
                if flag:
                    decodeString += decodeString[-1]
                    string = i
                    flag = False
            elif string == decodeString[-1]:
                if flag:
                    decodeString += i
                    flag = False
            else:
                decodeString += i
                flag = False
        elif string != i:
            string = i
            flag = True
    return decodeString

assert decode('#####11######') == '11'
assert decode('11122234###5511122234###55') == '12251225'
assert decode('11122234###55') == '1225'
assert decode('11#####11######') == '1111'
assert decode('111122222211111') == '121'
assert decode('11##11##') == '1111'
assert decode('125521212555') == '55'
assert decode('12121212') == ''
assert decode('111111111') == '1'
assert decode('11111111111222222222') == "12"
assert decode('111222') == '12'
assert decode('11222') == '12'
assert decode('11122') == '12'
assert decode('111222') == '12'
assert decode('12211122111222') == '21212'
assert decode('1211') == '1'
assert decode('1221') == '2'
assert decode('112') == '1'
assert decode('122') == '2'
assert decode('#') == ''
assert decode('1') == ''
assert decode('') == ''
assert decode('1122') == "12"
