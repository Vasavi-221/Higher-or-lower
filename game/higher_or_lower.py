import random
print("Welcome to the higher or lower game!")
score=0
crrnt_nmbr = random.randint(1,100)
while True:
  print(f"\n Current number is:{crrnt_nmbr}")
  guess = input("Will the next number be (H)igher or (L)ower?").lower()
  if guess not in['h','l']:
    print("Invalid input. Please enter 'H' or 'L'.")
    continue
  nxt_nmbr = random.randint(1,100)
  print(f"The next number is:{nxt_nmbr}")
  if(guess=='h' and nxt_nmbr>crrnt_nmbr) or (guess=='l' and nxt_nmber<crrnt_nmbr):
    score+=1
    print("Correct! Your score is:", score)
    crrnt_nmber=nxt_nmbr
  elif nxt_nmbr==crrnt_nmbr:
    print("It's the same number! No points. Try again.")
  else:
    print("Wrong guess.Game over.")
    print("Final score:",score)
    break
