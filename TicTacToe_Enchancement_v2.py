# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:43:20 2019

@author: Gokul
"""

import numpy as np
playing = True


class Grid:
    
    
    def __init__(self):
        pass
        #self.gridinput_n = gridinput_n
        
    
    def win(self,gridinput_n,checkboard,playermarker,numofplayers,count):
        
        self.gridinput_n = gridinput_n
        self.checkboard = checkboard
        self.playermarker = playermarker
        self.numofplayers = numofplayers
        self.count = count
        self.diagcount_1 = 0
        
        diag_check_larray = np.diagonal(self.checkboard).copy()
        diag_check_rarray = np.diagonal(np.fliplr(self.checkboard))

        
        #print(diag_check_larray)
        #print(diag_check_rarray)
        
                    
    
        
        
        for i in range(self.gridinput_n):
                 
            for j in range(self.numofplayers):
            
            #print(playermarker[i])
                
                #print(self.checkboard[i,i])
               # print(self.checkboard[i,:]))
                
        
                if (np.all(self.checkboard[i,:] == self.playermarker[j])):
                    print('Player with marker {} Wins Horizontally'.format(self.playermarker[j]))
                    return True
                
                
                elif  (np.all(self.checkboard[:,i] == self.playermarker[j])):
                    print('Player with marker {} Wins Vertically'.format(self.playermarker[j]))
                    return True
                
                
                
                
         #To Check Diagonally     
        
        if (np.all(diag_check_larray[0] != '')):
        
            if (np.all(diag_check_larray[0] ==diag_check_larray[:])):
                
                print('Player with marker {} Wins Diagonally'.format(diag_check_larray[0]))
                return True
            
        if  (np.all(diag_check_rarray[0] != '')):   
            
            if (np.all(diag_check_rarray[0] ==diag_check_rarray[:] )):
                
                print('Player with marker {} Wins Diagonally'.format(diag_check_rarray[0]))
                return True
            
            
        #GAME TIE
        
        if self.count == self.gridinput_n**2:
            
            for i in range(self.gridinput_n):
                     
                for j in range(self.numofplayers):
                
                    
            
                    if not ((np.all(checkboard[i,:] == self.playermarker[j])) and (np.all(checkboard[:,i] == self.playermarker[j])) and (np.all(diag_check_larray[0] ==diag_check_larray[:])) and (np.all(diag_check_rarray[0] ==diag_check_rarray[:]))  ):
                        print('GameTIE')
                        return True
            """        
            if not ((np.all(diag_check_larray[0] ==diag_check_larray[:]))):
                print('Diag GameTIE')
                return True
            
            elif not (np.all(diag_check_rarray[0] ==diag_check_rarray[:]))):
                    print('Diag GameTIE')
                    return True
         """
            
                    
                

                
            
    def checkforavailability(self,checkboard,rowposition,colposition):
        
        self.checkboard = checkboard
        self.rowposition= rowposition
        self.colposition = colposition
        
        if len(checkboard[self.rowposition,self.colposition]) != 0:
            #print(len(checkboard[rowposition,colposition]))
            #print('Sorry, the position is not available \n {}'.format((self.checkboard)))
            return True
            
            
            
class Player:
    
    def __init__(self):
        Grid.__init__(self)
        
        
        
        
    def player_input(self,gridinput_n,numofplayers):
        
        
        global playing
        count =0 
        self.gridinput_n = gridinput_n
        self.numofplayers = numofplayers
        emptyboard= np.chararray((self.gridinput_n,self.gridinput_n),unicode='False',itemsize=2)
        
        playerslist = ['X'+str(i) for i in range(self.numofplayers)]
        #str(playerslist)
        #print(playerslist)
        
        
        
        
        
        while count < self.gridinput_n**2:
                
                
                while playing:
            
                
                    for i in range(numofplayers):
                        #print(i)
                        
                    #print(emptyboard)
                    
                        print('Player {} Turn'.format(i))
                    
                        try:
                            rowposition = int(input('Please enter the Row position with index value between 0 - {}  '.format(self.gridinput_n-1)))
                            colposition = int(input('Please enter the Column position with index value between 0 - {}  '.format(self.gridinput_n-1)))
                            #tuple(position)
                            
            
                        except:
                            print('Sorry , please provide an interger number')
                                                                  
                                            
                        else:
                                           
                            if grid.checkforavailability(emptyboard,rowposition,colposition):
                                print('Sorry, the position is not available \n {}'.format((emptyboard)))
                            
                            else:
                                emptyboard[rowposition,colposition] = playerslist[i]
                                count+=1
                                print(emptyboard)
                                
                                if count >=self.gridinput_n:
                                  if grid.win(gridinput_n,emptyboard,playerslist,numofplayers,count):
                                    playing = False
                                    return False
                                    
                                    
            
            
        
                    
                    
class Game:

    def __init__(self):
        Player.__init__(self)

        
    
    def playerandgrid(self):
        

               c_gridinput_n= int(input('Enter any number greater than 2 for Gridsize of Tic Tac Toe Game!  '))
               numofplayers= int(input("How many number of players you would like to play? Enter number between 2 - {}: ".format(c_gridinput_n)))
    
               if (numofplayers > c_gridinput_n):
        
                    print("Sorry, you cannot play this game with matrix value greater than number of players")
                    numofplayers= int(input('Enter the size of TicTacToe project, Enter number between 1 - {}: '.format(c_gridinput_n+1)))
        
               else:
                    
                    player.player_input(c_gridinput_n,numofplayers)
            
                
    
            
        
        
        

grid = Grid()
player = Player()
game=Game()




while playing:
    
    
        print('Welcome to Tic Tac Toe Game!!! :) Lets play hard ;) !!!')
    
        print(game.playerandgrid())
        
        new_game = input("Would you like to play another game? Enter 'Y' or 'N' ?")
            
        if new_game[0].upper() == 'Y':
            playing = True
            continue
            
        else:
            print("Thanks for Playing!")
            break



    


    