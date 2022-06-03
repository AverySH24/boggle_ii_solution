from random import randrange


class BoggleBoard:
  dice = ["AAEEGN","ELRTTY","AOOTTW","ABBJOO","EHRTVW","CIMOTU","DISTTY","EIOSST","DELRVY","ACHOPS","HIMNQU","EEINSU","EEGHNW","AFFKPS","HLNNRZ", "DEILRX"]
  def __init__(self):
    self.board = [[],[],[],[]]

  def shake(self):
    hold = BoggleBoard.dice
    for x in range(0, 4):
      for y in range(0,4):
        randIndex = randrange(len(hold))
        pick1 = hold[randIndex]
        hold.remove(hold[randIndex])
      
        pick2 = pick1[randrange(6)] 
        self.board[x].append(pick2)



  def printBoard(self):
    for x in self.board:
      total = ""
      for y in x:
        if (y == 'Q'):
          y = "Qu"
        total += y + " "
      print(total)

  
  def in_board(self, word):
    #OOPS forgot to mention this earlier, but I forgot to take care of the Qu.
    #Here, I'm taking care of that before I run the recursion
    
    if (self.notValidInput(word.upper())):
      print("Not a possible input. Q must be followed by u.")
      return False
    word = word.upper().replace("QU", "Q")

    start = []
    #Create within the board for all the starting coordinates
    for val in range(0, len(self.board)):
      for val2 in range(0, len(self.board)):
        if self.board[val][val2] == word[0]:
          start.append([val, val2])
    for x in range(0, len(start)):
      if self.minimize(word[1:len(word)], start[x]):
        return True
    return False

  def minimize(self, word, location, checked = []):
    if word == "":
      return True
    #IF in range and not in checked, add to agenda
    nums = [0, 1, -1]
    nums2 = [0, 1, -1]
    agenda = []
    #Check all characters areound the current location
    #If they match the first letter of the word (the "next" letter) add it to the agenda
    for x in nums:
      for y in nums2:
        if self.in_range([location[0] + x, location[1] + y]) and not self.within_array([location[0] + x, location[1] + y], checked):
          agenda.append([location[0] + x, location[1] + y])

    bool_results = []
    #Go through each box that was set in the agenda and call the next line per word
    for y in range(0, len(agenda)):
      if self.board[agenda[y][0]][agenda[y][1]] == word[0]:
        copy = checked
        copy.append(y)
        bool_results.append(self.minimize(word[1:len(word)], [agenda[y][0], agenda[y][1]], copy))
    
    for x in bool_results:
      if x:
        return True
    return False


  def in_range(self, index):
    return index[0] >= 0 and index[0] < 4 and index[1] >= 0 and index[1] < 4

  def within_array(self, index, array):
    for x in array:
      if x == index:
        return True
    return False

  def clearBoard(self):
    self.board = [[],[],[],[]]

  def notValidInput(self, userInput):
    if ("Q" in userInput) and not ("QU" in userInput):
      return True
    return False



#Test for the boggle board
#type quit to exit the program
#Input your guess at the >
def run_board():
  bog = BoggleBoard()
  bog.shake()
  while True:
    bog.printBoard()
    userInput = input("> ")
    if userInput == "quit":
      break
    print(f"{bog.in_board(userInput)}\n")

run_board()
