# Makefile
# This Makefile compiles the hello.c program
# into an executable named hello

# Compiler
CC = gcc

# Compiler Flags
CFLAGS = -Wall

# Source files
SRC = main.c helper.c

# Object files
OBJ = $(SRC:.c=.o)

# Executable
PROGRAM = program

# Target file
all: $(PROGRAM)

$(PROGRAM): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

# Phony Target
.PHONY: clean
clean:
	rm -f $(OBJ) $(PROGRAM)