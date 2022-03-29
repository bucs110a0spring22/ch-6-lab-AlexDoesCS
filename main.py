import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
    
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
        count +=1
    return count
 
#Part B
def graph(upper):
  window = turtle.Screen()
  alex = turtle.Turtle()
  squirtle = turtle.Turtle()
  window.setworldcoordinates(0, 0, 10, 10)
  max_so_far=0
  for start in range(1, upper +1):
    result = seq3np1(start)
    if (max_so_far < result):
      max_so_far = result
      squirtle.clear()
      squirtle.up()
      squirtle.goto(0, result)
      squirtle.write("Maximum so far: " +str(result))
      window.setworldcoordinates(0, 0, start+10, result+10)
    alex.goto(start, result)
  window.exitonclick()


#Part A
def main():
  upper = int(input("What is the Upperbouund Value?"))
  if(upper < 0):
    exit()
  else:
    for start in range(1, upper +1):
      print(start, "Is the current loop value")
      iterations = seq3np1(start)
      print(iterations, "Is the number of Iterations")

  graph(upper)
  seq3np1(3)
main()

