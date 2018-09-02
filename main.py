import pygame
import Clock
import math
import HourPoints as HP

Legs = pygame.image.load("res/GymnastLegs.png")
Torso = pygame.image.load("res/GymnastTorso.png")
MornBG = pygame.image.load("res/MorningClockBg.png")
EvenBG = pygame.image.load("res/EveningClockBg.png")
LegsF = pygame.image.load("res/GymnastLegsFront.png")
TorsoF = pygame.image.load("res/GymnastTorsoFront.png")
TorsoB = pygame.image.load("res/GymnastTorsoBack.png")

pygame.init()
timer = pygame.time.Clock()
Display = pygame.display.set_mode((400, 400))
pygame.display.set_caption("GymnastClock")


running = True

def ClockLoop():
    flip = None
    if (Clock.getMinuteAngle() == Clock.getSecondAngle()):
        flip = True
    elif (Clock.roundOffAngle(Clock.getMinuteAngle() + 180) == Clock.getSecondAngle()):
        flip = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        hour = Clock.getTime().hour
        minute = Clock.getTime().minute
        value = 255 / 12 * (hour + minute/60)
        if value > 255:
            value = math.fabs(255 - (value - 225))
        print(value)
        if(hour > 11):
            hour -= 12

        Legs = pygame.image.load("res/GymnastLegs%d.png" % hour)
        Torso = pygame.image.load("res/GymnastTorso%d.png" % hour)
        LegsF = pygame.image.load("res/GymnastLegsFront%d.png" % hour)
        TorsoF = pygame.image.load("res/GymnastTorsoFront%d.png" % hour)
        TorsoB = pygame.image.load("res/GymnastTorsoBack%d.png" % hour)

        ColorList = HP.List

        Display.fill((value, value, value))
        pygame.draw.circle(Display, ColorList[hour], (200,200), 200, 5)
        HP.makePoints(Display, hour)

        if (Clock.getMinuteAngle() - 20 < Clock.getSecondAngle() < Clock.getMinuteAngle() + 20):
            LegsProfile = LegsF
            TorsoProfile = TorsoB

        elif (Clock.getMinuteAngle() - 20 < Clock.roundOffAngle(Clock.getSecondAngle() + 180) < Clock.getMinuteAngle() + 20):
            LegsProfile = LegsF
            TorsoProfile = TorsoF

        else:
            LegsProfile = Legs
            TorsoProfile = Torso

        if(Clock.getMinuteAngle() == Clock.getSecondAngle()):
            flip = True
        elif(Clock.roundOffAngle(Clock.getMinuteAngle() + 180) == Clock.getSecondAngle()):
            flip = False


        if not flip:
            Legs0 = LegsProfile
            Torso0 = TorsoProfile
        else :
            Legs0 = pygame.transform.flip(LegsProfile, False, True)
            Torso0 = pygame.transform.flip(TorsoProfile, False, True)

        centre = Legs.get_rect().center

        Torso2 = pygame.transform.rotate(Torso0, Clock.getMinuteAngle())
        Legs2 = pygame.transform.rotate(Legs0, Clock.getSecondAngle())

        Legs2.get_rect().center = centre
        Torso2.get_rect().center = centre

        Display.blit(Legs2, (200 - Legs2.get_width()/2, 200 - Legs2.get_height()/2))
        Display.blit(Torso2,(200 - Torso2.get_width()/2, 200 - Torso2.get_height()/2))

        pygame.display.update()
        Display.fill((0, 0, 0))
        timer.tick(10)



ClockLoop()
pygame.quit()
quit()
