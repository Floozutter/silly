/**
 * A demonstration of how when you dereference matters, for Victor.
 */

#include <iostream>


int main() {
	const int arr[] = {0, 10, 20, 30, 40};
	std::cout << "Dereference First: " << *arr + 1 << std::endl;
	std::cout << "Dereference Last: " << *(arr + 1) << std::endl;
}
