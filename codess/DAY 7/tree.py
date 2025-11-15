class Binarytree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

node1=Binarytree(50)
node2=Binarytree(20)
node3=Binarytree(45)
node4=Binarytree(11)
node5=Binarytree(15)
node6=Binarytree(30)
node7=Binarytree(78)

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.left=node6
node3.right=node7

