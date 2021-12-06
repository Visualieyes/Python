#Write an immutable function that merges the following inputs into a single list. (Feel free to use the space below or submit a link to your work.)

# Inputs
# - Original list of strings
# - List of strings to be added
# - List of strings to be removed

# Return
# - List shall only contain unique values
# - List shall be ordered as follows
# --- Most character count to least character count
# --- In the event of a tie, reverse alphabetical

# Other Notes
# - You can use any programming language you like
# - The function you submit shall be runnable

# For example:

# Original List = ['one', 'two', 'three',]
# Add List = ['one', 'two', 'five', 'six]
# Delete List = ['two', 'five']
# Result List = ['three', 'six', 'one'] 


def main(ogList, addList, delList):

  #first add unique values
  for i in addList:
    if i not in ogList:
      ogList.append(i)

  #Now del items from og list
  for i in delList:
    if i in ogList:
      ogList.remove(i)

  print(ogList)

  #sort the list by len
  ogList.sort(key=len, reverse=True)
  
  #sort for event of a tie and reverse alphabetical
  for i in range(len(ogList)):
    for j in range(i+1, len(ogList)):
      if ( len(ogList[j]) == len(ogList[i]) and (ogList[j][0] > ogList[i][0]) ):
        temp = ogList[i]
        ogList[i] = ogList[j]
        ogList[j] = temp

  print(ogList)
  return ogList
 
  

main(['one', 'two', 'three',], ['one', 'two', 'five', 'six'], ['two', 'five'])