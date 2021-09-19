import re


'''
. : 하나의 문자
^ : 문자열의 시작
$ : 문자열의 끝
'''

def print_match(m):
    if m:
        print('m.group(): ', m.group()) #일치하는 문자열
        print('m.string: ', m.string)   #입력받은 문자열
        print('m.start(): ', m.start()) #일치하는 문자열의 시작 index
        print('m.end(): ', m.end())     #일치하는 문자열의 끝 index
        print('m.span(): ', m.span())       #일치하는 문자열의 시작, 끝 index
    else :
        print('Not Matched')

#p = re.compile('ca.e')
#m = p.match('careless') #p.match(): 주어진 문자열로 시작하는지 
#m = p.search('careless') #p.search(): 주어진 문자열이 포함되어 있는지
#lst = p.findall('good care cafe') #일치하는 모든 것을 리스트 형태로 반환
print(lst)

