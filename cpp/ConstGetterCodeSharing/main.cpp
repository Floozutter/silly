/**
 * A demonstration of how to use a const getter in a non-const getter in order
 * to avoid duplicating code that should be shared between both getters, using
 * a Wrapper class that counts the number of times its getters have been
 * called.
 *
 * https://stackoverflow.com/a/123995
 */

#include <iostream>

template <typename T>
class Wrapper {
	public:
		// Wrappers must be initialized. (Avoid uninitialized const Wrappers.)
		Wrapper(T value) : value{value}, counter{0} {}
		Wrapper() = delete;
		// Disable copying. (Should the counter be copied? Ambiguous.)
		Wrapper(Wrapper const &) = delete;
		Wrapper & operator=(Wrapper const &) = delete;
		// Returns the number of times the Wrapper's getters have been called.
		unsigned int get_count() const {
			return counter;
		}
		// Const and non-const getters.
		T const & get() const {
			++counter;  // Code that must be shared between getters.
			return value;
		}
		T & get() {
			return const_cast<T &>(static_cast<Wrapper const *>(this)->get());
		}
	private:
		T value;
		unsigned int mutable counter;
};

int main() {
	Wrapper<int> a{999999};
	a.get() = 142857;
	const Wrapper<int> b{7};
	
	std::cout << "Wrapper a has: " << a.get() << std::endl;
	std::cout << "Wrapper b has: " << b.get() << std::endl;
	std::cout << "Getters called on a: " << a.get_count() << std::endl;
	std::cout << "Getters called on b: " << b.get_count() << std::endl;

	return 0;
}
