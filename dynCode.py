import FreeCAD 
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
