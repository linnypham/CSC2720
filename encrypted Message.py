def decryptMessage(self, s:str)->int:
    dict = {len(s): 1}
    def dec(i):
        if s[i] == "0":
            return 0
    if i in dict:
        return dict[i]
    n_ways = dec(i+1)

    if(i+1<len(s) and s[i+1]=='1' or s(s[i+1]=='2' and s[i+2] in '0123456')):
        n_ways += 1
    dict[i] = n_ways #memorization
    return n_ways
