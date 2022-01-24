# Big O of N --> O(N) - shugaman baidlaar usnu
# O(1) - const baidlaar 
# O(N^N) -  O(N!) - udaan ajillana 


# 10 -> 1 + 2 + 3 ... + 10 = 55 niilberiig oloh
# Hurdni - O(N) - Time complexity - shugaman baidlaar usnu
# Hemjee ni - O(1) - Space complexity - constance space - hemjee hewendee baidag uyd orj bga utga ni uyd iim bn - computeriin memory hicheeneen zai ezelj baigaag haruulah yum 
def tooNemeh(n):
    niiler = 0
    for i in range(1, n+1):
        niiler += i
    return niiler


# Hurd - O(2*N) => O(N) - N umnu ywar ch too baisan gesen O(N) gej bijdeg
# Hemjee - O(N)
def tooNemeh1(n):
    niilber = 0
    arr = list(range(1, n+1))

    for i in arr:
        niilber+=i

    return niilber

#Hurd - O(1)
#Hemjee - O(1) n eesee hamaarch usduggui bol O(1) baina
def tooNemeh2(n):
    return n * (n+1) // 2 



print(tooNemeh(10))

