import math

def decrypt(key, message):
    numOfColumns = math.ceil(len(myMessage) / myKey)
    numOfRows = key
    messageLength = len(message)
    numOfShadedBoxes = (numOfRows * numOfColumns) - (messageLength)
    numFull = numOfRows - numOfShadedBoxes
    columnText = numOfColumns * ([''])

    # Get the text from the full rows
    for block in range(numFull):
        # print(f"full block is {block}")
        for char in range(numOfColumns):
            mesIndex = block*numOfColumns
            columnText[char] += message[(mesIndex+char)]

    # Get the text from the last row
    start_ind = (block + 1) * numOfColumns
    # print(f"start ind at beg is {start_ind}")
    num_of_full_col = numOfColumns - 2
    col_ind = 0
    while start_ind < messageLength:
        # print(f"start ind is {start_ind} and col ind is {col_ind}")
        columnText[col_ind] += message[start_ind]
        if col_ind < num_of_full_col:
            col_ind += 1
        else:
            col_ind = 0
        start_ind += 1

    finalText = ''.join(columnText)
    return finalText

myKey = 2
myMessage = "Hloti sm in etsrn.Ddi ok???el hsi ygatts tig i twr!!!"
result = decrypt(myKey, myMessage)
print(result)