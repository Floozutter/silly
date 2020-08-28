#include <functional>
#include <iostream>


int main() {
	auto Object = [](int value){
		return [=]() mutable {
			const struct {
				std::function<int()> getValue;
				std::function<void(int)> setValue;
			} methods = {
				[&](){ return value; },
				[&](int v){ value = v; }
			};
			return methods;
		};
	};
	
	std::cout << "Creating objects a and b..." << std::endl;
	auto a = Object(0);
	auto b = Object(16);
	
	std::cout << "a's value: " << a().getValue() << std::endl;
	std::cout << "b's value: " << b().getValue() << std::endl;
	
	std::cout << std::endl;
	std::cout << "Mutating objects a and b..." << std::endl;
	a().setValue(1);
	b().setValue(b().getValue() + 9);

	std::cout << "a's value: " << a().getValue() << std::endl;
	std::cout << "b's value: " << b().getValue() << std::endl;
	
	return 0;
}
