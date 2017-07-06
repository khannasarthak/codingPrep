def convertFive(n):
    #Code here
    myl = list(str(n))
    new_items = [x if (x != '0') else '5' for x in myl]
    k = int(''.join(map(str,new_items)))
    return (k)
# IMP as it shows how to replace all items with a new one in a list, might be used in other questions
# https://stackoverflow.com/questions/1540049/replace-values-in-list-using-python