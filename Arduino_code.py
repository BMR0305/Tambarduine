from pyfirmata import Arduino, SERVO, util
from time import sleep

class momvementController:
    def __init__(self):
        self.port_1 = 'COM3'
        self.port_2 = 'COM4'
        self.MetronomeAct=False
        self.LedTime=0.15
        self.Movementtime=0.85
        self.pinB = 9
        self.pinS = 10
        #Vertical
        self.board_1 = Arduino(self.port_1)
        #Abanico
        self.board_2 = Arduino(self.port_2)

        self.board_1.digital[self.pinB].mode = SERVO
        self.board_2.digital[self.pinS].mode = SERVO

    def AbaVert(self,letter):
        if letter=="A":
            self.rotateservo(self.pinS,135,self.board_2)
        elif letter=="B":
            self.rotateservo(self.pinS,45,self.board_2)
        elif letter=="D":
            self.rotateservo(self.pinB, 135, self.board_1)
        elif letter=="I":
            self.rotateservo(self.pinB, 45, self.board_1)
        else:
            print("ERROR LETRA Movimimiento")

    def rotateservo(self, pin, angle, board):
        board.digital[pin].write(angle)
        sleep(self.Movementtime)
        board.digital[pin].write(90)
        sleep(self.Movementtime)

    def vibrato (self, pin, i, board):
        while i != 0:
            board.digital[pin].write(110)
            sleep(0.25)
            board.digital[pin].write(90)
            sleep(0.25)
            i-=1
    def Initialposition(self):
        self.board_1.digital[self.pinB].write(90)
        sleep(0.5)
        self.board_2.digital[self.pinS].write(90)
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


movement = momvementController()
movement.Initialposition()
vibrato_number = input("input vibrato: ")
movement.vibrato(movement.pinB, int(vibrato_number), movement.board_1)
while(True):

    movement_tempo = input("input tempo: ")
    movement.calculatetempo(float(movement_tempo))
    movement_letter = input("input letra: ")
    movement.AbaVert(movement_letter)
#base_angle = input("input Base: ")
#movement.rotateservo(movement.pinB, base_angle, movement.board_1)
#side_angle = input("input Side: ")
#movement.rotateservo(movement.pinS, side_angle, movement.board_2)
#if isinstance(int(base_angle), int) and isinstance(int(side_angle), int):
