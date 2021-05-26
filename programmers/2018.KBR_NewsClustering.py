def solution(str1, str2):
    str1 = str1.lower()#필요없지 합칠수있으면 같이합쳐짐
    str2 = str2.lower()#필요없지 합칠수있으면 같이합쳐짐

    s1, s2 = [], [] # 미리선언 필요 x append 안할꺼니까
    nume, deno = 0, 0
    union = []
    for i in range(len(str1)-1): # for문 + if문 + 행위 합칠수있음 
        if str1[i:i+2].isalpha():
            s1.append(str1[i:i+2])

    for i in range(len(str2)-1): # for문 + if문 + 행위 합칠수있음 
        if str2[i:i+2].isalpha():
            s2.append(str2[i:i+2])

    union = set(s1+s2)
    for i in union:
        nume+=min(s1.count(i), s2.count(i)) #교집합만 검색하면 됨
        deno+=max(s1.count(i), s2.count(i)) #모두 개수를 세야함

    if deno == 0 :
        return 65536
    return int((nume/deno)*65536)

#--------------------------------------------------------------------------------------------#

def solution(str1, str2):
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    union = set(s1) | set(s2)
    ints = set(s1) & set(s2)
    
    deno=sum([max(s1.count(i), s2.count(i)) for i in union])
    nume=sum([min(s1.count(i), s2.count(i)) for i in ints])

    if not deno : 
        return 65536
    return int((nume/deno)*65536)













str1 = 'FRANCE'
str2 = 'french'
print(solution(str1, str2)) 
str1 = 'handshake'
str2 = 'shake hands'
#print(solution(str1, str2)) 
str1 = 'aa1+aa2'
str2 = 'AAAA12'
#print(solution(str1, str2)) 
str1 = 'E=M*C^2'
str2 = 'e=m*c^2'
#print(solution(str1, str2)) 