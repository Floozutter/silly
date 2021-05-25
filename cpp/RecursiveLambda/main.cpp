/**
 * https://en.wikipedia.org/wiki/Anonymous_recursion
 * https://stackoverflow.com/a/40873505
 * http://pedromelendez.com/blog/2015/07/16/recursive-lambdas-in-c14/
 */

#include <iostream>

int main() {
    auto const fact = [](unsigned int n) -> unsigned int {
        auto const helper = [](auto const & helper, unsigned int n) -> unsigned int {
            return n ? n * helper(helper, n - 1) : 1;
        };
        return helper(helper, n);
    };
    for (unsigned int n{0}; n < 11; ++n) {
        std::cout << "fact(" << n << ") = " << fact(n) << std::endl;
    }
}
