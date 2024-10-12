
import random

def display(a):
  print("..................")
  print(":",a[0]," : ",a[1]," : ",a[2]," : ")
  print("..................")
  print(":",a[3]," : ",a[4]," : ",a[5]," : ")
  print("..................")
  print(":",a[6]," : ",a[7]," : ",a[8]," : ")
  print("..................")



def vali(a,comp,your):
  if (a[0]==a[1]==a[2]==comp or a[4]==a[3]==a[5]==comp or a[6]==a[7]==a[8]==comp or a[0]==a[3]==a[6]==comp or a[1]==a[4]==a[7]==comp or a[0]==a[8]==a[4]==comp or a[6]==a[4]==a[2]==comp ):
    display(a)
    print("\n\n...................................")
    print("...........computer is win............")
    print(".......................................\n\n")
    return 1
  elif (a[0]==a[1]==a[2]==your or a[4]==a[3]==a[5]==your or a[6]==a[7]==a[8]==your or a[0]==a[3]==a[6]==your or a[1]==a[4]==a[7]==your or a[0]==a[8]==a[4]==your or a[6]==a[4]==a[2]==your ):
    display(a)
    print("\n\n...............................")
    print("...........CONGRATS  YOU WIN............")
    print("..................................\n\n")
    return 1
  else:
    return 0

print("\n\n.................................")
print("...........TIC TAC TOE............")
print("..................................\n\n")

x='1'
while(x=='1'):  
  SYM=3  
  while((SYM !=1 )and (SYM !=2)):
      SYM=int (input("enter 1 for X, 2 for O:::"))
      if (SYM!=1 and (SYM !=2)):
        print("Warning : wrong input......")
  your="X" if SYM ==1 else "O"
  comp="X" if SYM ==2 else "O"
  print("YOURS SYMBOL:: ",your)
  print("computer SYMBOL:: ",comp)

  print("\n \n")




  first=3  
  while(first!=1 and (first !=2)):
      first=int (input("enter 1 for computer, 2 for you:::"))
      if (first!=1 and (first !=2)):
        print("Warning : wrong input......")




  print("sample numbering.......")
  a=["1","2","3","4","5","6","7","8","9"]
  display(a)
  print("\n \n")

  print("Initial :")
  a=[" "," "," "," "," "," "," "," "," "]
  display(a)


  if first ==1:
      n=0
      visited=[]   
      element=random.randint(0,8)
      while(n<9):
      
          print("\n\n")
          print(".......................................")
          print("Computer 's turn")
          print(".......................................")
          if element not in visited:
              visited.append(element)
              a[element]=comp
            
              n=n+1
          else:
              while True:
                  element = random.randint(0, 8) 
                  if element not in visited:
                       break
              visited.append(element)
              a[element]=comp
            
              n=n+1
          display(a)
          if(vali(a,comp,your)):
             break
        
      
          if n!=9:
            
              print("\n\n")
              print(".......................................")
              print("yours 's turn")
              print(".......................................")
              element=int(input("Enter the position ::"))
              element=element-1
              if element not in visited:
                 visited.append(element)
                 a[element]=your
                 n=n+1

              else:
                while True:
                  print("\n poisition is already filled::::")
                  element=int(input("Enter the position ::"))
                  element=element-1
                  if element not in visited:
                        break
                visited.append(element)
                a[element]=your
                n=n+1
              display(a)
              if(vali(a,comp,your)):
                 break

          else:
            print("......................")
            print("........match draw........")
            print("......................")

  elif first ==2:
  
      n=0
      visited=[]   
      element=random.randint(0,8)
      while(n<9):
              print("\n\n")
              print(".......................................")
              print("yours 's turn")
              print(".......................................")
              element=int(input("Enter the position ::"))
              element=element-1
              if element not in visited:
                 visited.append(element)
                 a[element]=your
                 n=n+1
  
              else:
                while True:
                  print("\n poisition is already fimlled::::")
                  element=int(input("Enter the position ::"))
                  element=element-1
                  if element not in visited:
                       break
                visited.append(element)
                a[element]=your
              n=n+1
              display(a)  
              if(vali(a,comp,your)):
                 break

              if n!=9:
                 print("\n\n")
                 print(".......................................")
                 print("Computer 's turn")
                 print(".......................................")
                 if element not in visited:
                      visited.append(element)
                      a[element]=comp
              
               
                 else:
                      while True:
                        element = random.randint(0, 8) 
                        if element not in visited:
                           break
                      visited.append(element)
                      a[element]=comp
            
                 n=n+1
                 display(a)
                 if(vali(a,comp,your)):
                        break
        
              else:
                  print("......................")
                  print("........match draw........")
                  print("......................")

  print("good game.......")
  print("\n DO you Want To Play Again ?")
  x=input("\n Enter 1 to play")
  if (x!='1'):
    print("Thanks for Playing...........")
















          
            
            
