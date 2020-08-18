#include <cstdio>


template <unsigned int n>
struct PI {
	static constexpr double value = (
		PI<n-1>::value
		+ (n%2 ? -4.0 : 4.0) / (2*n + 1)
	);
};
template <>
struct PI<0> {
	static constexpr double value = 4;
};

constexpr unsigned int N = 900;
constexpr double COMPI = PI<N>::value;


int main() {
	std::printf("%f\n", COMPI);
	return 0;
}
