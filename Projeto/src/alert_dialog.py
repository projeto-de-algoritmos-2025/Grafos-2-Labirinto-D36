import pygame
from settings import *

class AlertDialog:
    def __init__(self, screen, message, button_msg, width, height):
        self.screen = screen
        self.message = message
        self.button_msg = button_msg
        self.active = False

        self.width, self.height = width, height
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = (SCREEN_HEIGHT - self.height) // 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.Font(None, 24)

    def update_message(self, new_message):
        self.message = new_message
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.active:
            if self.button_rect.collidepoint(event.pos):
                self.active = False
                return True
        return False

    def draw(self):
        if self.active:
            shadow_rect = self.rect.copy()
            shadow_rect.x += 3
            shadow_rect.y += 3
            pygame.draw.rect(self.screen, WHITE_GRAY, shadow_rect)
            
            pygame.draw.rect(self.screen, (240, 240, 240), self.rect)
            pygame.draw.rect(self.screen, BLACK, self.rect, 2)

            if isinstance(self.message, list):
                line_height = self.font.get_height()
                y_offset = self.y + 20
                for line in self.message:
                    text_render = self.font.render(line, True, BLACK)
                    text_rect = text_render.get_rect(centerx=self.x + self.width / 2, y=y_offset)
                    self.screen.blit(text_render, text_rect)
                    y_offset += line_height + 5
            else:
                text_render = self.font.render(self.message, True, BLACK)
                text_rect = text_render.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
                self.screen.blit(text_render, text_rect)
                
            button_text_render = self.font.render(self.button_msg, True, WHITE)
            self.button_rect = pygame.Rect(0, 0, 120, 50)
            self.button_rect.center = (self.x + self.width // 2, self.y + self.height - 40)
            
            pygame.draw.rect(self.screen, BLUE, self.button_rect)
            pygame.draw.rect(self.screen, BLACK, self.button_rect, 2)
            self.screen.blit(button_text_render, button_text_render.get_rect(center=self.button_rect.center))