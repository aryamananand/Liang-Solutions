import LinearEquation 


def main():
        
    #Find equation of the first line
    x1,y1,x2,y2 = eval(input("Enter x1, y1 and x2, y2: "))

    le = LinearEquation.LinearEquation()
    le.setA(x1)
    le.setB(1)
    le.setE(y1)
    le.setC(x2)
    le.setD(1)
    le.setF(y2)

    a = le.getX()
    b = le.getY()


    #Find equation of the second line
    x3,y3,x4,y4 = eval(input("Enter x3, y3 and x4, y4: "))

    le_ = LinearEquation.LinearEquation()
    le_.setA(x3)
    le_.setB(1)
    le_.setE(y3)
    le_.setC(x4)
    le_.setD(1)
    le_.setF(y4)

    a_ = le_.getX()
    b_ = le_.getY()

    #Find intersection point of these two lines
    le2 = LinearEquation.LinearEquation()
    le2.setA(a)
    le2.setB(-1)
    le2.setE(-b)
    le2.setC(a_)
    le2.setD(-1)
    le2.setF(-b_)

    a2 = le2.getX()
    b2 = le2.getY()

    print(a2,",",b2)

main()





