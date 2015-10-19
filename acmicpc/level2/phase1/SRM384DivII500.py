'''
Created on Jun 7, 2014

@author: sshadmin
'''
class Library():
    def documentAccess(self, records, userGroups, roomRights):
        g=set(userGroups)
        r=set(roomRights)
        counted=set()
        c=0
        for record in records:
            record=record.split(" ")
            if record[2] in g and record[1] in r and record[0] not in counted:
                c+=1
                counted.add(record[0])
        return c