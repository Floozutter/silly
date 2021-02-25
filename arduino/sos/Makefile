ifndef PORT
$(error PORT is not set)
endif

DEVICE     = atmega328p
CLOCK      = 16000000
FUSES      = -U hfuse:w:0xde:m -U lfuse:w:0xff:m -U efuse:w:0x05:m
PROGRAMMER = -c arduino -b 115200 -P $(PORT)
OBJECTS    = main.o

COMPILE = avr-gcc -Wall -Os -DF_CPU=$(CLOCK) -mmcu=$(DEVICE)
AVRDUDE = avrdude $(PROGRAMMER) -p $(DEVICE)

# symbolic targets
all: main.hex

%.o : %.c
	$(COMPILE) -c $< -o $@

%.o : %.S
	$(COMPILE) -x assembler-with-cpp -c $< -o $@
# `-x assembler-with-cpp` should be on by default if case of `.S` is preserved

%.s : %.c
	$(COMPILE) -S $< -o $@

flash: all
	$(AVRDUDE) -U flash:w:main.hex:i

fuse:
	$(AVRDUDE) $(FUSES)

install: flash fuse

load: all
	bootloadHID main.hex
# change above for bootloader

clean:
	rm -f main.hex main.elf $(OBJECTS)

# file targets
main.elf: $(OBJECTS)
	$(COMPILE) -o main.elf $(OBJECTS)

main.hex: main.elf
	rm -f main.hex
	avr-objcopy -j .text -j .data -O ihex main.elf main.hex
	avr-size --format=avr --mcu=$(DEVICE) main.elf

# debugging targets
disasm: main.elf
	avr-objdump -d main.elf

cpp:
	$(COMPILE) -E main.i

# hex file for EEPROM section is necessary to flash if used
