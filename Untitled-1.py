def sumas(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    elif isinstance(a,str) and isinstance(b,str):
        return " ".join((a,b))
    else: return 8


print(sumas(1, "midcoan"))
