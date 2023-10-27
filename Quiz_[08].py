rrn = input("주민등록번호: ")
result1 = int(rrn[0]) * 2 + int(rrn[1]) * 3 + int(rrn[2]) * 4 + int(rrn[3]) * 5 + int(rrn[4]) * 6 + int(rrn[5]) * 7 + int(rrn[7]) * 8 + int(rrn[8]) * 9 + int(rrn[9]) * 2 + int(rrn[10])* 3 + int(rrn[11])* 4 + int(rrn[12]) * 5
result2 = 11 - (result1 % 11)
result3 = str(result2)

if rrn[-1] == result3[-1]:
    print(f"주민등록번호 {rrn}은 맞는 주민번호입니다!")
else:
    print(f"주민등록번호 {rrn}은 틀린 주민번호입니다!")
