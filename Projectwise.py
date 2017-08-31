import os
import pprint
import ArupCADDProjectwise
import ArupCADDProjectwise.PWDatasourceManager as pwman
import ArupCADDProjectwise.PWAddress as PWAddress
#os.environ["PATH"] += os.pathsep + ";C:/Program Files/Bentley/ProjectWise/bin/"

PWIncomingFolder = pwman.GetFolder(0, 'pw:\\\\sinpw101.global.arup.com:AUS_SIN_Projects\\Documents\\221392 C2105 (TSL Pkg D)\\10-00 Construction Stage\\09_Python Testing\\Incoming\\')
PWOutgoingFolder = pwman.GetFolder(0, 'pw:\\\\sinpw101.global.arup.com:AUS_SIN_Projects\\Documents\\221392 C2105 (TSL Pkg D)\\10-00 Construction Stage\\09_Python Testing\\Outgoing\\')


ID = PWIncomingFolder.ProjectId
# print("parent folder ID: " + str(ID))
#
ChildProjects = PWIncomingFolder.AllChildProjects
# print (ChildProjects)

list_name = []
for key in ChildProjects:
    if ChildProjects[key]["parentId"] == ID:
        name = ChildProjects[key]["name"]
        if name[0].isdigit():
            if name[3].isdigit():
                list_name.append(name)


sorted_name = sorted(list_name)
# print (sorted_name)

DAR_num = 1234

codes = sorted_name[-1].split('-')

next_num = int(codes[0]) + 1
#print next_num

def pad(next_num):
    paddings = "0000"
    num_str = str(next_num)
    to_pad = 4 - len(num_str)
    if to_pad <=0:
        return num_str
    return paddings[:to_pad] + num_str
#print pad(next_num)

new_name = ( str (pad(next_num)) + "-" + codes[1] + "-" + str(DAR_num)) + "-"
print new_name

#print ( str ( int(codes[0]) + 1 ) + "-" + codes[1] + "-" + str(x)) + "-"

#pprint.pprint(ChildProjects)
#print(type(ChildProjects))
PWIncomingFolder.CreateSubFolder(new_name, new_name)
PWOutgoingFolder.CreateSubFolder(new_name, new_name)





