def reverse_in_groups(lst,k):
  first_part=lst[ :k][::-1]
  second_part=lst[k: ][ : :-1]
  return first_part+second_part
n=[1,2,3,4,5,6,7,8]
k=4
output=reverse_in_groups(n,k)
print(output)  

