
a = set()  #Olonlog gsen ug
#Natural toonii olonlog = {1,2,3...}
#1 Olonlog dotor baigaa elementuud davhtsaj bolohgui 
#2 daraalal gej baihgui


s = "asjhjdsfdgfhgj" # heden shirheg uur useg baina we
usegnuud = set(s)
print(len(usegnuud))


# 1) Element baigaa uguig shalgah
[1,2,1,3432,43,2] # array uyd buh elementeer shalgana - O(N)
{1,2,1,3432,43,2} # O(1) - uyd ter element baigaa uguig l shalgana
# set add('s') - O(1) functioneer nemj bolno
# remove('s') - O(1) ustgana
# list - mutable nemj bolohgui

if 's' in set("sdjkdkjdskjsd"): # O(N)
    print("s useg baina")