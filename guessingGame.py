import random
correctNumber=random.randrange(1,20)
print('Number Guessing Game')
print('Guess a number between 1 and 20!')
numberEntered= int(input('Enter your desired number: '))
while correctNumber!= numberEntered:
   if correctNumber%2 == 0:
      if numberEntered%2==0 and numberEntered>correctNumber:
         print('Sorry, you number is too big! Try a number which is smaller than ',numberEntered)
         numberEntered= int(input('Enter your desired number: '))

      elif numberEntered%2==0 and numberEntered<correctNumber:
         print('Sorry, you number is too small! Try a number which is bigger than ',numberEntered)
         numberEntered= int(input('Enter your desired number: '))
      elif numberEntered%2 != 0 :
         print('Sorry, it is not an odd number. Please try with an even number ')
         numberEntered= int(input('Enter your desired number: '))
         

   elif correctNumber%2 != 0:
      if numberEntered%2!= 0 and numberEntered>correctNumber:
         print('Sorry, you number is too big! Try a number which is smaller than ',numberEntered)
         numberEntered= int(input('Enter your desired number: '))

         
      elif numberEntered%2!=0 and numberEntered<correctNumber:
         print('Sorry, you number is too small! Try a number which is bigger than ',numberEntered)
         numberEntered= int(input('Enter your desired number: '))

         
      elif numberEntered%2 == 0 :
         print('Sorry, it is not an even number. Please try with an odd number ')
         numberEntered= int(input('Enter your desired number: '))

         
   
if numberEntered == correctNumber:
    print('Congradulations! You read my mind')    




    

