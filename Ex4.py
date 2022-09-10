#EX1
sum=0
d=0
def function1(tree,num):
  d=function1(tree.right,num)+function1(tree.left,num)
  if type(tree.data)==chr:
    num = chr(num)
  else:
    num = int(num)
  if tree.data==num:
    sum=sum+1
  if tree.left!=None and tree.right==None:
    return function1(tree.left,num)
  if tree.right!=None and tree.left!=None:
    return function1(tree.right,num)
  if tree.right!=None and tree.right!=None:
    sum=sum+d
  return sum
#Ex2
def function2(tree,num):
  for x in num:
    if function1(tree,x)>0:
      continue
    else:
      return false
  return true
