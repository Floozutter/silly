#include <cstdio>


template <unsigned long long int a, unsigned long long int b>
struct GCD {
	static constexpr unsigned long long int value = GCD<b, a % b>::value;
};
template <unsigned long long int a>
struct GCD<a, 0> {
	static constexpr unsigned long long int value = a;
};

template <unsigned int n>
struct QPI;
template <unsigned int n>
struct QPIE {
	static constexpr unsigned long long int num = (
		(2*n + 1) * QPI<n-1>::num
		+ QPI<n-1>::den * static_cast<unsigned long long int>(n % 2 ? -1 : 1)
	);
	static constexpr unsigned long long int den = QPI<n-1>::den * (2*n + 1);
};
template <unsigned int n>
struct QPI {
	static constexpr unsigned long long int num = (
		QPIE<n>::num / GCD<QPIE<n>::num, QPIE<n>::den>::value
	);
	static constexpr unsigned long long int den = (
		QPIE<n>::den / GCD<QPIE<n>::num, QPIE<n>::den>::value
	);
};
template <>
struct QPI<0> {
	static constexpr unsigned long long int num = 1;
	static constexpr unsigned long long int	den = 1;
};

constexpr unsigned int N = 23;
constexpr double COMPI = 4 * static_cast<double>(QPI<N>::num) / QPI<N>::den;


int main() {
	std::printf("4 * %llu / %llu = %f\n", QPI<N>::num, QPI<N>::den, COMPI);
	return 0;
}
