import LinearEquation

def main():
    
    a,b,e,c,d,f= eval(input("Enter x1, y1, x2, y2"))

    le1 = LinearEquation.LinearEquation()
    le1.setA(a)
    le1.setB(b)
    le1.setC(c)
    le1.setD(d)
    le1.setE(e)
    le1.setF(f)
    if le1.isSolvable() == 1:
        print(f"Solution: x = {le1.getX()} and y = {le1.getY()}")
    else:
        print("This system of linear equations has no solution.")
main()
