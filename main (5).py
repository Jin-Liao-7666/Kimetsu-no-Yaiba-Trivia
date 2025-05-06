#introduction
again = True
while again == True:
  print("WELCOME TO...")
  print("")
  print("KIMETSU NO YAIBA TRIVIA")
  print("This is a Trivia based on both the anime and manga series of Kitmetsu no Yaiba. There will be three difficulties with three questions each. You get 1 point per question. There will also be 3 additional chances if you get the answer wrong. 0.5 points will still be rewarded if you get the answer right within those attempts. Have fun!")
  #choosing difficulty
  print("")
  print("Choose a difficulty: ")
  point = 0
  question_list_e = [
  "What year was the Kimetsu no Yaiba -The Movie: Mugen Train released? ", 
  "Which Hashira died during the movie? \n 1)Shinobu \n 2)Rengoku \n 3)Giyuu \n 4)Muzan ",
  "How many Hashira’s are there (dead or alive)? "]
  question_list_m = [
  "How many manga volumes are there in Kimetsu no Yaiba?" ,
  "How do you spell Muzan’s Surname? ",
  "How many Hashira’s were still alive after the final fight with Muzan? "]
  question_list_h = [
  "By December 2020, how much money did Kimetsu no Yaiba generate from their sales? (¥)" ,
  "How old is Tanjiro at the start of the story?" ,
  "How many family members does Tanjiro have?"]
  answer_list_e = ["2020", "2", "12"]
  answer_list_m = ["23", "Kibutsuji", "2"]
  answer_list_h = ["1 trillion", "13", "8"]
  sad_e = [" ", "Rengoku died slowly after being pierced through by the 3rd upper moon, Akaza. He died with a smile on his face.", "Hashiras/pillars are the strongest fighters in the demon slayer corp"]
  sad_m = ["", "", "Giyuu and Sanemi were the only surviving Hashiras until the end. "]
  sad_h = ["Kimetsu no Yaiba was a huge success, both in Japan and globally. It became one of the highest-grossing media franchises of all time.", "Tanjiro was only 13 when he saw his family massacred. ", "Tanjiro had a total of 8 siblings, the second oldest being Nezuko. "]
  print()
  print("Easy, Medium, Hard ")
  print()
  dif = input()
  questionlist = []
  answerlist = []

  if dif == "Easy" or dif == "easy":
    questionlist = question_list_e
    answerlist = answer_list_e
  elif dif == "Medium" or dif == "medium":
    questionlist = question_list_m
    answerlist = answer_list_m
  elif dif == "Hard" or dif == "hard":
    questionlist = question_list_h
    answerlist = answer_list_h
  print("***********************************************")
  for i in range (len(questionlist)):
    print("")
    print("QUESTION " + str(i+1))
    print(questionlist[i])
    print("")
    guess = input()
    if guess == answerlist[i]:
      point = point + 1
      print("Correct!")
    else:
      chances = 3
      for b in range (2):
        chances = chances - 1
        print("Try again. You have " + str(chances) + " chances ")
        guess = input()
        if guess == answerlist[i]:
          point = point + 0.5
          print("")
          print("Correct. You get 0.5 point")
          break
        if chances == 1:
          print("The correct answer is " + answerlist[i])
          break
    print("You have " + str(point) + " points out of  " + str(i+1))
    print("")
    if dif == "Easy" or dif == "easy":
      print(sad_e[i])
    elif dif == "Medium" or dif == "medium":
      print(sad_m[i])
    elif dif == "Hard" or dif == "hard":
      print(sad_h[i])
    print("")
    print("*********************************************")
    print("")
  print("")
  print("You got " + str(point) + "/3 on " + dif + " mode")
  if point == 3:
    print("Wow! You got a perfect score!👍👍👍👍👍👍👍👍👍👍👍")
  elif point >=2:
    print("Nice! You did great.")
  else:
    print("Maybe Kitmetsu no Yaiba wasn't your thing 😭")
  print("")
  print()

  again = input("Would you like to try again? (Y/N) ")
  if again == "Y":
    again = True
    print("*********************")
  else:
    print("Thank you for playing! Hope to see you soon! 😃")
    break