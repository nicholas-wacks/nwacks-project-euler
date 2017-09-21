input = ["319","680","180","690","129","620","762","689","762","318","368","710","720","710","629","168","160","689","716","731","736","729","316","729","729","710","769","290","719","680","318","389","162","289","162","718","729","319","790","680","890","362","319","760","316","729","380","319","728","716"]

relationships = set()

for i in input:
    relationships.add((i[0], i[1]))
    relationships.add((i[0], i[2]))
    relationships.add((i[1], i[2]))

start = ''
end = ''

neededChars = set()
for r in relationships:
    neededChars.add(r[0])
    neededChars.add(r[1])

while (len(neededChars) > 0):
    starts = set()
    ends = set()

    for r in relationships:
        if (r[0] and r[0] in neededChars):
            starts.add(r[0])
            ends.add(r[1])

    for s in starts.difference(ends):
        if s not in start:
            start += s
            neededChars.remove(s)

    for e in ends.difference(starts):
        if e not in end:
            end = end + e
            neededChars.remove(e)

print(start + end)