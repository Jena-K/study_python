def solution(new_id):
    #step1
    new_id = new_id.lower()
    
    #step2
    temp = ''
    for i in new_id :
        if i.isalpha() or i.isdigit() or i in '-_.':
            temp+=i
    new_id = temp
    
    #step3
    temp, old = new_id[0], new_id[0]
    for i in new_id[1:]:
        if i != '.' or i != old:
            temp+=i
            old = i
    new_id = temp

    #step4
    if new_id == new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    #step5
    if not new_id:
        new_id = 'a'

    #step6
    new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    #step7
    while len(new_id) < 3:
        new_id+=new_id[-1]

    return new_id


str1 = ["...!@BaT#*..y.abcdefghijklm", "bat.y.abcdefghi"]
str2 = ["z-+.^.", "z--"]
str3 = ["=.=", "aaa"]
str4 = ["123_.def", "123_.def"]
str5 = ["abcdefghijklmn.p",	"abcdefghijklmn"]


print(solution(str1[0]))
if solution(str6[0]) == str6[1] :
    print('TRUE')
else :
    print('False')