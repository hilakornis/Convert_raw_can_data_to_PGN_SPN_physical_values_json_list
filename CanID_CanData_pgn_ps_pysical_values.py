import json
import binascii
import json

import bitstring
import sys
import math
from collections import OrderedDict


# DA_MASK = 0x0000EF00
DA_MASK = 0x0000FF00

SA_MASK = 0x000000FF

# PF_MASK  = 0x01FF0000
PF_MASK = 0x00FF0000

TM_MASK = 0x00EB0000
CM_MASK = 0x00EC0000
ACK_MASK = 0x0E80000

#hilak constant:
PS_MASK   = 0x0000FF0000

BIG_ENDIAN = True

ERROR_PHYSICAL = -1

DEBUG_MODE = False

file_json_file = open('json_files/truck_messages_13_11_22/truck_messages_13_11-3.json')

online_canid_pgn = [
 {
  "canid": "0xc001027",
  "online": 0
 },
 {
  "canid": "0xc000127",
  "online": 0
 },
 {
  "canid": "0xc000027",
  "online": 0
 },
 {
  "canid": "0xc000021",
  "online": 0
 },
 {
  "canid": "0xc000003",
  "online": 0
 },
 {
  "canid": "0xc000f27",
  "online": 0
 },
 {
  "canid": "0xc010a21",
  "online": 256
 },
 {
  "canid": "0xc012171",
  "online": 256
 },
 {
  "canid": "0xc010305",
  "online": 256
 },
 {
  "canid": "0x18011771",
  "online": 256
 },
 {
  "canid": "0xc040b2a",
  "online": 1024
 },
 {
  "canid": "0x18701721",
  "online": 28672
 },
 {
  "canid": "0x1887fe21",
  "online": 34560
 },
 {
  "canid": "0x18a7ff21",
  "online": 42752
 },
 {
  "canid": "0x18e00027",
  "online": 57344
 },
 {
  "canid": "0x18e0ff00",
  "online": 57344
 },
 {
  "canid": "0x18e0ff21",
  "online": 57344
 },
 {
  "canid": "0x18e0ff27",
  "online": 57344
 },
 {
  "canid": "0x18ea001d",
  "online": 59904
 },
 {
  "canid": "0x18ea0017",
  "online": 59904
 },
 {
  "canid": "0x18ea0b27",
  "online": 59904
 },
 {
  "canid": "0x18ea2117",
  "online": 59904
 },
 {
  "canid": "0x18ea0b17",
  "online": 59904
 },
 {
  "canid": "0x18ea17f9",
  "online": 59904
 },
 {
  "canid": "0x18ebff0f",
  "online": 60160
 },
 {
  "canid": "0x18ebff00",
  "online": 60160
 },
 {
  "canid": "0x18ebff10",
  "online": 60160
 },
 {
  "canid": "0x1cebff00",
  "online": 60160
 },
 {
  "canid": "0x18ecff0f",
  "online": 60416
 },
 {
  "canid": "0x18efff21",
  "online": 61184
 },
 {
  "canid": "0x18efff00",
  "online": 61184
 },
 {
  "canid": "0x18f00010",
  "online": 61440
 },
 {
  "canid": "0x18f00021",
  "online": 61440
 },
 {
  "canid": "0x18f0000f",
  "online": 61440
 },
 {
  "canid": "0x18f0010b",
  "online": 61441
 },
 {
  "canid": "0x18f00121",
  "online": 61441
 },
 {
  "canid": "0xcf00203",
  "online": 61442
 },
 {
  "canid": "0xcf00300",
  "online": 61443
 },
 {
  "canid": "0xcf00327",
  "online": 61443
 },
 {
  "canid": "0xcf00400",
  "online": 61444
 },
 {
  "canid": "0x18f00503",
  "online": 61445
 },
 {
  "canid": "0x18f00621",
  "online": 61446
 },
 {
  "canid": "0x18f02300",
  "online": 61475
 },
 {
  "canid": "0x18fc4a00",
  "online": 64586
 },
 {
  "canid": "0x18fcbd00",
  "online": 64701
 },
 {
  "canid": "0x18fcdc00",
  "online": 64732
 },
 {
  "canid": "0x18fd0517",
  "online": 64773
 },
 {
  "canid": "0x18fd0621",
  "online": 64774
 },
 {
  "canid": "0x18fd0700",
  "online": 64775
 },
 {
  "canid": "0x18fd0721",
  "online": 64775
 },
 {
  "canid": "0x18fd0900",
  "online": 64777
 },
 {
  "canid": "0x18fd1721",
  "online": 64791
 },
 {
  "canid": "0x18fd2000",
  "online": 64800
 },
 {
  "canid": "0x14fd3e00",
  "online": 64830
 },
 {
  "canid": "0x18fd7c00",
  "online": 64892
 },
 {
  "canid": "0x18fd8321",
  "online": 64899
 },
 {
  "canid": "0x18fd9200",
  "online": 64914
 },
 {
  "canid": "0x18fda472",
  "online": 64932
 },
 {
  "canid": "0x18fda521",
  "online": 64933
 },
 {
  "canid": "0x18fdb200",
  "online": 64946
 },
 {
  "canid": "0x18fdc427",
  "online": 64964
 },
 {
  "canid": "0x18fdc421",
  "online": 64964
 },
 {
  "canid": "0x18fdc40b",
  "online": 64964
 },
 {
  "canid": "0x18fdc700",
  "online": 64967
 },
 {
  "canid": "0xcfdcc27",
  "online": 64972
 },
 {
  "canid": "0xcfdcc21",
  "online": 64972
 },
 {
  "canid": "0x18fdcd21",
  "online": 64973
 },
 {
  "canid": "0xcfe4127",
  "online": 65089
 },
 {
  "canid": "0xcfe4121",
  "online": 65089
 },
 {
  "canid": "0x18fe4a21",
  "online": 65098
 },
 {
  "canid": "0x18fe4e21",
  "online": 65102
 },
 {
  "canid": "0x18fe50f3",
  "online": 65104
 },
 {
  "canid": "0x18fe5121",
  "online": 65105
 },
 {
  "canid": "0x18fe5117",
  "online": 65105
 },
 {
  "canid": "0x18fe52f3",
  "online": 65106
 },
 {
  "canid": "0x18fe5600",
  "online": 65110
 },
 {
  "canid": "0x18fe5d00",
  "online": 65117
 },
 {
  "canid": "0x18fe6621",
  "online": 65126
 },
 {
  "canid": "0xcfe6cee",
  "online": 65132
 },
 {
  "canid": "0x18fe6f27",
  "online": 65135
 },
 {
  "canid": "0x1cfeac21",
  "online": 65196
 },
 {
  "canid": "0x18feae21",
  "online": 65198
 },
 {
  "canid": "0x18fec017",
  "online": 65216
 },
 {
  "canid": "0x18fec1ee",
  "online": 65217
 },
 {
  "canid": "0x1cfec321",
  "online": 65219
 },
 {
  "canid": "0x18feca21",
  "online": 65226
 },
 {
  "canid": "0x18feca27",
  "online": 65226
 },
 {
  "canid": "0x18feca00",
  "online": 65226
 },
 {
  "canid": "0x18feca19",
  "online": 65226
 },
 {
  "canid": "0x18feca71",
  "online": 65226
 },
 {
  "canid": "0x18fed521",
  "online": 65237
 },
 {
  "canid": "0x18fedf00",
  "online": 65247
 },
 {
  "canid": "0x18fee400",
  "online": 65252
 },
 {
  "canid": "0x18fee500",
  "online": 65253
 },
 {
  "canid": "0x18fee6ee",
  "online": 65254
 },
 {
  "canid": "0x18fee900",
  "online": 65257
 },
 {
  "canid": "0x18feed00",
  "online": 65261
 },
 {
  "canid": "0x18feee00",
  "online": 65262
 },
 {
  "canid": "0x18feef21",
  "online": 65263
 },
 {
  "canid": "0x18feef00",
  "online": 65263
 },
 {
  "canid": "0x18fef027",
  "online": 65264
 },
 {
  "canid": "0x18fef100",
  "online": 65265
 },
 {
  "canid": "0x18fef121",
  "online": 65265
 },
 {
  "canid": "0x18fef127",
  "online": 65265
 },
 {
  "canid": "0x18fef200",
  "online": 65266
 },
 {
  "canid": "0x18fef527",
  "online": 65269
 },
 {
  "canid": "0x18fef500",
  "online": 65269
 },
 {
  "canid": "0x18fef521",
  "online": 65269
 },
 {
  "canid": "0x18fef600",
  "online": 65270
 },
 {
  "canid": "0x18fef700",
  "online": 65271
 },
 {
  "canid": "0x18fef7f3",
  "online": 65271
 },
 {
  "canid": "0x18fef721",
  "online": 65271
 },
 {
  "canid": "0x18fef803",
  "online": 65272
 },
 {
  "canid": "0x18fefb10",
  "online": 65275
 },
 {
  "canid": "0x18fefc21",
  "online": 65276
 },
 {
  "canid": "0x18fefd21",
  "online": 65277
 },
 {
  "canid": "0xcff0027",
  "online": 65280
 },
 {
  "canid": "0x18ff0021",
  "online": 65280
 },
 {
  "canid": "0x18ff2100",
  "online": 65313
 },
 {
  "canid": "0x18ff2521",
  "online": 65317
 },
 {
  "canid": "0x18ff2517",
  "online": 65317
 },
 {
  "canid": "0x18ff3f21",
  "online": 65343
 },
 {
  "canid": "0x18ff6121",
  "online": 65377
 },
 {
  "canid": "0x18ff6221",
  "online": 65378
 },
 {
  "canid": "0x1cff6527",
  "online": 65381
 },
 {
  "canid": "0x1dff7800",
  "online": 130936
 },
 {
  "canid": "0x1dff7900",
  "online": "#REF!"
 },
 {
  "canid": "0x1dff7a00",
  "online": 130937
 },
 {
  "canid": "0x1dff7b00",
  "online": 130939
 },
 {
  "canid": "0x1dff7c00",
  "online": 130940
 },
 {
  "canid": "0x1dff7d00",
  "online": 130941
 },
 {
  "canid": "0x18ff8421",
  "online": 65412
 },
 {
  "canid": "0x18ffc272",
  "online": 65474
 },
 {
  "canid": "0xcffd221",
  "online": 65490
 },
 {
  "canid": "0x18ffd321",
  "online": 65491
 },
 {
  "canid": "0x18ffd421",
  "online": 65492
 },
 {
  "canid": "0x18ffda21",
  "online": 65498
 },
 {
  "canid": "0x18ffda19",
  "online": 65498
 },
 {
  "canid": "0x18ffdf27",
  "online": 65503
 }
]

# ex: get_only_data(61444, "ff ff ff 68 13 ff ff ff")
def get_only_data(canID_hex, pgn, strCanData, systemTickTimestamp):
    # Getting from  j1939 protocol data values to calculate
    file_protocol_values_to_calculate = open('json_files/canbus_parameters_info_new_13_11_22.json', encoding='utf8')
    json_protocol_values_to_calculate = json.load(file_protocol_values_to_calculate)
    payload_array = (json_protocol_values_to_calculate['payload'])

    # big_endian = json_protocol_values_to_calculate['endian type'] == "big endian"
    big_endian = True


    ls_result_for_pgn =[]
    for json_element in payload_array:
        data_found = {}

        pgn_element = json_element["PGN"]

        value = ERROR_PHYSICAL
        index_bit_start = ERROR_PHYSICAL
        if(pgn == pgn_element):
            spn = json_element["SPN"]




            str_scale = json_element["Resolution"].strip().split()[0]

            if(not "/" in str_scale):

                Resolution = float(str_scale)
            else:
                numerator = int(str_scale.strip().split("/")[0],10)
                denominator = int(str_scale.strip().split("/")[1],10)
                Resolution = float(numerator/denominator)

            offset = float(json_element["Offset"].strip().split()[0] )

            byte_start_str = (json_element["SP Position in PG"])

            #todo test:
            if("." in byte_start_str):
                index_byte_start = int(byte_start_str.strip().split(".")[0], 10) - 1
                index_bit_start = int(byte_start_str.strip().split(".")[1], 10) - 1

            else:
                if(not "-" in byte_start_str):
                    index_byte_start = int(byte_start_str.strip(), 10) - 1
                else:
                    index_byte_start = int(byte_start_str.split("-")[0], 10) - 1
                    index_byte_end = int(byte_start_str.split("-")[1], 10) - 1

            length = json_element["SP Length"]


            length_type = length.strip().split()[1]
            length_num = int(length.strip().split()[0], 10)

            is_invalid_byte = False
            if(length_type in ("bytes")):

                if(length_num == 1):
                    value, calculation_formula, mask, is_invalid_byte = get_physical_data_1_byte(str_hex=strCanData,
                                                                                                 index_byte=index_byte_start,
                                                                                                 bit_index_start=0,
                                                                                                 len_bit=8,
                                                                                                 offset=offset,
                                                                                                 scale=Resolution)
                    if(DEBUG_MODE):
                        print(f"str_hex={strCanData}, index_byte={index_byte_start}, bit_index_start = 0, len_bit= 8, offset= {offset}, scale= {Resolution}")

                        print(f"{value}, {calculation_formula}")
                if(length_num >= 2):
                    if (DEBUG_MODE):
                        print(f"pgn: {pgn}, spn: {spn}, {strCanData}, {index_byte_start}, {index_byte_end}, offset = {offset}, scale = {Resolution}")
                    value, calculation_formula, mask , is_invalid_byte= get_physical_data_more_than_one_byte(strCanData, index_byte_start, index_byte_end, offset = offset, scale = Resolution)



            else:
                if(length_type in ("bits")):
                    value, calculation_formula , mask , is_invalid_byte = get_physical_data_1_byte(str_hex=strCanData,index_byte= index_byte_start, bit_index_start=index_bit_start, len_bit=length_num, offset=offset,
                                                     scale=Resolution)

                else:
                    if(DEBUG_MODE):
                        print(f"illegal type: {length_type}!")
            data_range = json_element["Data Range"]
            is_valid = is_value_legal_by_legal_spn_values(pgn=pgn, spn=spn,
                                                          str_spn_legal_range_or_options=data_range, value=value)
            # todo return assert later:
            # assert (is_valid)

            if (DEBUG_MODE):
                print(f"(pgn={pgn},spn={spn},str_spn_legal_range_or_options={data_range},value={value}) ")
                print(f"raw_data: {strCanData} canId hex: {canID_hex}")
                print("----------------------")


            data_found["CanID_hex"] = canID_hex
            data_found["raw_data"] = strCanData
            data_found["PGN"] = pgn
            data_found["SPN"] = spn
            data_found["SP Label"] = json_element["SP Label"]
            data_found["Otofusion Param ID"] = json_element["Otofusion Param ID"]
            data_found["value"] = value

            data_found["Units"] = json_element["Units"].strip()
            data_found["SP Position in PG"] = byte_start_str
            data_found["SP Length"] = length
            # data_found["mask_to_extract_data_from_byte"] = mask
            data_found["calculation_formula"] = calculation_formula
            data_found["systemTickTimestamp"] = systemTickTimestamp
            # data_found["value_validity"] = "True" if is_valid else "False"
            data_found["value_and_legal_spn_values"] = f"value: {value}, data_range: "+data_range

            if (is_valid):
                ls_result_for_pgn.append(data_found)
            else :
                if (DEBUG_MODE):
                    print("Invalid byte!!")




    return ls_result_for_pgn


def get_str_CanData(strCanData):
    ls_strCanData = strCanData.strip().split()
    size_of_data = ls_strCanData[0]

    res = ""
    for duo in strCanData.strip().split()[1:]:
        res = res + " " + duo
    strCanData_on_size_of_on_left = res.strip()
    return size_of_data, strCanData_on_size_of_on_left


def parse_data_from_messages(sort_by_date):

    data = json.load(file_json_file)

    list_to_send = []
    for json_element in data:

        if(sort_by_date != ""):
            msg_date = (json_element["dateHourSecondsTimeReceived"].strip())

            if(not sort_by_date in msg_date):

                continue

        timestamp = (json_element["systemTickTimestamp"].strip())
        canId_str = (json_element['canId'].strip())
        strCanData = (json_element['strCanData'].strip())


        if(canId_str == "canId"):
            # not a number
            continue





        canId_number = int(canId_str,16)
        canID_hex = hex(canId_number)
        pgn, da, sa = parse_j1939_id(canId_number)

        # filter by pgn
        # if (pgn!= 65272):
        #     continue

        # filter by canId_str
        # if(canId_str != "0x18e00027"):
        #     # not a number
        #     continue
        if(DEBUG_MODE):
            print(f"canID_hex: {canID_hex}, pgn:{pgn}")
        size_of_data, strCanData_on_size_of_on_left = get_str_CanData(strCanData)

        ls_data_from_message = get_only_data(canID_hex, pgn=pgn, strCanData=strCanData_on_size_of_on_left,
                                             systemTickTimestamp=timestamp)



        if (len(ls_data_from_message) > 0):

            list_to_send = list_to_send + ls_data_from_message

    return list_to_send

def parse_pgn_numbers(sort_by_date, pgn_list):

    data = json.load(file_json_file)





    list_to_compare = []
    for json_element in data:
        if(sort_by_date != ""):
            msg_date = (json_element["dateHourSecondsTimeReceived"].strip())
            if(not sort_by_date in msg_date):
                continue



        canId_str = (json_element['canId'].strip())

        if(canId_str == "canId"):
            # not a number
            continue

        canId_number = int(canId_str,16)
        canID_hex = hex(canId_number)
        pgn, da, sa = parse_j1939_id(canId_number)

        tuple_canid_pgn = (canID_hex,pgn)

        list_to_compare.append(tuple_canid_pgn)



    set_canid_pgn = set(list_to_compare)
    list_unique_canid_pgn = list(set_canid_pgn)
    list_unique_canid_pgn.sort(key= lambda a: a[1])

    list_json = []
    for tup in list_unique_canid_pgn:
        json_canid_pgn = {}
        json_canid_pgn["canid"] = tup[0]
        json_canid_pgn["pgn_number"] = tup[1]
        list_json.append(json_canid_pgn)

    return list_json

def parse_pgn_numbers_compare_online(sort_by_date, pgn_list,):
    data = json.load(file_json_file)

    list_to_compare = []
    for json_element in data:
        if(sort_by_date != ""):
            msg_date = (json_element["dateHourSecondsTimeReceived"].strip())
            if(not sort_by_date in msg_date):
                continue



        canId_str = (json_element['canId'].strip())

        if(canId_str == "canId"):
            # not a number
            continue

        canId_number = int(canId_str,16)
        canID_hex = hex(canId_number)
        pgn, da, sa = parse_j1939_id(canId_number)

        tuple_canid_pgn = (canID_hex,pgn)

        list_to_compare.append(tuple_canid_pgn)



    set_canid_pgn = set(list_to_compare)
    list_unique_canid_pgn = list(set_canid_pgn)
    list_unique_canid_pgn.sort(key= lambda a: a[1])

    list_json = []
    for tup in list_unique_canid_pgn:
        json_canid_pgn = {}
        json_canid_pgn["canid"] = tup[0]
        json_canid_pgn["pgn_number"] = tup[1]
        list_json.append(json_canid_pgn)

    return list_json

def parse_canid_pgn_numbers(sort_by_date):

    data = json.load(file_json_file)

    ls_can_id_pgn_dic = []
    for json_element in data:
        dict_canid_pgn_element = {}
        if(sort_by_date != ""):
            msg_date = (json_element["dateHourSecondsTimeReceived"].strip())

            if(not sort_by_date in msg_date):

                continue

        canId_str = (json_element['canId'].strip())
        strCanData = (json_element['strCanData'].strip())


        if(canId_str == "canId"):
            # not a number
            continue

        canId_number = int(canId_str,16)
        canID_hex = hex(canId_number)
        pgn, da, sa = parse_j1939_id(canId_number)

        # filter by pgn
        # if (pgn!= 65272):
        #     continue

        # filter by canId_str
        # if(canId_str != "0x18e00027"):
        #     # not a number
        #     continue
        if(DEBUG_MODE):
            print(f"canID_hex: {canID_hex}, pgn:{pgn}")
        dict_canid_pgn_element["canid"] = canId_str
        dict_canid_pgn_element["pgn_local"] = pgn
        ls_can_id_pgn_dic.append(dict_canid_pgn_element)


    difference_list = []
    difference_list_tuple = []
    for local_canid_pgn_element in ls_can_id_pgn_dic:
        local_canid = local_canid_pgn_element["canid"]
        for online_canid_pgn_element in online_canid_pgn:
            online_canid = online_canid_pgn_element["canid"]
            if(local_canid == online_canid ):
                online_pgn = online_canid_pgn_element["online"]
                local_pgn = local_canid_pgn_element["pgn_local"]
                if(online_pgn != local_pgn):
                    # difference_list.append({"local_canid":local_canid, "online_canid":online_canid,"online_pgn" : online_pgn, "local_pgn":local_pgn})
                    difference_list_tuple.append((local_canid,online_canid, online_pgn,local_pgn) )
    # print(f"set_online_pgn: {set_online_pgn}")

    ret_list = list((set(difference_list_tuple)))
    ret_list.sort()
    return ret_list

def parse_j1939_id(can_id):
    sa = SA_MASK & can_id
    pf = (PF_MASK & can_id) >> 16
    da = (DA_MASK & can_id) >> 8

    if pf >= 240:  # PDU2 format
        pgn = pf * 256 + da
        da = 0xFF
    else:

        pgn = pf * 256



    return pgn, da, sa

def get_binary_array_skip_2(hex_string, len, bit_start, bit_end):
    current_bit = len - 1
    res = "0b"
    #go through msb to lsb
    for i in bin(hex_string)[2:]:
        if(current_bit >= bit_start and current_bit <= bit_end):
            res = res + str(i)
        current_bit = current_bit -1

    return res

def get_binary_array(hex_string, length, bit_start, bit_end):
    current_bit = length - 1
    res = "0b"
    #go through msb to lsb
    int_hex = int(hex_string,16)
    if(DEBUG_MODE):
        print(len((str(bin(int_hex)))))
    for i in bin(int_hex):
        if(current_bit >= bit_start and current_bit <= bit_end):
            res = res + str(i)
        current_bit = current_bit -1

    return res

def get_PGN_from_CanID_Hex(canId_hex):
    # canId_hex = 0x0CF00401
    len_of_canID = 29
    binary_res =  (get_binary_array(canId_hex, len_of_canID -1, 8, 25))
    number_decimal_from_binary = int(binary_res, 2)
    number_hex_from_binary = hex(number_decimal_from_binary)


    if(DEBUG_MODE):
        print(binary_res)
        print(number_decimal_from_binary)
        print(number_hex_from_binary)

    return number_decimal_from_binary

def get_ls_bytes(str_hex):
    if (not BIG_ENDIAN):
        str_hex_list = str_hex.strip().split()[::-1]  # first byte is on the left side .
    else:
        str_hex_list = str_hex.strip().split()



    return str_hex_list

# Get physical data from canData
def get_number_from_hex_str_1_byte(number_hex_byte_str, len_bit, bit_index_start):

    number = int(number_hex_byte_str, 16)

    mask_by_len_str = "0b"
    # print(f"len_bit: {len_bit}")
    if(len_bit == 0):
        mask_by_len_str = mask_by_len_str + "0"
    else:
        for i in range(len_bit):
            mask_by_len_str = mask_by_len_str + "1"


    mask_len_bin = int(mask_by_len_str,2)
    mask_len_bin = mask_len_bin << bit_index_start
    # print(f"mask_len_bin: {bin(mask_len_bin)}")

    value = (number & mask_len_bin) >> bit_index_start
    return value, bin(mask_len_bin)

def get_physical_data_1_byte(str_hex, index_byte, bit_index_start, len_bit, offset, scale):


    str_hex_list = get_ls_bytes(str_hex)

    #getting the hex string number:
    if(len(str_hex_list) - 1 < index_byte):
        return ERROR_PHYSICAL



    number_hex_byte_str = str_hex_list[index_byte]
    if(DEBUG_MODE):
        print(f"str_hex_list: {str_hex_list}, index_byte: {index_byte}")
        print(f"--byte {number_hex_byte_str}")

    is_invalid_byte = "ff" == number_hex_byte_str
    if is_invalid_byte:
        if(DEBUG_MODE):
            print("invalid byte: ff")

    # number_hex = int(number_hex_str, 16)

    number_hex, bin_mask_len_bin= get_number_from_hex_str_1_byte(number_hex_byte_str, len_bit, bit_index_start)

    physical_val = number_hex * scale + offset
    calculation_formula = (f"{physical_val} = {number_hex} * {scale} + {offset}")

    return physical_val,  calculation_formula, bin_mask_len_bin, is_invalid_byte

def get_physical_data_2_byte(str_hex, index_lsb_byte, index_msb_byte,offset, scale):
    # str_hex = "FF FF FF 68 13 FF FF FF" # todo remove later

    str_hex_list = get_ls_bytes(str_hex)

    #getting the hex string number:
    if(len(str_hex_list) - 1 < max(index_lsb_byte,index_msb_byte)):
        # print(str_hex)
        return ERROR_PHYSICAL

    # print(f"str_hex: {str_hex}")
    number_hex_str =  str_hex_list[index_msb_byte] +str_hex_list[index_lsb_byte]
    # print(f"number_hex_str: {number_hex_str} = str_hex_list[{index_lsb_byte}]:{str_hex_list[index_lsb_byte]} + str_hex_list[{index_msb_byte}]:{str_hex_list[index_msb_byte]}")
    # print(f"number_hex_str ")
    number_hex = int(number_hex_str, 16)
    # print(f"number_hex: {number_hex}")
    # print(number_hex)

    physical_val = number_hex * scale + offset
    calculation_formula = (f"{physical_val} = {number_hex} * {scale} + {offset}")
    mask = "0b1111111111111111"
    return physical_val, calculation_formula, mask

def get_physical_data_more_than_one_byte(str_hex, index_byte_start, index_byte_end, offset, scale):
    # str_hex = "FF FF FF 68 13 FF FF FF" # todo remove later
    str_hex_list = get_ls_bytes(str_hex)

    is_invalid_byte = False #todo later

    if (len(str_hex_list) - 1 < max(index_byte_start, index_byte_end)):
        # print(str_hex)
        return ERROR_PHYSICAL

    # print(f"str_hex: {str_hex}")
    number_hex_str = ""

    for i in range(index_byte_start, index_byte_end + 1):
        number_hex_str = str_hex_list[i] +number_hex_str
    if(DEBUG_MODE):
        print(f"--byte {number_hex_str}")
        # print(f"number_hex_str : {number_hex_str}")
        # number_hex_str = str_hex_list[index_lsb_byte] + str_hex_list[index_msb_byte]
        # print(f"number_hex_str: {number_hex_str} = str_hex_list[{index_lsb_byte}]:{str_hex_list[index_lsb_byte]} + str_hex_list[{index_msb_byte}]:{str_hex_list[index_msb_byte]}")
        # print(f"number_hex_str ")

        # print(f"number_hex: {number_hex}")
        # print(number_hex)
    number_hex = int(number_hex_str, 16)
    physical_val = number_hex * scale + offset
    calculation_formula = (f"{physical_val} = {number_hex} * {scale} + {offset}")
    mask = "0b" + "1" * 8 *(index_byte_end - index_byte_start)
    return physical_val, calculation_formula, mask, is_invalid_byte


# check spn values:
# if range is empty then by default it's ok. need to update what is the legal value in the relevant file.
def is_value_legal_by_legal_spn_values(pgn, spn, str_spn_legal_range_or_options, value):
    if(str_spn_legal_range_or_options == ""):
        if(DEBUG_MODE):
            print(f"pgn: {pgn}, spn: {spn}, str_spn_legal_range_or_options:{str_spn_legal_range_or_options}, value:{value} --Range Empty!!")
        return True

    if("options" in str_spn_legal_range_or_options):
        rs = str_spn_legal_range_or_options.strip().split("options:")[1].strip().split(",")
        found_option = False

        for r in rs:
            if (found_option):
                break
            r = r.strip()
            if "-" in r:
                sub_range = (r.split("-"))
                if (2 != len(sub_range)):
                    if(DEBUG_MODE):
                        print("Error!")
                    break

                if ("b" in r):
                    rr = int(sub_range[1].strip(), 2)
                    rl = int(sub_range[0].strip(), 2)

                else:
                    rr = int(sub_range[1].strip(), 10)
                    rl = int(sub_range[0].strip(), 10)

                found_option = value in range(rl, rr + 1)
                # print(f"{found_option} = {value} in {[i for i in range(rl, rr + 1)]}") #todo remove
            else:
                if ("b" in r):
                    option = int(r, 2)
                    found_option = value == option
                else:
                    option = int(r, 10)
                    found_option = value == option
            # print(option)

        return found_option


    if (",") in str_spn_legal_range_or_options:
        for i in str_spn_legal_range_or_options.strip().split(","):
            sub_ls_arg = i.split("to")
            # print(i.split("to"))
            # assert ("to" in sub_ls_arg[1])

            l = int(sub_ls_arg[0].strip(),10)
            r = int(sub_ls_arg[1].strip(),10)
            res = l <= float(value) and float(value) <= r
            if res:
                return True
        return False
    else:
        if("to" in str_spn_legal_range_or_options):
            ls_range = str_spn_legal_range_or_options.split()
            # print(f"ls_range: {ls_range}")

            if (not "to" in (ls_range[1])):
                if(DEBUG_MODE):
                    print("is_value_legal_by_legal_spn_values ERROR !!!! ")
                return False

            first_num  = float(ls_range[0].strip())
            second_num = float(ls_range[2].strip())

            res = first_num <= float(value) and float(value) <= second_num

            # print(f"{res} = {first_num} <= {float(value)} and {float(value)} <= {second_num}")

            return res
    if(DEBUG_MODE):
        print("is_value_legal_by_legal_spn_values could not read the range values!! ")
    return True


def test_with_assert():
        ret = is_value_legal_by_legal_spn_values(pgn=65272, spn=177, str_spn_legal_range_or_options="-273 to 1735 °C",
                                                 value=1774.969)
        assert (ret == False)

        ret = is_value_legal_by_legal_spn_values(pgn=65272, spn=177, str_spn_legal_range_or_options="-273 to 1735 °C",
                                                 value=-271.844)
        assert (ret == True)

        ret = is_value_legal_by_legal_spn_values(pgn=65272, spn=177, str_spn_legal_range_or_options="0 to 250.996 km/h",
                                                 value=0)
        assert (ret == True)


        ret = is_value_legal_by_legal_spn_values(pgn=65272, spn=177, str_spn_legal_range_or_options=" 0 to 2105540607.5 L",
                                                         value=0)
        assert (ret == True)

        ret = is_value_legal_by_legal_spn_values(pgn=65272, spn=177,
                                                 str_spn_legal_range_or_options="-31.374 to +31.374 rad",
                                                 value=0)
        assert (ret == True)

        #Options:
        ret = is_value_legal_by_legal_spn_values(pgn=65272, spn=177,
                                                 str_spn_legal_range_or_options="options: 0b0000, 0b0001 -  0b1110",
                                                 value=0)
        assert (ret == True)

        ret = is_value_legal_by_legal_spn_values(pgn=65272, spn=177,
                                                 str_spn_legal_range_or_options="options: 0b00, 0b01",
                                                 value=0)
        assert (ret == True)

        str="224 to 253  ,65 to 223 , 0 to 61  "
        ret = is_value_legal_by_legal_spn_values(pgn=65272, spn=177,
                                                 str_spn_legal_range_or_options=str,
                                                 value=61)
        assert (ret == True)

def test_byte_reader(pgn, candata):
    candata = "50 7d 7d 00 ff ff 7d"
    pgn = 61440
    spn = 1082
    byte_index = 0
    bit_index = 1-1
    length_bit = 2



    # physical_val, calculation_formula, bin_mask_len_bin = get_physical_data_more_than_one_byte(candata, 3,4, 0, 0.125)
    value, calculation_formula, mask, is_invalid_byte = get_physical_data_more_than_one_byte("ff ff ff 68 13 ff ff ff", 3, 4, offset = 0, scale = 0.125)

    print(value)
    print(calculation_formula)
    # print(physical_val)
    # print(calculation_formula)

    # ls_result_for_pgn = get_only_data(canID_hex="",strCanData=candata, pgn=pgn,systemTickTimestamp="")



def main():
    sort_by_date = ""

    # output valid items
    # result_ls = parse_data_from_messages(sort_by_date=sort_by_date)
    # print(f"result_ls: {result_ls}")


    # out_put = open('json_files/output_final_with_descriptions_13_11_only_valid.json','w')
    # out_put.write(str(result_ls))
    # out_put.close()


    #output_pgns
    # result_ls = parse_pgn_numbers(sort_by_date=sort_by_date)
    # set_result = set(result_ls)
    # ls_unique = list(set_result)
    # ls_unique.sort()
    # print(f"result_ls: {ls_unique}")
    #
    # out_put_only_pgn = open('json_files/output_only_pgn_numbers_from_table.json','w')
    # out_put_only_pgn.write(str(ls_unique))
    # out_put_only_pgn.close()

    # out_put_only_pgn = open('json_files/output_only_pgn_numbers_from_table.json','w')
    # out_put_only_pgn.write(str(ls_unique))
    # out_put_only_pgn.close()

    # ls_canid_pgn = parse_pgn_numbers("13_11",pgn_list)
    # out_put_only_pgn = open('json_files/canid_pgn_unique_by_canid_to_be_checked8.json','w')
    # out_put_only_pgn.write(str(ls_canid_pgn))
    # out_put_only_pgn.close()

    result_ls = parse_canid_pgn_numbers(sort_by_date=sort_by_date)
    # print(f"result_ls: {result_ls}")
    for tup in result_ls:
        print(tup)
    file_json_file.close()



def check_canid_to_pgn():
    # canid = "0x1dff7800" #ok
    # canid = "0x1dff7900" # //
    # canid = "0x1dff7a00" # //
    # canid = "0x1dff7b00" # ok
    # canid = "0x1dff7c00" # ok
    # canid = "0x1dff7d00" # ok
    # canid = "0x18ffc272"
    canid = "0xcffd221" # ok
    pgn, da, sa = parse_j1939_id(int(canid,16))

    print(pgn)

    print(bin(int(canid,16)))
    print(bin(65490))
    print(bin(65474))


main()

# print(set({1, 2}).difference(set({2, 3}) ))


# compare_pgns()

# check_canid_to_pgn()



# Tests:
# test_with_assert()

# test_byte_reader(61440, "")

##
# print(bin(2))

# print(int("0b1110",2))

# main()
# value, calculation_formula, mask = get_physical_data_more_than_one_byte("ff ff ff 68 13 ff ff ff", 3, 4, offset = 0, scale = 0.125)
# print(value)
# print(calculation_formula)
# ex: get_only_data(61444, "ff ff ff 68 13 ff ff ff")