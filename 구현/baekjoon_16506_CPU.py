# ----------------------------------------------------------------------------
# [baekjoon_16506] CPU 
# ----------------------------------------------------------------------------
opcode_dict = {"ADD":"0000", "SUB":"0001","MOV":"0010", "AND":"0011", "OR":"0100", "NOT":"0101", "MULT":"0110", "LSFTL":"0111", 
"LSFTR":"1000", "ASFTR":"1001", "RL":"1010", "RR":"1011"}

# 명령어 개수
N = int(input())

result = []
for _ in range(N):
    machine_code = ""
    string = input().split()
    opcode = string[0]
    rD = string[1]
    rA = string[2]
    rB = string[3]
    
    # opcdoe에 마지막 C가 존재하면 4번(5번째) bit 1
    if opcode[-1] == "C":
        machine_code += opcode_dict[opcode[:-1]]
        machine_code += "1"
    else:
        machine_code += opcode_dict[opcode]
        machine_code += "0"

    machine_code += "0"

    machine_code += str(bin(int(rD)))[2:].zfill(3)
    machine_code += str(bin(int(rA)))[2:].zfill(3)

    # 4번 비트가 0이면 rB + "0", 1이면 #C
    if machine_code[4] == "0":
        machine_code += str(bin(int(rB)))[2:].zfill(3)
        machine_code += "0"
    else:
        machine_code += str(bin(int(rB)))[2:].zfill(3)

    result.append(machine_code)

print("\n".join(result))