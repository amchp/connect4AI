from typing import Optional, Tuple
import pygame
from pygame import display, Surface
from pygame import MOUSEBUTTONDOWN
from pygame import Rect
from choices import ScreensEnum
from constant import (
    OVERLAY_ALPHA,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_SPACING,
    TITLE_FONT_SIZE,
    LABEL_FONT_SIZE,
    TIE_CODE,
    VICTORY_TITLE_Y_OFFSET,
    VICTORY_BUTTONS_TOP_OFFSET,
    BUTTON_BORDER_RADIUS,
    BUTTON_INNER_INFLATE,
    COLOR_WHITE,
    COLOR_BLACK,
)


_last_winner: Optional[int] = None
_last_frame: Optional[Surface] = None


def set_winner(winner: int) -> None:
    global _last_winner
    _last_winner = winner
    surf = display.get_surface()
    if surf is not None:
        global _last_frame
        try:
            _last_frame = surf.copy()
        except Exception:
            _last_frame = None


class VictoryScreen:

    def __init__(self) -> None:
        self.winner = _last_winner
        self._font = None

    def _ensure_font(self):
        if self._font is None:
            pygame.font.init()
            self._font = pygame.font.SysFont(None, LABEL_FONT_SIZE)

    def _layout(self, size: Tuple[int, int]) -> Tuple[Rect, Rect]:
        width, height = size
        btn_w, btn_h = BUTTON_WIDTH, BUTTON_HEIGHT
        spacing = BUTTON_SPACING
        center_x = width // 2
        top_y = (height // 2) + VICTORY_BUTTONS_TOP_OFFSET
        replay_rect = Rect(center_x - btn_w - spacing // 2, top_y, btn_w, btn_h)
        menu_rect = Rect(center_x + spacing // 2, top_y, btn_w, btn_h)
        return replay_rect, menu_rect

    def controls(self) -> Optional[int]:
        surf = display.get_surface()
        if not surf:
            return None
        replay_rect, menu_rect = self._layout(surf.get_size())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if replay_rect.collidepoint(mx, my):
                    return ScreensEnum.Game
                if menu_rect.collidepoint(mx, my):
                    return ScreensEnum.Menu
        return None

    def draw(self) -> None:
        surf = display.get_surface()
        if not surf:
            return

        width, height = surf.get_size()
        if _last_frame is not None:
            surf.blit(_last_frame, (0, 0))
        overlay: Surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)
        overlay.fill((*COLOR_BLACK, OVERLAY_ALPHA))
        surf.blit(overlay, (0, 0))

        msg = ""
        if self.winner in (1, -1):
            player = 1 if self.winner == 1 else 2
            msg = f"Player {player} Wins!"
        elif self.winner == TIE_CODE:
            msg = "It’s a draw!"
        else:
            msg = "Game Over"

        self._ensure_font()
        title_font = pygame.font.SysFont(None, TITLE_FONT_SIZE)
        text = title_font.render(msg, True, (255, 255, 255))
        text_rect = text.get_rect(center=(width // 2, height // 2 + VICTORY_TITLE_Y_OFFSET))
        surf.blit(text, text_rect)

        replay_rect, menu_rect = self._layout((width, height))
        for rect_obj, label in ((replay_rect, "Replay"), (menu_rect, "Back to Menu")):
            pygame.draw.rect(surf, COLOR_WHITE, rect_obj, border_radius=BUTTON_BORDER_RADIUS)
            inner = rect_obj.inflate(-BUTTON_INNER_INFLATE, -BUTTON_INNER_INFLATE)
            pygame.draw.rect(surf, COLOR_BLACK, inner, border_radius=BUTTON_BORDER_RADIUS)
            label_surf = self._font.render(label, True, COLOR_WHITE)
            label_rect = label_surf.get_rect(center=rect_obj.center)
            surf.blit(label_surf, label_rect)

        display.flip()
