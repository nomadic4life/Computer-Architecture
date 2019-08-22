"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""
    instructions = {
        0b00000000: 'NOP',
        0b00000001: 'HLT',
        0b00010001: 'RET',
        0b00010011: 'IRET',
        0b01000101: 'PUSH',
        0b01000110: 'POP',
        0b01000111: 'PRN',
        0b01001000: 'PRA',
        0b01010000: 'CALL',
        0b01010010: 'INT',
        0b01010100: 'JMP',
        0b01010101: 'JEQ',
        0b01010110: 'JNE',
        0b01010111: 'JGT',
        0b01011000: 'JLT',
        0b01011001: 'JLE',
        0b01011010: 'JGE',
        0b01100101: 'INC',
        0b01100110: 'DEC',
        0b01101001: 'NOT',
        0b10000010: 'LDI',
        0b10000011: 'LD',
        0b10000100: 'ST',
        0b10100000: 'ADD',
        0b10100001: 'SUB',
        0b10100010: 'MUL',
        0b10100011: 'DIV',
        0b10100100: 'MOD',
        0b10100111: 'CMP',
        0b10101000: 'AND',
        0b10101010: 'OR',
        0b10101011: 'XOR',
        0b10101100: 'SHL',
        0b10101101: 'SHR'
    }

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0b00000000] * 256

        self.pc = 0
        self.fl = 0
        self.ir = 0

        self.mar = 0
        self.mdr = 0

        self.halted = False

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        pass
