#!/usr/bin/env python

import vtk

filename = "chair.stl"
 
reader = vtk.vtkSTLReader()
reader.SetFileName(filename)
 
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a rendering window and renderer
ren = vtk.vtkRenderer()
ren_win = vtk.vtkRenderWindow()
ren_win.AddRenderer(ren)
 
# Create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Assign actor to the renderer
ren.AddActor(actor)

# Enable user interface interactor
iren.Initialize()
ren_win.Render()
iren.Start()
