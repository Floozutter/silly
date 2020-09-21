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
	
	return 0;
}
