from pyfirmata import Arduino, SERVO, util, PWM
from time import sleep

class momvementController:
    def __init__(self):
        self.port_1 = 'COM3'
        self.port_2 = 'COM4'
        self.MetronomeAct=False
        self.LedTime=0.15
        self.Movementtime=0.85
        self.pinI_b1 = 9
        self.pinB_b1 = 10
        self.pinC_b1 = 11
        self.pinA_b1 = 12
        self.pinAb_b2 = 9
        self.pinD_b2 = 10
        self.pinS_b2 = 11
        self.pinM_b2 = 8
        #Izquierda/Base/Centro/Arriba
        self.board_1 = Arduino(self.port_1)
        #Side/Abajo/Derecha
        self.board_2 = Arduino(self.port_2)

        self.board_1.digital[self.pinI_b1].mode = SERVO
        self.board_1.digital[self.pinB_b1].mode = SERVO
        self.board_1.digital[self.pinC_b1].mode = SERVO
        self.board_1.digital[self.pinA_b1].mode = SERVO
        self.board_2.digital[self.pinAb_b2].mode = SERVO
        self.board_2.digital[self.pinD_b2].mode = SERVO
        self.board_2.digital[self.pinS_b2].mode = SERVO


        self.Initialposition()

    def makesound(self):
        if (self.MetronomeAct):
            self.board_2.digital[self.pinM_b2].write(1)
        sleep(self.LedTime)
        self.board_2.digital[self.pinM_b2].write(0)

    def movement_analisis(self,movements):
        for letter in movements:
            if letter=="A":
                self.rotateservo(self.pinS_b2,115,self.board_2)
            elif letter=="B":
                self.rotateservo(self.pinS_b2,65,self.board_2)
            elif letter=="D":
                self.rotateservo(self.pinB_b1, 115, self.board_1)
            elif letter=="I":
                self.rotateservo(self.pinB_b1, 65, self.board_1)
            elif letter=="G":
                self.rotateservo(self.pinC_b1, 60, self.board_1)
            elif letter=="GA":
                self.rotateservo(self.pinA_b1, 60, self.board_1)
            elif letter=="GB":
                self.rotateservo(self.pinAb_b2, 120, self.board_2)
            elif letter=="GD":
                self.rotateservo(self.pinD_b2, 70, self.board_2)
            elif letter=="GI":
                self.rotateservo(self.pinI_b1, 110, self.board_1)
            elif letter=="GDI":
                self.rotate_multipleservos(self.pinI_b1, self.pinD_b2, 110, 70, self.board_1, self.board_2)
            elif letter=="GAB":
                self.rotate_multipleservos(self.pinA_b1, self.pinAb_b2, 60, 120, self.board_1, self.board_2)
            elif letter[0] == "V":
                self.vibrato(movement.pinB_b1, int(letter[1:]), movement.board_1)
            elif letter[0] == "M":
                self.ActivateMetronome(letter[1])
                self.calculatetempo(float(letter[2:]))


    def rotate_multipleservos (self, pin1, pin2, angle1, angle2, board1, board2):
        self.makesound()
        board1.digital[pin1].write(angle1)
        board2.digital[pin2].write(angle2)
        sleep(self.Movementtime)
        self.makesound()
        board1.digital[pin1].write(90)
        board2.digital[pin2].write(90)
        sleep(self.Movementtime)

    def rotateservo(self, pin, angle, board):
        self.makesound()
        board.digital[pin].write(angle)
        sleep(self.Movementtime)
        self.makesound()
        board.digital[pin].write(90)
        sleep(self.Movementtime)


    def vibrato (self, pin, i, board):
        while i != 0:
            board.digital[pin].write(100)
            sleep(0.25)
            board.digital[pin].write(90)
            sleep(0.25)
            i-=1

    def Initialposition(self):
        self.board_1.digital[self.pinB_b1].write(90)
        sleep(0.5)
        self.board_2.digital[self.pinD_b2].write(90)
        sleep(0.5)
        self.board_1.digital[self.pinI_b1].write(90)
        sleep(0.5)
        self.board_1.digital[self.pinC_b1].write(90)
        sleep(0.5)
        self.board_1.digital[self.pinA_b1].write(90)
        sleep(0.5)
        self.board_2.digital[self.pinAb_b2].write(90)
        sleep(0.5)
        self.board_2.digital[self.pinS_b2].write(90)
        sleep(0.5)

    def ActivateMetronome(self,Letter):
        if Letter=="A":
            self.MetronomeAct=True
        elif Letter=="D":
            self.MetronomeAct=False
        else:
            print("Error Letra metronomo")
    def calculatetempo(self,tempo):
        if(tempo<0.4):
            print("Error")
        else:
            self.Movementtime=tempo-0.15


#movement = momvementController()

#vibrato_number = input("input vibrato: ")
#movement.vibrato(movement.pinB_b1, int(vibrato_number), movement.board_1)
'''while(True):
    #angle = input("Angle: ")
    #movement.rotateservo(movement.pinD_b2, int(angle), movement.board_2)
    self.pinI_b1 = 9
    self.pinB_b1 = 10
    self.pinC_b1 = 11
    self.pinA_b1 = 12
    self.pinAb_b2 = 9
    self.pinD_b2 = 10
    self.pinS_b2 = 11
    #movement_tempo = input("input tempo: ")
    #movement.calculatetempo(float(movement_tempo))
    movement_letter = input("input movements: ")
    movement.movement_analisis(movement_letter.split(" "))'''
#base_angle = input("input Base: ")
#movement.rotateservo(movement.pinB, base_angle, movement.board_1)
#side_angle = input("input Side: ")
#movement.rotateservo(movement.pinS, side_angle, movement.board_2)
#if isinstance(int(base_angle), int) and isinstance(int(side_angle), int):
