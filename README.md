Bomb Man
1.	Game Introduction
A game contains n players, n can be chosen (n <= 4, recommended 3). Each player has infinite bomb to plant but have a 1.5s CD. Each bomb will release cross shape laser after 1.5s bomb have been planted. The laser can be stopped by obstacles and boundaries but will lower HP of obstacles (initial 2, -1 when be shotted), once HP of a obstacle below 0, it will be removed. Because of system difference, we recommand to play on windows system, the unroot linux(ed) version only support 1 player playing with bots. Also movement in unroot linux will have delay.
Each player has same initial HP 10, HP will decrease by 2 if they are shotted by laser, laser will penetrate the player. After being shotten by laser, the player will get 2s dodging all lasers. If HP downs below 0, the player is removed from the map. If there is 1 player left, game stopped

2.	Winning conditions
Once the game stops, there is a rating for each player. Surviving rank contains 80% of it and damage done contains 20%. This score will multiply with 1.5^n while n is killing number to form final score. Player with highest score wins.
3.	Game Menu
The game menu contains three choices (start, setting and quit). Player can use direction key to select, and use enter to confirm. Setting is for player to change keyboard settings (not recommended change default). If play is chosen, turn to the page of entering number of players and start the game. 
After the game, the program will show congratulations to winner and give a list of ranking of final score, containing diverse scores (placement, damage done and killing score).
