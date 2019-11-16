def class_desks(a,b,c):
    total=a+b+c
    check=total%2
    desks=total//2
    if check==0:
        print(desks)
        return desks
    desks=desks+1
    print(desks)
    return desks
class_desks(20,21,22)