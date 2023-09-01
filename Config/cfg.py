import os

#Frame per second
FPS = 40

#Size of the screen
SCREENSIZE = (640, 640)

#Skier images of the game
SKIER_IMAGE_PATH = [os.path.join(os.getcwd(), "resources/images/skier_forward.png"),
                    os.path.join(os.getcwd(), "resources/images/skier_right1.png"),
                    os.path.join(os.getcwd(), "resources/images/skier_right2.png"),
                    os.path.join(os.getcwd(), "resources/images/skier_left1.png"),
                    os.path.join(os.getcwd(), "resources/images/skier_left2.png"),
                    os.path.join(os.getcwd(), "resources/images/skier_fall.png")]

#Obstacle images of the game
OBSTACLE_PATH = {'tree': os.path.join(os.getcwd(), "resources/images/tree.png"),
                 'flag': os.path.join(os.getcwd(), "resources/images/flag.png")}

#Music of the game
BGM_PATH = os.path.join(os.getcwd(), "resources/music/bgm.mp3")

#Font for the game
FONT_PATH = os.path.join(os.getcwd(), "resources/font/FZSTK.TTF")