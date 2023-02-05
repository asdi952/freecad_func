import FreeCAD 
import math
import FreeCADGui


_shapeBinder_count = 0
def _getShapeBinderNum():
    global _shapeBinder_count
    aux = _shapeBinder_count
    _shapeBinder_count += 1
    return aux

def printError( msg):
    FreeCAD.Console.PrintError(msg)
    FreeCAD.Console.PrintError("\n")
    
def create_shapeBinder():
    activeBody = FreeCADGui.ActiveDocument.ActiveView.getActiveObject("pdbody")
    if activeBody == None:
        FreeCAD.Console.PrintError( "Their's no active body\n")
        return

    selection = FreeCADGui.Selection.getSelectionEx()
    if len( selection) == 0:
        FreeCAD.Console.PrintError( "selection is empty\n")
        return

    if len( selection) > 1:
        FreeCAD.Console.PrintError( "selection can only be in one object\n")
        return

    selection = selection[0]
    content = []
    if len( selection.SubElementNames) > 0:
        for elm in selection.SubElementNames:
            content.append((selection.Object, elm))
    else:
        content.append(( selection.Object, ""))

    sBinder = activeBody.newObject( 'PartDesign::ShapeBinder', "sBinder" + str(_getShapeBinderNum()))
    sBinder.Support = content
    sBinder.TraceSupport = True

    FreeCAD.ActiveDocument.recompute()


def create_scketch():
   pass


def cameraToFocus():
    focusPoints = []
    cMass = [ 0, 0, 0]

    def addPoint( point):
        focusPoints.append( point)
        cMass[0] += point[0]
        cMass[1] += point[1]
        cMass[2] += point[2]

    selObj = FreeCADGui.Selection.getSelectionEx()
    for obj in selObj:
        if len( obj.SubObjects) == 0:
            addPoint( obj.Object.Shape.CenterOfMass)
        else:
            for subObj in obj.SubObjects:
                addPoint( subObj.CenterOfMass)
            
    cMass[0] /= len( focusPoints)
    cMass[1] /= len( focusPoints)
    cMass[2] /= len( focusPoints)
    maxDist = 0
    for point in focusPoints:
        x = point[0] - cMass[0]
        y = point[1] - cMass[1]
        z = point[2] - cMass[2]
        dist = math.sqrt( x*x + y*y + z*z)
        if dist > maxDist: 
            maxDist = dist

    cam = FreeCADGui.ActiveDocument.ActiveView.getCameraNode()
    cam.position.setValue(cMass[0], cMass[1], cMass[2])
    cam.position.setValue(cMass[0], cMass[1], cMass[2])

def cameraToFaceNormal():
    sel = FreeCADGui.Selection.getSelectionEx().SubObjects
    if len(sel) == 0:
        printError("No face")

    FreeCADGui.ActiveDocument.ActiveView.getCameraNode()
    cam.position.setValue()
    cam.orientation.setValue()

