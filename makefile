CC = gcc
CFLAGS =
LDFLAGS = -lSDL2

SRC = $(wildcard Projeto/src/*.c)
OBJ = $(SRC:.c=.o)
EXEC = jogo

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CC) $(OBJ) $(LDFLAGS) -o $@

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(EXEC)
