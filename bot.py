from command import Command
import numpy as np
from buttons import Buttons
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import pandas as pd


import keyboard
import csv

class Bot:
 
    def __init__(self):

        # Define the column names and the data row (replace these with actual values in your code)
        self.model = tf.keras.models.load_model("game_model.h5")

        self.column_names = [
            "timer", "fight_result", "has_round_started", "is_round_over", 
            "Player1_player_id", "Player1_health", "Player1_is_player_in_move", "Player1_move_id",
            "Player1_x_coord", "Player1_y_coord", "Player1_is_jumping", "Player1_is_crouching",
            "Player1_player_buttons_A", "Player1_player_buttons_B", "Player1_player_buttons_L",
            "Player1_player_buttons_R", "Player1_player_buttons_Y", "Player1_player_buttons_X",
            "Player1_player_buttons_up", "Player1_player_buttons_down", "Player1_player_buttons_left",
            "Player1_player_buttons_right", "Player1_player_buttons_select", "Player1_player_buttons_start",
            "Player2_player_id", "Player2_health", "Player2_is_player_in_move", "Player2_move_id",
            "Player2_x_coord", "Player2_y_coord", "Player2_is_jumping", "Player2_is_crouching",
            "Player2_player_buttons_A", "Player2_player_buttons_B", "Player2_player_buttons_L",
            "Player2_player_buttons_R", "Player2_player_buttons_Y", "Player2_player_buttons_X",
            "Player2_player_buttons_up", "Player2_player_buttons_down", "Player2_player_buttons_left",
            "Player2_player_buttons_right", "Player2_player_buttons_select", "Player2_player_buttons_start"
        ]
        self.output_columns = [
                "Player1_player_buttons_A",
                "Player1_player_buttons_B",
                "Player1_player_buttons_L",
                "Player1_player_buttons_R",
                "Player1_player_buttons_Y",
                "Player1_player_buttons_X",
                "Player1_player_buttons_up",
                "Player1_player_buttons_down",
                "Player1_player_buttons_left",
                "Player1_player_buttons_right",
                "Player1_player_buttons_select",
                "Player1_player_buttons_start"
            ]

        # Display the DataFrame (optional)
      
        self.my_command = Command() 
        self.buttn= Buttons()
        # for data storage in file
        ( # with open("GameState.csv",mode='w',newline='') as file:
        #     writer=csv.writer(file)
        #     print("IN header")
        #     writer.writerow(['timer',"fight_result","has_round_started","is_round_over",
        #                     'Player1_player_id','Player1_health',"Player1_is_player_in_move","Player1_move_id",
        #                     'Player1_x_coord','Player1_y_coord','Player1_is_jumping','Player1_is_crouching',
        #                     'Player1_player_buttons_A','Player1_player_buttons_B','Player1_player_buttons_L',
        #                     'Player1_player_buttons_R','Player1_player_buttons_Y','Player1_player_buttons_X',
        #                     'Player1_player_buttons_up','Player1_player_buttons_down','Player1_player_buttons_left',
        #                     'Player1_player_buttons_right','Player1_player_buttons_select','Player1_player_buttons_start',
        #                     "player2_player_id","player2_health","Player2_is_player_in_move","Player2_move_id",
        #                     "player2_x_coord","player2_y_coord","player2_is_jumping","player2_is_crouching",
        #                     "player2_player_buttons_A","player2_player_buttons_B","player2_player_buttons_L",
        #                     "player2_player_buttons_R","player2_player_buttons_Y","player2_player_buttons_X",
        #                     "player2_player_buttons_up","player2_player_buttons_down","player2_player_buttons_left",
        #                     "player2_player_buttons_right","player2_player_buttons_select","player2_player_buttons_start"])
       )
    def fight(self,current_game_state,player):
        #rule based
        {#python Videos\gamebot-competition-master\PythonAPI\controller.py 1
        # print("in ")
        # if player=="1":
        #     print("in 1\n\n\n\n\n\n")
        #     #print("1")
        #     #v - < + v - < + B spinning

        #     if( self.exe_code!=0  ):
        #        self.run_command([],current_game_state.player1)
        #     diff=current_game_state.player2.x_coord - current_game_state.player1.x_coord
        #     if (  diff > 60 ) :
        #         toss=np.random.randint(3)
        #         if (toss==0):
        #             #self.run_command([">+^+Y",">+^+Y",">+^+Y","!>+!^+!Y"],current_game_state.player1)
        #             self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player1)
        #         elif ( toss==1 ):
        #             self.run_command([">+^+B",">+^+B","!>+!^+!B"],current_game_state.player1)
        #         else: #fire
        #             self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player1)
        #     elif (  diff < -60 ) :
        #         toss=np.random.randint(3)
        #         if (toss==0):#spinning
        #             #self.run_command(["<+^+Y","<+^+Y","<+^+Y","!<+!^+!Y"],current_game_state.player1)
        #             self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player1)
        #         elif ( toss==1):#
        #             self.run_command(["<+^+B","<+^+B","!<+!^+!B"],current_game_state.player1)
        #         else: #fire
        #             self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player1)
        #     else:
        #         toss=np.random.randint(2)  # anyFightActionIsTrue(current_game_state.player2.player_buttons)
        #         if ( toss>=1 ):
        #             if (diff>0):
        #                 self.run_command(["<","<","!<"],current_game_state.player1)
        #             else:
        #                 self.run_command([">",">","!>"],current_game_state.player1)
        #         else:
        #             self.run_command(["v+R","v+R","v+R","!v+!R"],current_game_state.player1)
        #     self.my_command.player_buttons=self.buttn

        # elif player=="2":
        #     print("in 2\n\n\n\n\n")
        #     if( self.exe_code!=0  ):
        #        self.run_command([],current_game_state.player2)
        #     diff=current_game_state.player1.x_coord - current_game_state.player2.x_coord
        #     if (  diff > 60 ) :
        #         toss=np.random.randint(3)
        #         if (toss==0):
        #             #self.run_command([">+^+Y",">+^+Y",">+^+Y","!>+!^+!Y"],current_game_state.player2)
        #             self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player2)
        #         elif ( toss==1 ):
        #             self.run_command([">+^+B",">+^+B","!>+!^+!B"],current_game_state.player2)
        #         else:
        #             self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player2)
        #     elif ( diff < -60 ) :
        #         toss=np.random.randint(3)
        #         if (toss==0):
        #             #self.run_command(["<+^+Y","<+^+Y","<+^+Y","!<+!^+!Y"],current_game_state.player2)
        #             self.run_command(["<","-","!<","v+<","-","!v+!<","v","-","!v","v+>","-","!v+!>",">+Y","-","!>+!Y"],current_game_state.player2)
        #         elif ( toss==1):
        #             self.run_command(["<+^+B","<+^+B","!<+!^+!B"],current_game_state.player2)
        #         else:
        #             self.run_command([">","-","!>","v+>","-","!v+!>","v","-","!v","v+<","-","!v+!<","<+Y","-","!<+!Y"],current_game_state.player2)
        #     else:
        #         toss=np.random.randint(2)  # anyFightActionIsTrue(current_game_state.player2.player_buttons)
        #         if ( toss>=1 ):
        #             if (diff<0):
        #                 self.run_command(["<","<","!<"],current_game_state.player2)
        #             else:
        #                 self.run_command([">",">","!>"],current_game_state.player2)
        #         else:
        #             self.run_command(["v+R","v+R","v+R","!v+!R"],current_game_state.player2)
        #     self.my_command.player2_buttons=self.buttn
        }
        {# if current_game_state.fight_result=="NOT_OVER":
        #     self.writeGameState(current_game_state)
        # if player=="1":

        #     self.buttn.A = keyboard.is_pressed('a') or keyboard.is_pressed('A')
            
        #     self.buttn.B = keyboard.is_pressed('b') or keyboard.is_pressed('B')
            
        #     self.buttn.L = keyboard.is_pressed('l') or keyboard.is_pressed('L')
            
        #     self.buttn.R = keyboard.is_pressed('r') or keyboard.is_pressed('R')
            
        #     self.buttn.Y = keyboard.is_pressed('y') or keyboard.is_pressed('Y')
            
        #     self.buttn.X = keyboard.is_pressed('x') or keyboard.is_pressed('X')
            
        #     self.buttn.up = keyboard.is_pressed('up')
        #     self.buttn.down = keyboard.is_pressed('down')
        #     self.buttn.left = keyboard.is_pressed('left')
        #     self.buttn.right = keyboard.is_pressed('right')
            
        #     self.buttn.select = keyboard.is_pressed('enter')
        #     self.buttn.start = keyboard.is_pressed('space')
        #     self.my_command.player_buttons=self.buttn
            }
        if player=="1":
            self.buttn.select = keyboard.is_pressed('enter')
            self.buttn.start = keyboard.is_pressed('space')
        data_row = [
            current_game_state.timer, current_game_state.fight_result, current_game_state.has_round_started, current_game_state.is_round_over, 
            current_game_state.player1.player_id, current_game_state.player1.health, current_game_state.player1.is_player_in_move, current_game_state.player1.move_id,
            current_game_state.player1.x_coord, current_game_state.player1.y_coord, current_game_state.player1.is_jumping, current_game_state.player1.is_crouching,
            current_game_state.player1.player_buttons.A, current_game_state.player1.player_buttons.B, current_game_state.player1.player_buttons.L,
            current_game_state.player1.player_buttons.R, current_game_state.player1.player_buttons.Y, current_game_state.player1.player_buttons.X,
            current_game_state.player1.player_buttons.up, current_game_state.player1.player_buttons.down, current_game_state.player1.player_buttons.left,
            current_game_state.player1.player_buttons.right, current_game_state.player1.player_buttons.select, current_game_state.player1.player_buttons.start,
            current_game_state.player2.player_id, current_game_state.player2.health, current_game_state.player2.is_player_in_move, current_game_state.player2.move_id,
            current_game_state.player2.x_coord, current_game_state.player2.y_coord, current_game_state.player2.is_jumping, current_game_state.player2.is_crouching,
            current_game_state.player2.player_buttons.A, current_game_state.player2.player_buttons.B, current_game_state.player2.player_buttons.L,
            current_game_state.player2.player_buttons.R, current_game_state.player2.player_buttons.Y, current_game_state.player2.player_buttons.X,
            current_game_state.player2.player_buttons.up, current_game_state.player2.player_buttons.down, current_game_state.player2.player_buttons.left,
            current_game_state.player2.player_buttons.right, current_game_state.player2.player_buttons.select, current_game_state.player2.player_buttons.start
        ]

        # Create DataFrame
        input_df = pd.DataFrame([data_row], columns=self.column_names)
        prediction = self.predict(input_df)
        self.setbutton(prediction)
        self.my_command.player_buttons=self.buttn
        return self.my_command
    def setbutton(self,prediction):
        if prediction[0][0]==1:
            self.buttn.A = True
        else:
            self.buttn.A = False
        if prediction[0][1]==1:
            self.buttn.B = True
        else:
            self.buttn.B = False
        if prediction[0][2]==1:
            self.buttn.L = True
        else:
            self.buttn.L = False
        if prediction[0][3]==1:
            self.buttn.R = True
        else:
            self.buttn.R = False
        if prediction[0][4]==1:
            self.buttn.Y = True
        else:
            self.buttn.Y = False
        if prediction[0][5]==1:
            self.buttn.X = True
        else:
            self.buttn.X = False
        if prediction[0][6]==1:
            self.buttn.up = True
        else:
            self.buttn.up = False
        if prediction[0][7]==1:
            self.buttn.down = True
        else:
            self.buttn.down = False
        if prediction[0][8]==1:
            self.buttn.left = True
        else:
            self.buttn.left = False
        if prediction[0][9]==1:
            self.buttn.right = True
        else:
            self.buttn.right = False

        
        

    def predict(self,df):
        df = df[~df['fight_result'].isin(['P2 ', 'P1'])]

        df.drop(columns=['fight_result', 'Player1_move_id', 'Player2_move_id'], inplace=True)

        df = df.replace(True, 1)
        df = df.replace(False, 0)

        df.dropna(inplace=True)
            # Feature scaling
        columns = df.columns
        for col in columns:
            if col in ['Player1_player_id', 'Player2_player_id']:
                df[col] = df[col] / 100
                continue
            
            maxVal = df[col].max()
            if maxVal > 1: 
                df[col] = df[col] / maxVal 

            #  output columns 


        # Split data into features 
        X = df.drop(self.output_columns, axis=1)
        y = df[self.output_columns]


        normalizer = StandardScaler()
        x = normalizer.fit_transform(X)
        y_pred = self.model.predict(x)
        print("here")
        threshold = 0.5
        y_pred_binary = (y_pred > threshold).astype(int)
        return y_pred_binary


                

    def writeGameState(self,current_game_state):

        with open("GameState.csv",mode='a',newline='') as file:
            writer=csv.writer(file)
            writer.writerow([current_game_state.timer,current_game_state.fight_result,current_game_state.has_round_started,current_game_state.is_round_over,
                             current_game_state.player1.player_id,current_game_state.player1.health,current_game_state.player1.is_player_in_move,current_game_state.player1.move_id,
                             current_game_state.player1.x_coord,current_game_state.player1.y_coord,current_game_state.player1.is_jumping,current_game_state.player1.is_crouching,
                             current_game_state.player1.player_buttons.A,current_game_state.player1.player_buttons.B,current_game_state.player1.player_buttons.L,
                             current_game_state.player1.player_buttons.R,current_game_state.player1.player_buttons.Y,current_game_state.player1.player_buttons.X,
                             current_game_state.player1.player_buttons.up,current_game_state.player1.player_buttons.down,current_game_state.player1.player_buttons.left,
                             current_game_state.player1.player_buttons.right,current_game_state.player1.player_buttons.select,current_game_state.player1.player_buttons.start,
                             current_game_state.player2.player_id,current_game_state.player2.health,current_game_state.player2.is_player_in_move,current_game_state.player2.move_id,
                             current_game_state.player2.x_coord,current_game_state.player2.y_coord,current_game_state.player2.is_jumping,current_game_state.player2.is_crouching,
                             current_game_state.player2.player_buttons.A,current_game_state.player2.player_buttons.B,current_game_state.player2.player_buttons.L,
                             current_game_state.player2.player_buttons.R,current_game_state.player2.player_buttons.Y,current_game_state.player2.player_buttons.X,
                             current_game_state.player2.player_buttons.up,current_game_state.player2.player_buttons.down,current_game_state.player2.player_buttons.left,
                             current_game_state.player2.player_buttons.right,current_game_state.player2.player_buttons.select,current_game_state.player2.player_buttons.start])


    def run_command( self , com , player   ):

        if self.exe_code-1==len(self.fire_code):
            self.exe_code=0
            self.start_fire=False
            print ("compelete")
            #exit()
            # print ( "left:",player.player_buttons.left )
            # print ( "right:",player.player_buttons.right )
            # print ( "up:",player.player_buttons.up )
            # print ( "down:",player.player_buttons.down )
            # print ( "Y:",player.player_buttons.Y )

        elif len(self.remaining_code)==0 :

            self.fire_code=com
            #self.my_command=Command()
            self.exe_code+=1

            self.remaining_code=self.fire_code[0:]

        else:
            self.exe_code+=1
            if self.remaining_code[0]=="v+<":
                self.buttn.down=True
                self.buttn.left=True
                print("v+<")
            elif self.remaining_code[0]=="!v+!<":
                self.buttn.down=False
                self.buttn.left=False
                print("!v+!<")
            elif self.remaining_code[0]=="v+>":
                self.buttn.down=True
                self.buttn.right=True
                print("v+>")
            elif self.remaining_code[0]=="!v+!>":
                self.buttn.down=False
                self.buttn.right=False
                print("!v+!>")

            elif self.remaining_code[0]==">+Y":
                self.buttn.Y= True #not (player.player_buttons.Y)
                self.buttn.right=True
                print(">+Y")
            elif self.remaining_code[0]=="!>+!Y":
                self.buttn.Y= False #not (player.player_buttons.Y)
                self.buttn.right=False
                print("!>+!Y")

            elif self.remaining_code[0]=="<+Y":
                self.buttn.Y= True #not (player.player_buttons.Y)
                self.buttn.left=True
                print("<+Y")
            elif self.remaining_code[0]=="!<+!Y":
                self.buttn.Y= False #not (player.player_buttons.Y)
                self.buttn.left=False
                print("!<+!Y")

            elif self.remaining_code[0]== ">+^+L" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.L= not (player.player_buttons.L)
                print(">+^+L")
            elif self.remaining_code[0]== "!>+!^+!L" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.L= False #not (player.player_buttons.L)
                print("!>+!^+!L")

            elif self.remaining_code[0]== ">+^+Y" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.Y= not (player.player_buttons.Y)
                print(">+^+Y")
            elif self.remaining_code[0]== "!>+!^+!Y" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.Y= False #not (player.player_buttons.L)
                print("!>+!^+!Y")


            elif self.remaining_code[0]== ">+^+R" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.R= not (player.player_buttons.R)
                print(">+^+R")
            elif self.remaining_code[0]== "!>+!^+!R" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.R= False #ot (player.player_buttons.R)
                print("!>+!^+!R")

            elif self.remaining_code[0]== ">+^+A" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.A= not (player.player_buttons.A)
                print(">+^+A")
            elif self.remaining_code[0]== "!>+!^+!A" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.A= False #not (player.player_buttons.A)
                print("!>+!^+!A")

            elif self.remaining_code[0]== ">+^+B" :
                self.buttn.right=True
                self.buttn.up=True
                self.buttn.B= not (player.player_buttons.B)
                print(">+^+B")
            elif self.remaining_code[0]== "!>+!^+!B" :
                self.buttn.right=False
                self.buttn.up=False
                self.buttn.B= False #not (player.player_buttons.A)
                print("!>+!^+!B")

            elif self.remaining_code[0]== "<+^+L" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.L= not (player.player_buttons.L)
                print("<+^+L")
            elif self.remaining_code[0]== "!<+!^+!L" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.L= False  #not (player.player_buttons.Y)
                print("!<+!^+!L")

            elif self.remaining_code[0]== "<+^+Y" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.Y= not (player.player_buttons.Y)
                print("<+^+Y")
            elif self.remaining_code[0]== "!<+!^+!Y" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.Y= False  #not (player.player_buttons.Y)
                print("!<+!^+!Y")

            elif self.remaining_code[0]== "<+^+R" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.R= not (player.player_buttons.R)
                print("<+^+R")
            elif self.remaining_code[0]== "!<+!^+!R" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.R= False  #not (player.player_buttons.Y)
                print("!<+!^+!R")

            elif self.remaining_code[0]== "<+^+A" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.A= not (player.player_buttons.A)
                print("<+^+A")
            elif self.remaining_code[0]== "!<+!^+!A" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.A= False  #not (player.player_buttons.Y)
                print("!<+!^+!A")

            elif self.remaining_code[0]== "<+^+B" :
                self.buttn.left=True
                self.buttn.up=True
                self.buttn.B= not (player.player_buttons.B)
                print("<+^+B")
            elif self.remaining_code[0]== "!<+!^+!B" :
                self.buttn.left=False
                self.buttn.up=False
                self.buttn.B= False  #not (player.player_buttons.Y)
                print("!<+!^+!B")

            elif self.remaining_code[0]== "v+R" :
                self.buttn.down=True
                self.buttn.R= not (player.player_buttons.R)
                print("v+R")
            elif self.remaining_code[0]== "!v+!R" :
                self.buttn.down=False
                self.buttn.R= False  #not (player.player_buttons.Y)
                print("!v+!R")

            else:
                if self.remaining_code[0] =="v" :
                    self.buttn.down=True
                    print ( "down" )
                elif self.remaining_code[0] =="!v":
                    self.buttn.down=False
                    print ( "Not down" )
                elif self.remaining_code[0] =="<" :
                    print ( "left" )
                    self.buttn.left=True
                elif self.remaining_code[0] =="!<" :
                    print ( "Not left" )
                    self.buttn.left=False
                elif self.remaining_code[0] ==">" :
                    print ( "right" )
                    self.buttn.right=True
                elif self.remaining_code[0] =="!>" :
                    print ( "Not right" )
                    self.buttn.right=False

                elif self.remaining_code[0] =="^" :
                    print ( "up" )
                    self.buttn.up=True
                elif self.remaining_code[0] =="!^" :
                    print ( "Not up" )
                    self.buttn.up=False
            self.remaining_code=self.remaining_code[1:]
        return
