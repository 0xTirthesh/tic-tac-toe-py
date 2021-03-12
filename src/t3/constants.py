P1️ = "1️⃣"
P2️ = "2️⃣"
P3️ = "3️⃣"
P4️ = "4️⃣"
P5️ = "5️⃣"
P6️ = "6️⃣"
P7️ = "7️⃣"
P8️ = "8️⃣"
P9️ = "9️⃣"

CROSS = "❌"
OH = "⭕"

BOARD = """
    {}  {}  {}
    
    {}  {}  {}
    
    {}  {}  {} 
"""

RULES = f"""
Rules: 
 - Game will prompt for the player's turn. Player 1 marks '{CROSS}' and Player 2 marks '{OH}'
 - Player will have to choose the number from the board they wish to mark.
 - The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
 - When all 9 squares are full, the game is over.
"""
