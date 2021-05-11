class Animal {};
class Cat: public Animal {};
class Dog: public Animal {};

int main() {
    Cat kitty{};
    static_cast<Animal &>(kitty) = Dog{};
    return 0;
}
