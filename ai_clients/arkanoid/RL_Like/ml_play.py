"""
The template of the main script of the machine learning process
"""
import pygame
from sklearn import neighbors
import os
import sys
import io
import pickle
import csv
import random
# Describe this function...

  
class MLPlay:
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        self.model = None
        DIR = os.path.dirname(__file__)
        #load history data
        if os.path.exists(DIR+'/model.pickle'):
            with open(DIR+'/model.pickle', 'rb') as f:
                self.model = pickle.load(f)
            print('model loaded')
        self.ball_served = False
        self.record = [] #frame,ballX,ballY,dx,dy,platformX
        self.features = []
        self.targets = []
        self.offset = 200
        self.mapSize = int((340-self.offset)/10*40)#int((390-self.offset)/10*40)
        print("=============================")
    def update(self, scene_info, keyboard=None, *args, **kwargs):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        command = None
        if keyboard is None:keyboard = []
        if scene_info["status"] == "GAME_OVER":
            return "RESET"
        elif scene_info["status"] == "GAME_PASS":
            print("\nGAME_PASS!!!")
            raise Exception("exit")
        if not self.ball_served:
            command = "SERVE_TO_RIGHT"
            self.ball_served = True
        else:
            frame = scene_info['frame']
            x,y = scene_info['ball']
            platformX = scene_info['platform'][0]
            brickNum = len(scene_info['hard_bricks']) + len(scene_info['bricks'])
            dx,dy = 0,0
            Map = [0]*self.mapSize#(390-offset)/10*40
            for xb,yb in scene_info['bricks']:
                if yb<self.offset:break
                ii = int((xb/5)+(yb-self.offset)*4)#int((xb/5)+(yb-self.offset)/10*40)
                Map[ii]=9
            for xb,yb in scene_info['hard_bricks']:
                if yb<self.offset:break
                ii = int((xb/5)+(yb-self.offset)*4)
                Map[ii]=10
                
            if frame>0 and len(self.record)>0:
                lastFrame,lastX,lastY,last_dx,last_dy = self.record[-1][0:5]
                dx,dy = last_dx,last_dy
                if frame - lastFrame==1:
                    dx,dy = (x-lastX)*5,(y-lastY)*5
                    #if dx!=last_dx or dy!=last_dy:print('dx,dy=',dx,dy)
            command = "MOVE_LEFT"
            fv = [frame,x,y,dx,dy]
            #print(x,y,dx,dy)
            fv.extend(Map)
            self.record.append(fv)
            
            if self.model!=None and y<395+7:#platform length = 40
                targetX = self.model.predict([fv[1:]])[0]
                if platformX+20 > targetX:  command = "MOVE_LEFT"
                elif platformX+20 <= targetX:command = "MOVE_RIGHT"
                #print(targetX)
                
            if y==395: print('hit at frame ',frame)            
            if pygame.K_LEFT in keyboard:  command = "MOVE_LEFT"
            elif pygame.K_RIGHT in keyboard: command = "MOVE_RIGHT"
            #print(command)
        return command

    def reset(self):
        """
        Reset the status
        """
        
        print("=============================")
        DIR = os.path.dirname(__file__)
        #load history data
        if os.path.exists(DIR+'/targets.pickle'):
            with open(DIR+'/targets.pickle', 'rb') as f:
                self.targets = pickle.load(f)
            with open(DIR+'/features.pickle', 'rb') as f:
                self.features = pickle.load(f)
        
        #save record
        with open(DIR+ '/record' +'.csv', 'w', newline='') as f:
            csv.writer(f, delimiter=',').writerows(self.record)
        #model training
        self.record.reverse()
        ii = None
        for i in range(len(self.record)):
            y=self.record[i][2]
            if y>=(395-7) and y<=(395+7):ii = i;break
        
        targetX = self.record[ii][1] #x
        Temp = []
        i=0
        for fv in self.record[ii:]:
            frame,x,y,dx,dy = fv[0:5]
            self.features.append(fv[1:])
            self.targets.append([targetX])
            temp=[targetX]
            temp.extend(fv)
            Temp.append(temp)
            i+=1
            if y==395 and i>4:break
            
        print("增加feature數量:",i)
        
        self.model = neighbors.KNeighborsRegressor(7, weights='distance')
        self.model.fit(self.features,self.targets)
        #save features <==> targets
        
        with open(DIR+ '/features' +'.csv', 'w', newline='') as f:
            csv.writer(f, delimiter=',').writerows(Temp)
            
        
            
        with open(DIR+ '/features' + '.pickle', 'wb') as f:
            pickle.dump(self.features, f)
        with open(DIR+ '/targets' + '.pickle', 'wb') as f:
            pickle.dump(self.targets, f)
            
        with open(DIR+ '/model' + '.pickle', 'wb') as f:
            pickle.dump(self.model, f)
        #reset parameter
        self.ball_served = False
        self.record = []
        
