import sys

health = 10
atk = 1
choice = 0
Enemy1Alive = True
Enemy2Alive = True
bossAlive = True
switchActivated = False
GateDiscovered = False
daggerFound = False
cloakFound = False

print("------------------------°°..°°------------------------")
input("\n > You enter a gloomy forest, not knowing why you are here")
input(" > You just know you have to proceed")

while health > 0 and bossAlive:
  print("\n > You are at the entrance of the forest.\n   The trees are tall, and the light is dim")
  print("   There is a sign showing you 3 routes : \n    1)Right\n    2)Left\n    3)Forward")
  choice = int(input())

  #Right
  if choice == 1:
    input(" > You turn right")
    if Enemy1Alive:  #Combat scene 1
      input(" > There is a Goblin ahead")
      input(" > You engage the combat")
      print("\n//////////////////////////////////////////////////////\n")
      enemyLife = 4
      enemyAtk = 1
      yourLife = health
      while enemyLife > 0:  #you cant die there, so no condition on your life
        input(" ~ You attack")
        print(" ~ You did ", atk, " damages")
        input()
        enemyLife -= atk
        input(" ~ The ennemy attacks")
        yourLife -= enemyAtk
        print(" ~ You lost ", enemyAtk, " HP. ", yourLife, " HP remaining")
        input()
      print("\n//////////////////////////////////////////////////////\n")
      input(" > You won, the goblin is dead")
      input(" > Your have been healed")
      Enemy1Alive = False
      input(" > After this combat you return to the entrance of the forest\n")

    else:
      input(" > There is nothing to see here, you chose to return to the entrance\n")

  #Left
  elif choice == 2:
    input(" > You turn left")
    choice = 0
    if Enemy2Alive:  #Combat scene 2
      input(" > There is an evil Pixie ahead")
      input(" > You engage combat")
      print("\n//////////////////////////////////////////////////////\n")
      enemyLife = 4
      enemyAtk = 1
      yourLife = health
      while enemyLife > 0:  #you cant die there, so no condition on your life
        input(" ~ You attack")
        print(" ~ You did ", atk, " damages")
        input()
        enemyLife -= atk
        input(" ~ The ennemy attacks")
        yourLife -= enemyAtk
        print(" ~ You lost ", enemyAtk, " HP. ", yourLife, " HP remaining")
        input()
      print("\n//////////////////////////////////////////////////////\n")
      input(" > You won, the Pixie is dead")
      input(" > Your have been healed") 
      Enemy2Alive = False

    while choice != 3:
      input("\n > In front of you are two stone ruins")
      print(" > You can choose to go :")
      print("    1) in the one to your left")
      print("    2) the one to your right")
      print("    3) or return to the entrance")
      choice = int(input())

      if choice == 1:  #atk boost
        if not daggerFound :
          input(" > You enter the ruin on your left")
          input(" > In that ruin you see a chest, you decide to open it")
          input(" > In that chest you find a dagger, you feel more powerful")
          atk += 3
          input(" > Your attack has increased")
          input(" > You exit the ruin")
          daggerFound = True
        else :
          input(" > You already been here. That is where you found the dagger")

      elif choice == 2:  #Health boost
        if not cloakFound :
          input(" > You enter the ruin on your right")
          input(" > In that ruin you see a chest, you decide to open it")
          input(" > In that chest you find a cloak, you feel protected")
          health += 10
          input(" > Your health has increased")
          input(" > You exit the ruin")
          cloakFound = True
        else :
          input(" > You already been here. That is where you found the cloak")

      elif choice == 3:
        input(" > You return to the entrance")

      else:
        input(" # This path dont exist")

  #Forward
  elif choice == 3:
    choice = 0
    print(" > You proceed forward")

    while choice != 3:
      input("\n > You are at a branching route. There is two ways.")
      input(" > Between those ways is a skull on a spade. You feel close to the end")
      print(" > You can choose to go :")
      print("    1) to your left")
      print("    2) to your right")
      print("    3) or return to the entrance")
      choice = int(input())

      if choice == 1:  #Switch
        input(" > You turn left")

        #switch can be activated only if you find gate
        print(" > There is a switch")
        if GateDiscovered:
          input("   That might be usefull to open the gate, you activate switch. There is a big noise")
          switchActivated = True
        else:
          input("   You wonder for what is it for. You should investigate the forest more.")
        input(" > You return to the branching route")

      elif choice == 2:  #gate
        input(" > You turn right")
        
        print(" > There is a HUUGE gate")
        
        #if swtch activated then gate open
        if switchActivated:
          input(" > It is now open")
          choice = 0
          while choice != 2 and choice != 1 :
            if not cloakFound or not daggerFound:
              print(" ! You havent found all the gears aviable, there is a dangerous enemy ahead, do you wish to proceed?")
              print("    1) Yes\n    2) No")
            else:
              print(
                  " > You feel you are prepared for the danger ahead, do you wish to proceed?\n  1) Yes\n  2) No"
              )
            choice = int(input())
  
            if choice == 1:  #boss zone

              #plot
              input(" > You see a strange cabin")
              input(" > You wonder why it was closed behind a gate this huge")
              input(" > You feel drawn to the door")
              input(" > You get closer and decided to knock")
              input(" > An old, bearded man open the door, angry")
              input(" > He waves a glowing scepter to you")
              input(" - who dare disturbing my reading. You will perish!")
              
              input(" > The combat starts")
              print("\n//////////////////////////////////////////////////////\n")
              enemyLife = 10
              enemyAtk = 4
              yourLife = health
              while yourLife > 0 and enemyLife > 0:
                input(" ~ You attack")
                print(" ~ You did ", atk, " damages")
                input()
                enemyLife -= atk
                if enemyLife > 0 :
                  input(" ~ The ennemy attacks")
                  yourLife -= enemyAtk
                  print(" ~ You lost ", enemyAtk, " HP. ", yourLife, " HP remaining")
                  input()
              print("\n//////////////////////////////////////////////////////\n")
              if enemyLife <= 0:
                input(" > You won, the evil Sorcerer is dead")
                input(" > Behind the shack is a way out of the forest. Finally")
                bossAlive = False
                break
              else:
                print(" > You are dead, you failed your mission, whatever it was")
                print(" > You should have been more prepared")
                health = 0
                break
  
            elif choice == 2:
              input(" > You return to the branching route")
  
            else:
              input(" # This path dont exist")

        else:
          input(" > It is closed, you need to fine a way to open it")
          input(" > You return to the branching route")
          GateDiscovered = True
        if not bossAlive  or health == 0:
          break
  else:
    input(" # This path dont exist")

if not bossAlive:
  print("\n___.oO You won, you found your way out and beated the bad guy Oo.___")

print("\n\n________________THE END________________")
