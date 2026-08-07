# 🎰 Python CLI Slot Machine

A terminal-based slot machine game built from scratch in Python, using **NumPy** for weighted random choices and custom conditional logic for dynamic win/loss multipliers.

---

## 🌟 Features

* **Weighted Symbol Probabilities:** Powered by NumPy's `random.choice`, giving high-paying symbols rarer odds while keeping common symbols frequent.
* **Scatter & Combo Mechanics:**
  * **Fruit Combos:** Payouts for matching 3-of-a-kind (Cherries, Lemons, Peaches, Kiwis).
  * **Coconut Multipliers:** Earn bonuses for landing 1 or 2 Coconuts, or hit a massive **x10 balance multiplier** on 3 Coconuts.
  * **Bomb Penalties:** Single and double Bombs deduct balance, while landing 3 Bombs triggers an instant **TRIPLE BOMBER** wipeout (Balance = $0).
* **Simultaneous Event Resolution:** Independent logic checks ensure both bonuses (Coconuts) and penalties (Bombs) resolve on the same spin if landed together.
* **Quit & Cash-Out Option:** Safely exit the loop at any time by entering `q` to view your final balance.

---

## 📊 Symbol Odds & Payout Table

| Symbol | Name | Odds (Weight) | Outcome / Payout |
| :---: | :--- | :---: | :--- |
| 🍒 | Cherry | 22.0% | **3-of-a-kind:** +$35 |
| 🍋 | Lemon | 22.0% | **3-of-a-kind:** +$35 |
| 🍑 | Peach | 14.0% | **3-of-a-kind:** +$45 |
| 🥝 | Kiwi | 10.0% | **3-of-a-kind:** +$150 |
| 🥥 | Coconut | 9.5% | **Single:** +$20 \| **Double:** x2 Balance \| **Triple:** x10 Balance |
| 💣 | Bomb | 22.5% | **Single:** -$10 \| **Double:** -$15 \| **Triple:** Balance = 0 |

---


### Prerequisites

Make sure you have Python installed, along with the `numpy` library.

```bash
pip install numpy
