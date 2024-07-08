import random as rd
import emoji 
TOTALLINES=8
CHANCES=8
# print(randomValue)
def getRandomWord():
    randomValue=rd.randrange(0,TOTALLINES) #chooses a random line from txt
    f=open("wordsList.txt")
    line=f.read().splitlines()
    randomWord=line[randomValue]
    word=randomWord.split()
    # randomWord.split()
    GuessWord=list(word[0])
    HintWordList=word[1:]
    HintWord=""
    for i in HintWordList:
        HintWord=HintWord+i+" "
    return GuessWord,HintWord
    # print(GuessWord," :- ",HintWord)

def StartTemplate(guess:str,hint):
    print("🤩 Welcome to the HANGMAN Game :- 🤔")
    print("\t\t\tQuestion Hint :- ",hint)
    question=("_ "*len(guess)).split(" ")
    question.remove("")
    print("\t\t\tQUESTION :- ","_ "*len(guess))
    return question

def updateQuestion(question:list,template:list,letter):
     count=0
     for i in question:
          if(i == letter):
               break
          count+=1
     question.pop(count)
     question.insert(count,"_")
     
     template.pop(count)
     template.insert(count,letter)
     print("\t\t\tLetter found 👀 :- ",template)
     
     

if __name__=="__main__":
        guessWord,hintWord=getRandomWord()
        templateQuestion=StartTemplate(guessWord,hintWord)
        while True:
            print("\t\t\tYour Total CHANCES 🫁  = ",CHANCES)
            if templateQuestion.count("_")==0:
                      print("😎 YAYYY YOU WON 🥳")
                      break
            if(CHANCES==0):
                 w=""
                 print("the word was :- ",(w.join(guessWord)).capitalize())
                 print("💀 YOU ARE HANGED ☠ 👻")
                 break
            answer=input("TYPE YOUR LETTER HERE 👉 :- ")
            CHANCES-=1
            if answer == "exit":
                break
            elif len(answer)!=1:
                 print("\t\t\tenter proper word 😾")
                 CHANCES+=1
                 continue
            elif answer.lower() in guessWord:
                 CHANCES+=1
                 updateQuestion(guessWord,templateQuestion,answer.lower())
            else:
                 print("\t\t\tTRY AGAIN 🤞")
            
        print("game completed")
                 

                 

    
    
    


