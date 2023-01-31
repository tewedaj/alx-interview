
#!/usr/bin/python3
"""there are 3 conditions if the size of the array is 0 then it can be opend
    and  if it has size more than zero it has to have more than 0 size inorder for the next array to be opend 
"""


def canUnlockAll(boxes):
    """create an empty opject to track how many are unlocked """
    x = 0
    unlockedList = {}

    for box in boxes:
        """We enter into the first array/list and we loop turgh it checking 
                all conditions """
        if len(box) == 0 or x == 0:
            """if the size of the array is 0 or if the x is the 0th x
                we automaticly pass it as it is open according to the role"""
            unlockedList[x] = "always_unlockedList"
        for val in box:
            if val < len(boxes) and val != x:
                """ since each value is a key we use it to add value to our unlocked list
                    by doing that we can add the size of the unlocked list and we don't have to
                    worry about duplicates since douplicates will overide on them self instead
                    of adding on to the total value """
                unlockedList[val] = val
        if len(unlockedList) == len(boxes):
            return True
        x += 1
    return False