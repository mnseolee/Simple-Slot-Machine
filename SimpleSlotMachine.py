import numpy as np

balance = 100
spin_fee = 5

#--GAME LOOP--
while balance >= 5:
        action = input("Action: ")
        if action == "p":
                balance -= spin_fee
                spin = (np.random.choice(["🍒", "🍋", "🍑", "🥝", "🥥", "💣"], p=[0.22, 0.22, 0.14, 0.1, 0.095, 0.225], size=3))
                print(f"{spin}  Current Balance: {balance}")

                if spin[0] == "🍒" and spin[1] == "🍒" and spin[2] == "🍒":
                        balance += 35
                        print("Cherry Combo! +35")

                if spin[0] == "🍋" and spin[1] == "🍋" and spin[2] == "🍋":
                        balance += 35
                        print("Lemon Combo! +35")

                if spin[0] == "🍑" and spin[1] == "🍑" and spin[2] == "🍑":
                        balance += 45
                        print("Peach Combo! +45")

                if spin[0] == "🥝" and spin[1] == "🥝" and spin[2] == "🥝":
                        balance += 150
                        print("-Kiwi Combo!- +150")

                if "💣" in spin:
                        bomb_count= list(spin).count("💣")
                        if bomb_count == 1:
                                balance -= 10
                                print("Bomb Single! -10")
                        elif bomb_count == 2:
                                balance -= 15
                                print("Bomb Double! -15")
                        elif bomb_count == 3:
                                balance = 0
                                print("-TRIPLE BOMBER- BALANCE SET 0")
                    
                if "🥥" in spin:
                        coconut_count= list(spin).count("🥥")
                        if coconut_count == 1:
                                balance += 20
                                print("Coconut Single! +20")
                        elif coconut_count == 2:
                                balance = balance * 2
                                print("Coconut Double! x2")
                        elif coconut_count == 3:
                                balance = balance * 10
                                print("TRIPLE COCONUT! x10")

        if action == "q":
                print(f"You have quit the game!     Final Balance: {balance}")
                break


if balance < 5:
        print("Insufficient credits. GAME OVER!")



