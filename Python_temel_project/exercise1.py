# SORU -1 Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.

flatt = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
new_list = []
def flatten(n):
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            new_list.append(i)

flatten(flatt)
print(new_list)