phrase = "issam was a good in the good with mush goodness in his heart"
a = 0
booll = True
List_occ = []
List_char = []
l = 0

while booll:
    first_char = phrase[l]
    for x in phrase:
        if x == first_char:
            a+=1
    l+=1
    if first_char not in List_char and first_char != ' ' :
        List_occ.append(a)
        List_char.append(first_char)
    if l == len(phrase):
        booll = False
    a=0
print(List_char)
print(List_occ)
