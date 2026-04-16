import pygame
import datetime


class MickeyClock:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.center = (width // 2, height // 2)
        
        # BACKGROUND (clock face)
        self.clock_bg = pygame.image.load("clock.png").convert_alpha()
        self.clock_bg = pygame.transform.smoothscale(
            self.clock_bg,
            (width, height)
        )

        # MICKEY IMAGE (center layer)

        self.mickey_img = pygame.image.load("mickey.png").convert_alpha()
        self.mickey_img = pygame.transform.smoothscale(
            self.mickey_img,
            (int(width * 0.4), int(height * 0.4))
        )

        
        # HAND IMAGE
        self.hand_img = pygame.image.load("mickey_hand.png").convert_alpha()

        # separate sizes for better visual control
        self.sec_hand_base = pygame.transform.smoothscale(self.hand_img, (55, 230))
        self.min_hand_base = pygame.transform.smoothscale(self.hand_img, (45, 175))

        # time values
        self.sec_angle = 0
        self.min_angle = 0


    # TIME → ANGLES
    def get_time_angles(self):
        now = datetime.datetime.now()

        seconds = now.second
        minutes = now.minute

        sec_angle = seconds * 6   # 360 / 60
        min_angle = minutes * 6

        return sec_angle, min_angle

    # ROTATION HELP

    def rotate(self, image, angle):
        rotated = pygame.transform.rotate(image, -angle)
        rect = rotated.get_rect(center=self.center)
        return rotated, rect
    # UPDATE LOGIC
    def update(self):
        self.sec_angle, self.min_angle = self.get_time_angles()

    # DRAW EVERYTHING
    
    def draw(self, screen):

        # 1. BACKGROUND CLOCK
        bg_rect = self.clock_bg.get_rect(center=self.center)
        screen.blit(self.clock_bg, bg_rect)

        # 2. MICKEY ON TOP OF CLOCK FACE
        mickey_rect = self.mickey_img.get_rect(center=self.center)
        screen.blit(self.mickey_img, mickey_rect)

        # 3. SECOND HAND
        sec_img, sec_rect = self.rotate(self.sec_hand_base, self.sec_angle)
        screen.blit(sec_img, sec_rect)

        # 4. MINUTE HAND
        min_img, min_rect = self.rotate(self.min_hand_base, self.min_angle)
        screen.blit(min_img, min_rect)