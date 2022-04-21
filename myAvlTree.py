import myLinkedList as mll

class AVLTree:
	root = None

class AVLNode:
	parent = None
	leftNode = None
	rightNode = None
	key = None
	value = None
	height = None
	balanceFactor = None

"""Insert"""
def insertNode(curr,newNode):
	if (newNode == None):
		return None
	
	if (newNode.key < curr.key):
		if (curr.leftNode == None):
			curr.leftNode = newNode
			newNode.parent = curr
		else:
				return insertNode(curr.leftNode,newNode)
	else:
		if (curr.rightNode == None):
			curr.rightNode = newNode
			newNode.parent = curr
		else:
			return insertNode(curr.rightNode,newNode)
	return newNode


def insert(AVL,value,key):
	newNode = AVLNode()
	newNode.value = value
	newNode.key = key
	newNode.balanceFactor = 0

	if (AVL.root == None):
		AVL.root = newNode
		return newNode
	
	else:
		insertNode(AVL.root,newNode)
		updateAndRebalance(AVL,newNode)

	return newNode


"""Search"""
def searchValue(curr,value):
	if (curr == None):
		return None
	
	if (curr.value == value):
		return curr.key
	else:
		if (curr.leftNode != None):
			return searchValue(curr.leftNode,value)
		if (curr.rightNode != None):
			return searchValue(curr.rightNode,value)
		return None

def search(AVL,value):
	if (AVL.root == None):
		return None
	return searchValue(AVL.root,value)


"""Access"""
def access(AVL,key):
	nodeAccess = getNode(AVL.root,key)
	if (nodeAccess != None):
		return nodeAccess.value

	return None


"""Update"""
def update(AVL,value,key):
	nodeToUpdate = getNode(AVL.root,key)
	if (nodeToUpdate != None):
		nodeToUpdate.value = value
	return nodeToUpdate
	

"""Delete"""
def deleteNode(AVL,curr):
	if (curr == None):
		return None

	if (isLeaf(curr)): #hoja
		if (isLeftChild(curr)):
			curr.parent.leftNode = None
		else:
			curr.parent.rightNode = None
	elif (not hasBothChilds(curr)): #tiene un hijo
		
		if (curr.leftNode != None): 
			leftChild = curr.leftNode
			if (isLeftChild(curr)):
				curr.parent.leftNode = leftChild

			else:
				curr.parent.rightNode = leftChild
			leftChild.parent = curr.parent
			updateBfAndHeight(leftChild.parent)	
		else:
			rightChild = curr.rightNode
			if (isLeftChild(curr)): 
				curr.parent.leftNode = rightChild
			else:
				curr.parent.rightNode = rightChild
			rightChild.parent = curr.parent
			updateBfAndHeight(rightChild.parent)
			
	else: #tiene ambos hijos
		minor = getMinor(curr.rightNode)
		if (isLeftChild(minor)):
			minor.parent.leftNode = None
		else:
			minor.parent.rightNode = None
		minor.parent.balanceFactor = getBalanceFactor(minor.parent)
		minor = replaceNode(minor,curr)
		
		if (AVL.root == curr):
			AVL.root = minor
			
		elif(isLeftChild(curr)):
			curr.parent.leftNode = minor
			minor.parent = curr.parent
		else:
			curr.parent.rightNode = minor
			minor.parent = curr.parent
			
	return curr


def deleteKey(AVL,key):
	nodeToDelete = getNode(AVL.root,key)
	if (nodeToDelete != None):
		deleteNode(AVL,nodeToDelete)
		updateAndRebalance(AVL,nodeToDelete)
	return nodeToDelete


def deleteValue(AVL,value):
	nodeToDelete = getNode(AVL.root,searchValue(AVL.root,value)) #searchValue devuelve la key
	if (nodeToDelete != None):
		deleteNode(AVL,nodeToDelete)
		updateAndRebalance(AVL,nodeToDelete)
	return nodeToDelete


"""Funciones encargadas de mantener el árbol balanceado"""
def reBalance(AVL,curr):
	if (curr == None):
		return None
	
	if (curr.balanceFactor > 1):
		if (curr.leftNode.balanceFactor > 0):
			print("right")
			rightRotate(AVL,curr)
		else:
			print("leftRight")
			leftRightRotate(AVL,curr)
	
	elif (curr.balanceFactor < -1):
		if (curr.rightNode.balanceFactor < 0):
			print("left")
			leftRotate(AVL,curr)
		else:
			print("rightLeft")
			rightLeftRotate(AVL,curr)
	return AVL
    

def rightLeftRotate(AVL,oldRoot):
	rightRotate(AVL,oldRoot.rightNode)
	return leftRotate(AVL,oldRoot)


def leftRightRotate(AVL,oldRoot):
	leftRotate(AVL,oldRoot.leftNode)
	return rightRotate(AVL,oldRoot)

    
def leftRotate(AVL,oldRoot):
	newRoot = oldRoot.rightNode
	oldRoot.rightNode = newRoot.leftNode

	if (newRoot.leftNode != None):
		newRoot.leftNode.parent = oldRoot
	newRoot.parent = oldRoot.parent

	if (oldRoot.parent == None):
		AVL.root = newRoot
	else:
		if (isLeftChild(oldRoot)):
			oldRoot.parent.leftNode = newRoot
		else:
			oldRoot.parent.rightNode = newRoot

	newRoot.leftNode = oldRoot
	oldRoot.parent = newRoot
	updateBfAndHeight(newRoot)
	updateBfAndHeight(oldRoot)


def rightRotate(AVL,oldRoot):
	newRoot = oldRoot.leftNode
	oldRoot.leftNode = newRoot.rightNode

	if (newRoot.rightNode != None):
		newRoot.rightNode.parent = oldRoot
	newRoot.parent = oldRoot.parent

	if (oldRoot.parent == None):
		AVL.root = newRoot
	else:
		if (isRightChild(oldRoot)):
			oldRoot.parent.rightNode = newRoot
		else:
			oldRoot.parent.leftNode = newRoot

	newRoot.rightNode = oldRoot
	oldRoot.parent = newRoot
	updateBfAndHeight(newRoot)
	updateBfAndHeight(oldRoot)



"""Relacionadas con balanceFactor"""
def updateAndRebalance(AVL,curr):
	if (curr == None):
		return None
	updateBfAndHeight(curr)

	if (curr.balanceFactor < -1 or curr.balanceFactor > 1):
		reBalance(AVL,curr)
	if (curr.parent != None):
		updateAndRebalance(AVL,curr.parent)
	return AVL

def updateBfAndHeight(curr):
    if (curr == None):
        return None
    
    curr.height = getHeight(curr)
    curr.balanceFactor = getBalanceFactor(curr)


"""Auxiliares"""
def replaceNode(new,old):
	new.height = old.height
	new.parent = old.parent
	new.balanceFactor = getBalanceFactor(new)
	new.leftNode = old.leftNode
	new.leftNode.parent = new
	new.rightNode = old.rightNode
	new.rightNode.parent = new
	return new


def getNode(curr,key):
	if (curr == None):
		return curr
	if (curr.key == key):
		return curr
	elif (curr.key < key):
		return getNode(curr.rightNode,key)
	elif (curr.key > key):
		return getNode(curr.leftNode,key)


def getMajor(curr):
	if (curr.rightNode == None):
		return curr
	return getMajor(curr.rightNode)


def getMinor(curr):
	if (curr.leftNode == None):
		return curr
	return  getMinor(curr.leftNode)


def getMaxDepth(curr):
    if (curr == None):
        return 0
    return max(getMaxDepth(curr.leftNode), getMaxDepth(curr.rightNode)) + 1

	
def getBalanceFactor(curr):
    if (curr == None):
        return 0
    return getMaxDepth(curr.leftNode) - getMaxDepth(curr.rightNode)


def getHeight(curr):
	if (curr == None):
		return 0

	return 1 + getHeight(curr.parent)


def hasBothChilds(curr):
	return (curr.leftNode != None and curr.rightNode != None)

def isLeftChild(curr):
	return (curr.parent.leftNode == curr)

def isRightChild(curr):
	return (curr.parent.rightNode == curr)

def isLeaf(curr):
	return (curr.leftNode == None and curr.rightNode == None)


"""Recorridos"""
def reverse(LL): 
	mll.reverse(LL)
	return LL

#inorder
def InOrderList(curr,LL):
	if curr!=None:
		InOrderList(curr.leftNode,LL)
		mll.add(LL,curr.key)
		InOrderList(curr.rightNode,LL)
	return LL


def traverseInOrder(B):
	InOrder=mll.LinkedList()
	InOrder=InOrderList(B.root,InOrder)
	return reverse(InOrder)

	
#postorder
def PostOrderList(curr,LL):
	if curr!=None:
		PostOrderList(curr.leftNode,LL)
		PostOrderList(curr.rightNode,LL)
		mll.add(LL,curr.key)
	return LL


def traverseInPostOrder(B):
	PostOrder=mll.LinkedList()
	PostOrder=PostOrderList(B.root,PostOrder)
	return reverse(PostOrder)

	
#preorder
def PreOrderList(curr,LL):
	if curr!=None:
		mll.add(LL,curr.key)
		PreOrderList(curr.leftNode,LL)
		PreOrderList(curr.rightNode,LL)
	return LL


def traverseInPreOrder(B):
	PreOrder=mll.LinkedList()
	PreOrder=PreOrderList(B.root,PreOrder)
	return reverse(PreOrder)

	
#breadthfirst
def traverseBreadFirst(B):
	Queue=mll.LinkedList()
	BFirst=mll.LinkedList()

	mll.add(Queue,B.root)
	while Queue.head!=None:
		curr=mll.dequeue(Queue)
		mll.add(BFirst,curr.key)
		if curr.leftNode!=None:
			mll.add(Queue,curr.leftNode)
		if curr.rightNode!=None:
			mll.add(Queue,curr.rightNode)
	return reverse(BFirst)
