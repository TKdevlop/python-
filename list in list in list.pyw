n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results=[]
  for numbers in lists:
      for i in numbers:
          print(i)
          results.append(i)
  #  print(numbers)



print (flatten(n))
