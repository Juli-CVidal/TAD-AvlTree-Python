"""nombre: Julián Vidal
Ejercitación TAD LinkedList"""
class LinkedList:
	head=None

class Node:
	value=None
	nextNode=None

def printlist(L):
	actN=L.head
	print("[",end="")
	while actN!=None:
		print (actN.value, end="")
		if actN.nextNode!=None:
			print("",end=", ")
		actN=actN.nextNode
	print ("]")

def add(L,element):
	addNode=Node()
	addNode.value=element
	addNode.nextNode=L.head
	L.head=addNode
#Complejidad constante en lista, tad no utilizado en array

def length(L):
	leng=0
	act=L.head
	while act!=None:
		act=act.nextNode
		leng+=1
	return leng
#Complejidad lineal en lista, constante en array

def search(L,element):
	if length(L)==0:
		return None
	else:
		act=L.head
		pos=0
		for i in range(0,length(L)):
			if act.value==element:
				return pos
			else:
				act=act.nextNode
				pos+=1
#Complejidad lineal, tanto en lista como en array

def insert(L,element,pos):
	act=L.head
	actP=0 #posición actual
	if pos==0:
		add(L,element)
		return pos
	else:
		while act!=None and actP<pos-1:
			act=act.nextNode
			actP+=1
	if act==None:
		return None
	else:
		insNode=Node()
		insNode.value=element
		insNode.nextNode=act.nextNode
		act.nextNode=insNode
		actP+=1

		return actP
#Complejidad lineal, tanto en lista como en array

def delete(L,element):
	pos=search(L,element)
	
	if pos==0:
		L.head=L.head.nextNode
	elif pos==None:
		return None
	else:
		act=L.head
		for i in range(0,pos-1):
			act=act.nextNode
		act.nextNode=act.nextNode.nextNode
		
		return pos
#Complejidad lineal, tanto en lista como en array

def access(L,pos):
	act=L.head
	for i in range(0,pos):
		if act==None: break
		else:
			act=act.nextNode
	if act==None:
		return None
	else:
		return act.value
#Complejidad lineal en lista, constante en array

def update(L,element,pos):
	act=L.head 	#nodo actual
	actP=0			#posición actual
	while actP<pos and act!=None:
		act=act.nextNode
		actP+=1
	
	if act==None:
		return None
	else:
		act.value=element
		return actP
#Complejidad lineal en lista, tad no implementado en array

def reverse(L):
	prev=None #nodo anterior
	act=L.head #nodo actual
	nextt=act.nextNode #nodo siguiente
	while act!=None:
		act.nextNode=prev
		prev=act
		act=nextt
		if nextt!=None:
			nextt=nextt.nextNode
	L.head=prev


def enqueue(Q,element):
	add(Q,element)


def dequeue(Q):
	curr=Q.head
	if curr==None:
		return None
	elif curr.nextNode==None:
		Q.head=None
		return curr.value
	else:
		prev=Q.head
		curr=Q.head.nextNode
		while curr.nextNode!=None:
			prev=curr
			curr=curr.nextNode
		prev.nextNode=None

		return curr.value