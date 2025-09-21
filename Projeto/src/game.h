#ifndef GAME_H
#define GAME_H

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <SDL2/SDL.h>

typedef struct {
    SDL_Window* window;
    SDL_Renderer* renderer;
    Player player;
    int running;
} Game;

int init_game(Game* game, int width, int height, const char* title);
void handle_events(Game* game);
void update_game(Game* game);
void render_game(Game* game);
void clean_game(Game* game);


#endif // GAME_H