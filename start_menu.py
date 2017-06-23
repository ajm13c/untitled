import pygame

class MenuItem(pygame.font.Font):
        def __init__(self, text, font=None, font_size=30, (pos_x, pos_y)=(0, 0)):
                #sets initial size, color, and position of text on the menu screen
                pygame.font.Font.__init__(self, font, font_size)
                self.text = text
                self.font_size = font_size
                self.font_color = (0, 0, 0)
                self.label = self.render(self.text, 1, self.font_color)
                self.width = self.label.get_rect().width
                self.height = self.label.get_rect().height
                self.pos_x = pos_x
                self.pos_y = pos_y
                self.position = pos_x, pos_y

        def set_position(self, x_position, y_position):
                #changes position of text
                self.position = (x_position, y_position)
                self.pos_x = x_position
                self.pos_y = y_position

        def set_font_color(self, rgb_tuple):
                #changes color of text
                self.font_color = rgb_tuple
                self.label = self.render(self.text, 1, self.font_color)


        def is_mouse_selection(self, (posx, posy)):
                #detects mouse hovering over text
                if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
                        (posy >= self.pos_y and posy <= self.pos_y + self.height):
                        return True
                return False

class start_menu():
        def __init__(self, items, funcs, screen_height, screen_width, font = None, font_size = 30):
                self.bg_color = (255,100,50)
                self.items = []
                self.font = pygame.font.SysFont(font, font_size)
                self.font_color = (0,0,0)
                self.funcs = funcs
                for index, item in enumerate(items):
                        menu_item = MenuItem(item)
                        total_height = len(items) * menu_item.height
                        posx = (screen_width / 2) - (menu_item.width / 2)
                        posy = (screen_height / 2) - (total_height / 2) + ((index * 2) + index * menu_item.height)
                        menu_item.set_position(posx, posy)
                        self.items.append(menu_item)

        def run(self, screen):
                menu = True
                while menu:
                        mpos = pygame.mouse.get_pos()
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        menu = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        for item in self.items:
                                                if item.is_mouse_selection(mpos):
                                                        self.funcs[item.text]()
                        screen.fill(self.bg_color)
                        for item in self.items:
                                if item.is_mouse_selection(pygame.mouse.get_pos()):
                                        item.set_font_color((255,0,200))
                                        item.set_italic(True)
                                else:
                                        item.set_font_color((0,0,0))
                                        item.set_italic(False)
                                screen.blit(item.label, item.position)
                        pygame.display.flip()

