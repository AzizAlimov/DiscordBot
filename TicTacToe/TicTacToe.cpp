// tictactoe.cpp
#include <iostream>

//Constructor
TicTacToe::TicTacToe() {

	srand(time(0));
	player = 1;

}

//Creates the board
void TicTacToe::makeBoard() {

	for (int i=0; i<9; i++) {
		board[i] = " ";
	}

}

//Gives visual representation of board
void TicTacToe::drawBoard(){
	std::cout << board[0] << " | " << board[1] << " | " << board[2]
			  << "\n---|-----|---\n"
			  << board[3] << " | " << board[4] << " | " << board[5]
			  << "\n---|-----|---\n"
			  << board[6] << " | " << board[7] << " | " << board[8]
			  << std::endl
}

void TicTacToe::printPlayerTurn() {
	std::cout << "Player "
			<< player
			<< ", enter the board position you would like to play: " 
			<< endl;
}

//Executes one turn of the game
void TicTacToe::PlayerTurn() {
	printPlayerTurn();

	int move;

	do
	{
		std::cin >> move;
		move--;
		if (move<0 || move>8 || pos[move]!=0) {
			std::cout << "\nInvalid move";
		}
	}
	while (move<0 || move>8 || pos[move] != 0);

	board[move] = player
}

void TicTacToe::play() {
	do {
		drawBoard();
		PlayerTurn();
	} while (!WinningCond())
}

//If a player is in a winning position, returns true, otherwise false
boolean TicTacToe::WinningCond(){
	

}

