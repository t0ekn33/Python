"""lab08b_func.py

This program reads a temperature from the keyboard.  It then reads a
character that determines what type of conversion to perform.  A 'c'
causes a fahrenheit-to-centigrade coversion while a 'f' causes the
opposite conversion.  Separate functions provide the conversion as
well as print statements showing the result of the conversion. Then
it requests another input from the keyboard until a 'q' is entered.
"""


def f_to_c(xtmp):
    ctmp = 5.0 / 9.0 * (xtmp - 32)
    print('{0} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(
        xtmp, ctmp))


def c_to_f(xtmp):
    ctmp = 9.0 / 5.0 * xtmp + 32
    print('{0} degrees Centigrade is {1:.1f} degrees Fahrenheit'.format(
        xtmp, ctmp))


while True:
    temp = input('Enter a temperature or Q: ')
    if temp == 'q' or temp == 'Q':
        break
    flt_temp = float(temp)
    convert = input('Enter a c or f: ')
    if convert == 'c':
        f_to_c(flt_temp)
    elif convert == 'f':
        c_to_f(flt_temp)
    else:
        print('Invalid conversion request')
