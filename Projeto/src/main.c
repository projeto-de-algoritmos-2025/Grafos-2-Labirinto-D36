#include <stdio.h>
#include "game.h"

int main(int argc, char *argv[]) {
    Game game;
    if (init_game(&game, 800, 600, "Game Title") != 0) {
        fprintf(stderr, "Failed to initialize game\n");
        return 1;
    }

    while (game.running) {
        handle_events(&game);
        update_game(&game);
        render_game(&game);
    }

    clean_game(&game);
    return 0;
}