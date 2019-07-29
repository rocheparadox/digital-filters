#Author : Roche Christopher
#File created on 29 Jul 2019 9:34 PM

import xlrd
from low_pass_filter import SIMPLE_LPF

beta = 0.1

workbook = xlrd.open_workbook("accelerometer.xlsx")
sheets = workbook.sheets()

for sheet in sheets:
    initial_value = sheet.cell_value(1,0)
    lpf_0_1 = SIMPLE_LPF(0.1, initial_value)
    lpf_0_1_5 = SIMPLE_LPF(0.15, initial_value)
    lpf_0_2 = SIMPLE_LPF(0.2, initial_value)
    lpf_0_3 = SIMPLE_LPF(0.3, initial_value)
    lpf_0_5 = SIMPLE_LPF(0.5, initial_value)
    lpf_0_7 = SIMPLE_LPF(0.7, initial_value)
    lpf_0_8 = SIMPLE_LPF(0.8, initial_value)


    #print(initial_value)
    for row in range(2,sheet.nrows):
        input = sheet.cell_value(row, 0)
        lpf_0_1.update(input)
        lpf_0_1_5.update(input)
        lpf_0_2.update(input)
        lpf_0_3.update(input)
        lpf_0_5.update(input)
        lpf_0_7.update(input)
        lpf_0_8.update(input)

        print(input, lpf_0_1.get_output(), lpf_0_1_5.get_output(),lpf_0_2.get_output(),lpf_0_3.get_output(),lpf_0_5.get_output())

# lpf = SIMPLE_LPF(beta)
# output = lpf.update()
