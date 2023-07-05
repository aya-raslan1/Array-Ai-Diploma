import calc
c=0
while(c<3):
     a=float(input("first num= "))
     b=float(input("second num= "))
     sign=input("enter the operation => add,sub,mult,div: ")
     if sign=="add":
          ans=calc.add(a, b)
          print(ans)
     elif sign=="sub":
          ans=calc.sub(a,b)
          print(ans)
     elif sign=="mult":
          ans=calc.mult(a,b)
          print(ans)
     else:
          ans=calc.div(a, b)
          print(ans)
     with open("calculator.txt", "a", encoding='utf-8') as f:
        f.write(str(a)+sign+str(b)+" equal "+str(ans)+"\n")
     re=input("you want to make another operation yes or no?")
     if re=="yes":
        continue
     elif re=="no":
        break

