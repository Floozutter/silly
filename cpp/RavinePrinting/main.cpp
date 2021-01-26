// it's called ravine printing because there's a whitespace hole down the middle

#include <iostream>
#include <iomanip>
#include <sstream>

void print_data(double principal_amount, double interest_rate, double times_compounded) {
    int const l{20}, r{10};
    std::ostringstream a; a << '$' << principal_amount;
    std::ostringstream b; b << interest_rate << '%';
    std::ostringstream c; c << times_compounded;
    using std::setw, std::left, std::right, std::endl;
    std::cout
        << left << setw(l) << "Principal Amount:" << right << setw(r) << a.str() << endl
        << left << setw(l) << "Interest Rate:"    << right << setw(r) << b.str() << endl
        << left << setw(l) << "Times Compounded:" << right << setw(r) << c.str() << endl;
}

int main() {
    print_data(420.69, 3.14, 2.72);
    return 0;
}
