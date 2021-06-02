# Checks the four problmes expected.
def check(problems):
  error = False
  len_problems = len(problems)

  if len_problems > 5:
    error = "Error: Too many problems."
  elif len_problems <= 5:
    for i in range(len_problems):
      problems_splited = problems[i].split()
      if problems_splited[1] != '+' and problems_splited[1] != '-':
        error = "Error: Operator must be '+' or '-'."
        break
      if len(problems_splited[0]) > 4  or len(problems_splited[2]) > 4:
        error = "Error: Numbers cannot be more than four digits."
        break
      else:
        try:
          int(problems_splited[0])
          int(problems_splited[2])
        except: 
          error = "Error: Numbers must only contain digits."
  return error

# Comparator checks the space between two numbers.
def comparator(number1,number2):
  if len(number1) > len(number2):
    spaces = len(number1)-len(number2)
    number = 2
  elif len(number2) == (number1):
    spaces = 0
    number = 1
  else:
    spaces = len(number2)-len(number1)
    number = 0
  return spaces, number

# Operation makes the operation selecte in p2 (+ -), it can be
# extended 
def operation(p1,p2,p3):
  p1 = int(p1)
  p3 = int(p3)
  if p2 == "+":
    ans = p1+p3
  elif p2 == "-":
    ans = p1-p3
  return  ans

def arithmetic_arranger(problems, show = "False"):

  error = check(problems)
  up = ""
  down = "" 
  bar = ""
  result = ""

  if error == False:
     for i in range(len(problems)):
      problems_splited = problems[i].split()
      [spaces, number] = comparator(problems_splited[0],problems_splited[2])

      #Add the spaces to normalize the size of numbers 1 and 2
      if number == 0 or number == 2:
        for x in range(spaces):
          problems_splited[number] = ' ' + problems_splited[number]

      # Add line of result
      for d in range(len(problems_splited[number])+2): 
        bar = bar + "-"

      #Normalize the output
      if i < (len(problems)-1):
        up = up + "  " +problems_splited[0] + "    "
        down= down + problems_splited[1] + " " +problems_splited[2] + "    "
        bar = bar + "    "  
      else:
        up = up + "  " +problems_splited[0] 
        down= down + problems_splited[1] + " " +problems_splited[2]
        bar = bar 


     #Shows ans and calculate the ans
     if show == True: 
      bar_splited = bar.split()

      for a in range(len(bar_splited)):
       problems_splited = problems[a].split()
       ans = str(operation(problems_splited[0],problems_splited[1],problems_splited[2]))
       [spaces, number] = comparator(ans,bar_splited[a])

       # Normalize the ans
       for e in range(spaces):
         ans = " " + ans
       if a < (len(bar_splited)-1):
         result = result + ans + "    " 
       else:
         result = result + ans 
      arranged_problems = up + "\n" + down + "\n" + bar + "\n" + result  
     else:
      arranged_problems = up + "\n" + down + "\n" + bar
  else:
    arranged_problems = error
  return arranged_problems

# Final comments 
## This program can be extended with some operations more, and a large number of operations, some instrucctions can be called as functions but how the program is simple I wanna have a "core".
