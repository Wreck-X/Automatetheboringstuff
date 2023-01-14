# import re,time
# def regexstrip(string, strp):
#     lcheck = re.compile(fr'^({strp})*')
#     rcheck = re.compile(fr'({strp})*$')
#     templout = lcheck.search(string)
#     temprout = rcheck.search(string)
#     lout = len(templout.group())
#     rout = len(temprout.group())
#     liststring = list(string)
#     for i in range(lout):
#         liststring.pop(0)
#     for j in range(rout):
#         liststring.pop()
#     string = ''.join(liststring)
#     print(string)

# string = 'aaaaaabananana apple aaaa'
# time_ = time.time()
# regexstrip(string,'a')
# time_2 = time.time()
# print(time_2 - time_)

import re,time

def regexstrip(string,strip):
    finalstring = re.compile(fr'^{strip}*(.*)[^{strip}]').search(string).group(1)
    return finalstring
time_ = time.time()
print(regexstrip('aaaaaabananana apple aaaa','a'))
time_2 = time.time()
print(time_2-time_)