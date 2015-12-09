__author__ = 'Chetan'

from opensim import *

print "Hello Model"

#m = opensim.model('C:\OpenSim 3.3\Models\Gait2354_Simbody\gait2354_simbody.osim')
myModel = opensim.Model('C:\OpenSim 3.3\Models\Gait2354_Simbody\gait2354_simbody.osim')


print myModel.getCoordinateSet().getSize()
cordSet = myModel.getCoordinateSet()
print cordSet.get(0).getName()
print cordSet.get(0).getDefaultValue()
numberJoints= myModel.getJointSet().getSize()
print numberJoints

# inverse kinematics needed for setting coordinate values of model
# this is an experiment
invDynamic = opensim.InverseDynamicsTool()
coordSet = myModel.getCoordinateSet()


for i in range(coordSet.getSize()):
    currentCoord = coordSet.get(i)
    invDynamic.setCoordinateValue(currentCoord, currentCoord.getDefaultValue())