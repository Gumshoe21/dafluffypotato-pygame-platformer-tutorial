import sys

import pygame

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        # 16:50
        # Load image, but not put it on the screen yet
        # Usually want png b/c it's lossless
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')

        # 24:15
        # black box around cloud
        # set_colorkey takes a color in the image and replaces it with transparency
        self.img.set_colorkey((0, 0, 0)) # pure black
        
        self.img_pos = [160, 260]
        # 20:20
        # 22:00
        # if self.movement[0] = True, we're holding down the up key
        # if self.movement[1] = True, we're hodling down the down key

        self.movement = [False, False]
        # 27:15 - Collision detection
        self.collision_area = pygame.Rect(50, 50, 300, 50)
        
    def run(self):
        while True:
            # 23:05 - Cloud is leaving a trail
            # that's because we're blit'ing the cloud onto the screen every frame at a different location
            # we're rendering the cloud on top of the previous render which already has a cloud or clouds rendered, causing the trail
            # so we have to clear the screen each frame so that the cloud gets rendered onto a blank screen each frame
            self.screen.fill((14, 219, 248)) # sky color

            # 29:00
            # A collision rectangle that maps its position to our cloud's position
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            # 30:09 - Collision test
            # if the cloud collides with the collision area
            # basically if, in this frame, these two Rects are overlapping
            if img_r.colliderect(self.collision_area):
                # draw our collision area rect onto the screen with light blue color
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
                # same but with dark blue
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)
            # 31:30 - Rendering order (cloud on top)
            # Layering is based on rendering order
            # Second image will cover first one

            # 22:18
            # Bools can be converted to integers implicitly
            # True = 1
            # False = 0
            # If we hold down up, it'll add up to 1
            # If we hold down, it'll add up to -1
            # Can change the speed by multiplying by a number (5)
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            # 17:25
            # Put the image on the screen at the position we defined (array)
            # 19:03
            # blit is a memory copy - you're copying some section of memory onto another Surface
            # A Surface is an image
            # Can blit any Surface onto another Surface
            self.screen.blit(self.img, self.img_pos)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # 20:30
                # If a key was pressed down
                # 21:13
                # These events are fired when you press or release the keys, they don't necessarily mean that you're holding the key down at that moment
                # So you're not going to be getting these events every single frame while you're holding the key down, so we have to have something to keep track of whether the key is being held down on our end
                # Pygame has its own ways, but this is our way because you can modify it in the future (easier to do so)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                # 21:47
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()