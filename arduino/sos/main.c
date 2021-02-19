#include <avr/io.h>
#include <util/delay.h>

const int DIT_LENGTH = 200;

void wait(unsigned units) {
    for (int i = 0; i < units; ++i) {
        _delay_ms(DIT_LENGTH);
    }
}

void on(unsigned units) {
    PORTB |= (1 << PB5);
    wait(units);
}
void off(unsigned units) {
    PORTB &= ~(1 << PB5);
    wait(units);
}

int main(void) {
    DDRB |= (1 << DDB5);
    while (1) {
        on(1); off(1); on(1); off(1); on(1); off(1);  // S
        on(3); off(1); on(3); off(1); on(3); off(1);  // O
        on(1); off(1); on(1); off(1); on(1); off(1);  // S
        off(6);
    }
    return 0;
}
