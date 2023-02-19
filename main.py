class Tree:  
  leafs = 569797859686
  age = 120 

  def __init__(self):
    print("3434")

  def get_older(self):
    self.age += 1


my_tree = Tree()

print(my_tree.age)

my_tree.get_older()
print(my_tree.age)
