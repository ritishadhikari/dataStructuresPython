class TreeNode:
    def __init__(self, data):
        self.data=data
        self.children=[]
        self.parent=None    

    def addChild(self, child):
        child.parent=self
        self.children.append(child)

    def printTree(self):
        level=self.getLevel()
        if self.parent: 
            print(level*"  "+"|__"+self.data)
        else:
            print(level*"  "+self.data)

        if self.children:
            for superChild in self.children:
                superChild.printTree()

    def getLevel(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def __repr__(self):
        return f"TreeNode({self.data})"

if __name__=="__main__" :
    root=TreeNode(data="Electronics")
    
    laptop=TreeNode(data="Laptop")
    laptop.addChild(child=TreeNode(data="Mac"))
    laptop.addChild(child=TreeNode(data="Surface"))
    laptop.addChild(child=TreeNode("Thinkpad"))

    cellPhone=TreeNode(data="Cell Phone")
    cellPhone.addChild(child=TreeNode(data="iPhone"))
    cellPhone.addChild(child=TreeNode(data="Google Pixel"))
    cellPhone.addChild(child=TreeNode(data="Vivo"))

    tv=TreeNode(data="TV")
    tv.addChild(child=TreeNode(data="Samsung"))
    tv.addChild(child=TreeNode(data="LG"))

    root.addChild(child=laptop)
    root.addChild(child=cellPhone)
    root.addChild(child=tv)

    root.printTree()