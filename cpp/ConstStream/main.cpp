#include <iostream>
#include <iomanip>

const long magic{3735928559};
const long cigam{4276869869};

void print_into_buffer(std::ostream const & out) {
    std::ostream share{out.rdbuf()};
    share << std::hex;
    share << "uwu: " << magic << ' ' << cigam << std::endl;
}

int main() {
    std::cout << "owo: " << magic << ' ' << cigam << std::endl;
    print_into_buffer(std::cout);
    std::cout << "owo: " << magic << ' ' << cigam << std::endl;
}
