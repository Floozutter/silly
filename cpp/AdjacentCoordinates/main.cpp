/**
 * A collection of different ways to visit the adjacent coordinates of a given
 * coordinate for a two-dimensional array.
 */

#include <iostream>

int main() {
	char const grid[3][3] = {
		{'#', '3', '#'},
		{'4', '@', '2'},
		{'#', '1', '#'}
	};
	int const row = 1;
	int const col = 1;
	
	std::cout << "By hand:" << std::endl;
	std::cout << grid[row+1][col] << std::endl;
	std::cout << grid[row][col+1] << std::endl;
	std::cout << grid[row-1][col] << std::endl;
	std::cout << grid[row][col-1] << std::endl;
	
	std::cout << "Row difference and column difference arrays:" << std::endl;
	int const dr[] = {1, 0, -1, 0};
	int const dc[] = {0, 1, 0, -1};
	for (size_t i = 0; i < 4; ++i) {
		std::cout << grid[row + dr[i]][col + dc[i]] << std::endl;
	}
	
	std::cout << "Coordinate difference array:" << std::endl;
	struct {
		int row;
		int col;
	} const dco[] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
	for (size_t i = 0; i < 4; ++i) {
		std::cout << grid[row + dco[i].row][col + dco[i].col] << std::endl;
	}
	
	return 0;
}
