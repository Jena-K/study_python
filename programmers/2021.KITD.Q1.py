def solution(s):
    Number = {'zero': '0', 'one' : '1', 'two' : '2' ,'three' : '3', 'four' : '4', 'five' : '5',
     'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9' }

    for i in Number.keys():
        s = s.replace(i, Number[i])

    return int(s)

s = "one4seveneight"
print(solution(s))
s = "23four5six7"
print(solution(s))
s = "2three45sixseven"
print(solution(s))
s = "123"
print(solution(s))


