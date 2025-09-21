def findClosestValueInBst(root, target):
    return findClosestValueInBstHelper(root, target, float("inf"))

def findClosestValueInBstHelper(currentNode,target,closest):
    
    while currentNode is not None:
        if(abs(target - closest) > abs(target - currentNode.value)):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break

    return closest

