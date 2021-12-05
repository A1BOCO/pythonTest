
def addBinary(binary1, binary2):
    result='0'
    return addBinaryHelper(binary1, binary2, result)

def addBinaryHelper(binary1,binary2,result):

    while len(binary1) > 0 or len(binary2) > 0:
        if int(binary1[-1]) + int(binary2[-1]) + int(result[0]) == 0:
            result = '00' + result[1:]
        elif int(binary1[-1]) + int(binary2[-1]) + int(result[0]) == 1:
            result = '01' + result[1:]
        elif int(binary1[-1]) + int(binary2[-1])+ int(result[0])  == 2:
            result = '10' + result[1:]
        elif int(binary1[-1]) + int(binary2[-1]) + int(result[0]) == 3:
            result = '11' + result[1:]
        binary1 = binary1[:-1]
        binary2 = binary2[:-1]
    if result[0] == '0':
        return result[1:]
    return result
print(addBinary('1111','1111'))