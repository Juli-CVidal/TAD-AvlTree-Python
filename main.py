import myAvlTree as mAvl
import myLinkedList as mll

AVL = mAvl.AVLTree()

values = ["h", "c", "n", "a", "f", "l", "b", "e", "g", "j", "d", "i", "k"]
keys = [60, 41, 74, 16, 53, 65, 25, 46, 55, 63, 42, 62, 64]

for i in range(len(values)):
    mAvl.insert(AVL, values[i], keys[i])

bFirst = mAvl.traverseBreadFirst(AVL)
mll.printlist(bFirst)

print(f"\nAltura del árbol: {mAvl.heightWithRoot(AVL.root)}")
leftLimit = 41
rightLimit = 63
print(f"\nCantidad de nodos entre {leftLimit} y {rightLimit}: {mAvl.countNodes(AVL.root,leftLimit,rightLimit)}")

key = 53
print(f"\nKey del nodo a eliminar: {key}")
mAvl.deleteKey(AVL,key)
bFirst = mAvl.traverseBreadFirst(AVL)
mll.printlist(bFirst)