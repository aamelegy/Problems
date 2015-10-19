'''
Created on May 31, 2014

@author: sshadmin
'''
class GymTraining():
    def trainingTime(self, needToTrain, minPulse, maxPulse, trainChange, restChange):
        tr,to,p=0,0,minPulse
        while(tr<needToTrain):
            if p+trainChange<=maxPulse:
                p+=trainChange
                tr+=1
            elif p>minPulse:
                p=max(p-restChange,minPulse)
            else:
                return -1
            to+=1
        return to
                