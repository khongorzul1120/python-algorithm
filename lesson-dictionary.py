# Dictionary -> key bolon value tai baina
a = {'dog':'nohoi', 'right':"zuw gesn ug"} # ingej bijne
# Utga ni dawhtsaj bolohgui
# Daraalal gej baihgui


# element nemehed  O(1)
# ustagahad O(1)
#Bodlogo1 Yamar2 useg heden shirheg baina ve?
# key = useg hed bgag
# value = heden udaa orsoniig hadgalna

s = 'dafsghdjfkglh;j'
d = {}
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
print(d)

