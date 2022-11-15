
file_input = open('canbus_canID1_hex.txt', 'r')
file_output = open('canbus_canID1_hex_res_compare_me.txt', 'w')

Lines = file_input.readlines()
for line in Lines:
    ln_num = line[2::]
    print("--------")
    print(line)
    print(ln_num)

    ln_upper = ln_num.upper()
    print(ln_upper)
    file_output.writelines(ln_upper )
    print("--------")



file_input.close()
file_output.close()
