#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Mon May  8 16:02:58 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""
## Mental Rotation Task
#LIV WROTE AND DEBUGGED, 16 hours total

# --- Import packages ---
from matplotlib import pyplot as plt
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
import csv


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'rotation_experiment'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/oliviacohen/Desktop/rotation_experiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "introduction" ---
text_4 = visual.TextStim(win=win, name='text_4',
    text='Welcome! You are about to begin the mental rotation task. Three shapes will appear on your screen when we begin. The goal is to match the shape at the top of the screen with the rotated version of itself, NOT the mirrored and rotated version. Good luck, and click to start!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "poly1" ---
text_5 = visual.TextStim(win=win, name='text_5',
    text='Wrong!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
background = visual.Rect(
    win=win, name='background',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-1.0, interpolate=True)
text_6 = visual.TextStim(win=win, name='text_6',
    text='Correct!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices=[[-0.1,-0.1],[0,-0.05],[0,0.25]],
    size=(0.5, 0.5),
    ori=0.0, pos=(0.0, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices=[[-0.1,-0.1],[0,-0.05],[0,0.25]],
    size=(0.5, 0.5),
    ori=120.0, pos=(-0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices=[[0.1,-0.1],[0,-0.05],[0,0.25]],
    size=(0.5, 0.5),
    ori=30.0, pos=(0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "poly2" ---
text_7 = visual.TextStim(win=win, name='text_7',
    text='Wrong!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
background_3 = visual.Rect(
    win=win, name='background_3',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-1.0, interpolate=True)
text_8 = visual.TextStim(win=win, name='text_8',
    text='Correct!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices=[[0,0],[-0.1,0.15],[0,-0.15],[0.25,0.25]],
    size=(0.5, 0.5),
    ori=0.0, pos=(0.0, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
polygon_5 = visual.ShapeStim(
    win=win, name='polygon_5', vertices=[[0,0],[0.1,0.15],[0,-0.15],[-0.25,0.25]],
    size=(0.5, 0.5),
    ori=90.0, pos=(-0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
polygon_6 = visual.ShapeStim(
    win=win, name='polygon_6', vertices=[[0,0],[-0.1,0.15],[0,-0.15],[0.25,0.25]],
    size=(0.5, 0.5),
    ori=160.0, pos=(0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "poly3" ---
text_9 = visual.TextStim(win=win, name='text_9',
    text='Wrong!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
background_2 = visual.Rect(
    win=win, name='background_2',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-1.0, interpolate=True)
text_10 = visual.TextStim(win=win, name='text_10',
    text='Correct!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
polygon_7 = visual.ShapeStim(
    win=win, name='polygon_7', vertices=[[-0.25,0],[-0.25,0.05],[0.1,0.05],[0.1,0.25],[0.15,0.25],[0.15,0.05],[0.25,0.05],[0.25,0],[0.05,0]],
    size=(0.5, 0.5),
    ori=0.0, pos=(0.0, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
polygon_8 = visual.ShapeStim(
    win=win, name='polygon_8', vertices=[[-0.25,0],[-0.25,0.05],[0.1,0.05],[0.1,0.25],[0.15,0.25],[0.15,0.05],[0.25,0.05],[0.25,0],[0.05,0]],
    size=(0.5, 0.5),
    ori=34.0, pos=(-0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
polygon_9 = visual.ShapeStim(
    win=win, name='polygon_9', vertices=[[0.25,0],[0.25,0.05],[-0.1,0.05],[-0.1,0.25],[-0.15,0.25],[-0.15,0.05],[-0.25,0.05],[-0.25,0],[-0.05,0]],
    size=(0.5, 0.5),
    ori=142.0, pos=(0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "poly4" ---
text_11 = visual.TextStim(win=win, name='text_11',
    text='Wrong!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
background_4 = visual.Rect(
    win=win, name='background_4',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-1.0, interpolate=True)
text_12 = visual.TextStim(win=win, name='text_12',
    text='Correct!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
polygon_10 = visual.ShapeStim(
    win=win, name='polygon_10', vertices=[[0,-0.2],[0,0.25],[0.25,0.25],[0.25,0.2],[0.05,0.2],[0.05,0.1],[0.25,0.1],[0.25,0.05],[0.05,0.05],[0.05,-0.2]],
    size=(0.5, 0.5),
    ori=0.0, pos=(0.0, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
polygon_11 = visual.ShapeStim(
    win=win, name='polygon_11', vertices=[[0,-0.2],[0,0.25],[0.25,0.25],[0.25,0.2],[0.05,0.2],[0.05,0.1],[0.25,0.1],[0.25,0.05],[0.05,0.05],[0.05,-0.2]],
    size=(0.5, 0.5),
    ori=40.0, pos=(-0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
polygon_12 = visual.ShapeStim(
    win=win, name='polygon_12', vertices=[[0,-0.2],[0,0.25],[-0.25,0.25],[-0.25,0.2],[-0.05,0.2],[-0.05,0.1],[-0.25,0.1],[-0.25,0.05],[-0.05,0.05],[-0.05,-0.2]],
    size=(0.5, 0.5),
    ori=142.0, pos=(0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "poly5" ---
text_13 = visual.TextStim(win=win, name='text_13',
    text='Wrong!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
background_5 = visual.Rect(
    win=win, name='background_5',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-1.0, interpolate=True)
text_14 = visual.TextStim(win=win, name='text_14',
    text='Correct!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
polygon_13 = visual.ShapeStim(
    win=win, name='polygon_13', vertices=[[-0.25,0],[-0.1,0.1],[0,0.05],[0.1,0.25],[0.25,0]],
    size=(0.5, 0.5),
    ori=0.0, pos=(0.0, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
polygon_14 = visual.ShapeStim(
    win=win, name='polygon_14', vertices=[[-0.25,0],[-0.1,0.1],[0,0.05],[0.1,0.25],[0.25,0]],
    size=(0.5, 0.5),
    ori=47.0, pos=(0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
polygon_15 = visual.ShapeStim(
    win=win, name='polygon_15', vertices=[[0.25,0],[0.1,0.1],[0,0.05],[-0.1,0.25],[-0.25,0]],
    size=(0.5, 0.5),
    ori=19.0, pos=(-0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "poly6" ---
text_15 = visual.TextStim(win=win, name='text_15',
    text='Wrong!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
background_6 = visual.Rect(
    win=win, name='background_6',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-1.0, interpolate=True)
text_16 = visual.TextStim(win=win, name='text_16',
    text='Correct!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
polygon_16 = visual.ShapeStim(
    win=win, name='polygon_16', vertices=[[-0.05,-0.05],[-0.05,0.25],[0,0.25],[0,0],[0.1,0],[0.1,-0.05]],
    size=(0.5, 0.5),
    ori=0.0, pos=(0.0, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
polygon_17 = visual.ShapeStim(
    win=win, name='polygon_17', vertices=[[-0.05,-0.05],[-0.05,0.25],[0,0.25],[0,0],[0.1,0],[0.1,-0.05]],
    size=(0.5, 0.5),
    ori=90.0, pos=(-0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
polygon_18 = visual.ShapeStim(
    win=win, name='polygon_18', vertices=[[0.05,-0.05],[0.05,0.25],[0,0.25],[0,0],[-0.1,0],[-0.1,-0.05]],
    size=(0.5, 0.5),
    ori=160.0, pos=(0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "poly7" ---
text_17 = visual.TextStim(win=win, name='text_17',
    text='Wrong!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
background_7 = visual.Rect(
    win=win, name='background_7',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-1.0, interpolate=True)
text_18 = visual.TextStim(win=win, name='text_18',
    text='Correct!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
polygon_19 = visual.ShapeStim(
    win=win, name='polygon_19', vertices=[[-0.2,-0.2],[0.2,-0.2],[0.2,0.25],[0.1,0.25],[0.1,0.2],[-0.2,0.2]],
    size=(0.5, 0.5),
    ori=0.0, pos=(0.0, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
polygon_20 = visual.ShapeStim(
    win=win, name='polygon_20', vertices=[[0.2,-0.2],[-0.2,-0.2],[-0.2,0.25],[-0.1,0.25],[-0.1,0.2],[0.2,0.2]],
    size=(0.5, 0.5),
    ori=171.0, pos=(0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
polygon_21 = visual.ShapeStim(
    win=win, name='polygon_21', vertices=[[-0.2,-0.2],[0.2,-0.2],[0.2,0.25],[0.1,0.25],[0.1,0.2],[-0.2,0.2]],
    size=(0.5, 0.5),
    ori=52.0, pos=(-0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "poly8" ---
text_19 = visual.TextStim(win=win, name='text_19',
    text='Wrong!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
background_8 = visual.Rect(
    win=win, name='background_8',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-1.0, interpolate=True)
text_20 = visual.TextStim(win=win, name='text_20',
    text='Correct!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
polygon_22 = visual.ShapeStim(
    win=win, name='polygon_22', vertices=[[0,-0.2],[0,0.25],[0.25,0.25],[0.25,0.2],[0.05,0.2],[0.05,0.1],[0.25,0.1],[0.25,0.05],[0.05,0.05],[0.05,-0.15],[0.25,-0.15],[0.25,-0.2]],
    size=(0.5, 0.5),
    ori=0.0, pos=(0.0, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
polygon_23 = visual.ShapeStim(
    win=win, name='polygon_23', vertices=[[0,-0.2],[0,0.25],[-0.25,0.25],[-0.25,0.2],[-0.05,0.2],[-0.05,0.1],[-0.25,0.1],[-0.25,0.05],[-0.05,0.05],[-0.05,-0.15],[-0.25,-0.15],[-0.25,-0.2]],
    size=(0.5, 0.5),
    ori=58.0, pos=(-0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
polygon_24 = visual.ShapeStim(
    win=win, name='polygon_24', vertices=[[0,-0.2],[0,0.25],[0.25,0.25],[0.25,0.2],[0.05,0.2],[0.05,0.1],[0.25,0.1],[0.25,0.05],[0.05,0.05],[0.05,-0.15],[0.25,-0.15],[0.25,-0.2]],
    size=(0.5, 0.5),
    ori=9.0, pos=(0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "poly9" ---
text_21 = visual.TextStim(win=win, name='text_21',
    text='Wrong!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
background_9 = visual.Rect(
    win=win, name='background_9',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-1.0, interpolate=True)
text_22 = visual.TextStim(win=win, name='text_22',
    text='Correct!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
polygon_25 = visual.ShapeStim(
    win=win, name='polygon_25', vertices=[[-0.1,-0.1],[0,-0.05],[0,0.25],[0.25,-0.25]],
    size=(0.5, 0.5),
    ori=0.0, pos=(0.0, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
polygon_26 = visual.ShapeStim(
    win=win, name='polygon_26', vertices=[[-0.1,-0.1],[0,-0.05],[0,0.25],[0.25,-0.25]],
    size=(0.5, 0.5),
    ori=130.0, pos=(-0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
polygon_27 = visual.ShapeStim(
    win=win, name='polygon_27', vertices=[[0.1,-0.1],[0,-0.05],[0,0.25],[-0.25,-0.25]],
    size=(0.5, 0.5),
    ori=30.0, pos=(0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "poly10" ---
text_23 = visual.TextStim(win=win, name='text_23',
    text='Wrong!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
background_10 = visual.Rect(
    win=win, name='background_10',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0039, 0.0039, 0.0039],
    opacity=None, depth=-1.0, interpolate=True)
text_24 = visual.TextStim(win=win, name='text_24',
    text='Correct!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
polygon_28 = visual.ShapeStim(
    win=win, name='polygon_28', vertices=[[0,0],[0,-0.15],[0.25,0.25],[-0.1,0.2],[0.15,0]],
    size=(0.5, 0.5),
    ori=0.0, pos=(0.0, 0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-3.0, interpolate=True)
polygon_29 = visual.ShapeStim(
    win=win, name='polygon_29', vertices=[[0,0],[0,-0.15],[-0.25,0.25],[0.1,0.2],[-0.15,0]],
    size=(0.5, 0.5),
    ori=90.0, pos=(-0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-4.0, interpolate=True)
polygon_30 = visual.ShapeStim(
    win=win, name='polygon_30', vertices=[[0,0],[0,-0.15],[0.25,0.25],[-0.1,0.2],[0.15,0]],
    size=(0.5, 0.5),
    ori=150.0, pos=(0.5, -0.25), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[1.0000, -1.0000, -1.0000],
    opacity=None, depth=-5.0, interpolate=True)

# --- Initialize components for Routine "trial" ---
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you for playing! Click anywhere to close and generate your results.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "introduction" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
introductionComponents = [text_4]
for thisComponent in introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "introduction" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        if bool(mouse.getPressed()[0]):
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.stopped')
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "introduction" ---
for thisComponent in introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "poly1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    poly1Components = [text_5, background, text_6, polygon, polygon_2, polygon_3]
    for thisComponent in poly1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "poly1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and mouse.isPressedIn(polygon_3) or mouse.isPressedIn(polygon_2):
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.stopped')
                text_5.setAutoDraw(False)
        
        # *background* updates
        if background.status == NOT_STARTED and mouse.isPressedIn(polygon_2):
            # keep track of start time/frame for later
            background.frameNStart = frameN  # exact frame index
            background.tStart = t  # local t and not account for scr refresh
            background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background.started')
            background.setAutoDraw(True)
        if background.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                background.tStop = t  # not accounting for scr refresh
                background.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background.stopped')
                background.setAutoDraw(False)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and mouse.isPressedIn(polygon_2):
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.stopped')
                text_6.setAutoDraw(False)
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon.started')
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            if bool(mouse.isPressedIn(polygon_2)):
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.stopped')
                polygon.setAutoDraw(False)
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_2.started')
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            if bool(mouse.isPressedIn(polygon_2)):
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_2.stopped')
                polygon_2.setAutoDraw(False)
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_3.started')
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            if bool(mouse.isPressedIn(polygon_2)):
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_3.stopped')
                polygon_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in poly1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "poly1" ---
    for thisComponent in poly1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "poly1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "poly2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    poly2Components = [text_7, background_3, text_8, polygon_4, polygon_5, polygon_6]
    for thisComponent in poly2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "poly2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and mouse.isPressedIn(polygon_6) or mouse.isPressedIn(polygon_5):
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_7.stopped')
                text_7.setAutoDraw(False)
        
        # *background_3* updates
        if background_3.status == NOT_STARTED and mouse.isPressedIn(polygon_6):
            # keep track of start time/frame for later
            background_3.frameNStart = frameN  # exact frame index
            background_3.tStart = t  # local t and not account for scr refresh
            background_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_3.started')
            background_3.setAutoDraw(True)
        if background_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                background_3.tStop = t  # not accounting for scr refresh
                background_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_3.stopped')
                background_3.setAutoDraw(False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and mouse.isPressedIn(polygon_6):
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_8.started')
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.stopped')
                text_8.setAutoDraw(False)
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_4.started')
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            if bool(mouse.isPressedIn(polygon_6)):
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_4.stopped')
                polygon_4.setAutoDraw(False)
        
        # *polygon_5* updates
        if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_5.frameNStart = frameN  # exact frame index
            polygon_5.tStart = t  # local t and not account for scr refresh
            polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_5.started')
            polygon_5.setAutoDraw(True)
        if polygon_5.status == STARTED:
            if bool(mouse.isPressedIn(polygon_6)):
                # keep track of stop time/frame for later
                polygon_5.tStop = t  # not accounting for scr refresh
                polygon_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_5.stopped')
                polygon_5.setAutoDraw(False)
        
        # *polygon_6* updates
        if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_6.frameNStart = frameN  # exact frame index
            polygon_6.tStart = t  # local t and not account for scr refresh
            polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_6.started')
            polygon_6.setAutoDraw(True)
        if polygon_6.status == STARTED:
            if bool(mouse.isPressedIn(polygon_6)):
                # keep track of stop time/frame for later
                polygon_6.tStop = t  # not accounting for scr refresh
                polygon_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_6.stopped')
                polygon_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in poly2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "poly2" ---
    for thisComponent in poly2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "poly2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "poly3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    poly3Components = [text_9, background_2, text_10, polygon_7, polygon_8, polygon_9]
    for thisComponent in poly3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "poly3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and mouse.isPressedIn(polygon_8) or mouse.isPressedIn(polygon_9):
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_9.started')
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_9.stopped')
                text_9.setAutoDraw(False)
        
        # *background_2* updates
        if background_2.status == NOT_STARTED and mouse.isPressedIn(polygon_8):
            # keep track of start time/frame for later
            background_2.frameNStart = frameN  # exact frame index
            background_2.tStart = t  # local t and not account for scr refresh
            background_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_2.started')
            background_2.setAutoDraw(True)
        if background_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                background_2.tStop = t  # not accounting for scr refresh
                background_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_2.stopped')
                background_2.setAutoDraw(False)
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and mouse.isPressedIn(polygon_8):
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_10.started')
            text_10.setAutoDraw(True)
        if text_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_10.tStop = t  # not accounting for scr refresh
                text_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_10.stopped')
                text_10.setAutoDraw(False)
        
        # *polygon_7* updates
        if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_7.frameNStart = frameN  # exact frame index
            polygon_7.tStart = t  # local t and not account for scr refresh
            polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_7.started')
            polygon_7.setAutoDraw(True)
        if polygon_7.status == STARTED:
            if bool(mouse.isPressedIn(polygon_8)):
                # keep track of stop time/frame for later
                polygon_7.tStop = t  # not accounting for scr refresh
                polygon_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_7.stopped')
                polygon_7.setAutoDraw(False)
        
        # *polygon_8* updates
        if polygon_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_8.frameNStart = frameN  # exact frame index
            polygon_8.tStart = t  # local t and not account for scr refresh
            polygon_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_8.started')
            polygon_8.setAutoDraw(True)
        if polygon_8.status == STARTED:
            if bool(mouse.isPressedIn(polygon_8)):
                # keep track of stop time/frame for later
                polygon_8.tStop = t  # not accounting for scr refresh
                polygon_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_8.stopped')
                polygon_8.setAutoDraw(False)
        
        # *polygon_9* updates
        if polygon_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_9.frameNStart = frameN  # exact frame index
            polygon_9.tStart = t  # local t and not account for scr refresh
            polygon_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_9.started')
            polygon_9.setAutoDraw(True)
        if polygon_9.status == STARTED:
            if bool(mouse.isPressedIn(polygon_8)):
                # keep track of stop time/frame for later
                polygon_9.tStop = t  # not accounting for scr refresh
                polygon_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_9.stopped')
                polygon_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in poly3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "poly3" ---
    for thisComponent in poly3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "poly3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "poly4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    poly4Components = [text_11, background_4, text_12, polygon_10, polygon_11, polygon_12]
    for thisComponent in poly4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "poly4" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_11* updates
        if text_11.status == NOT_STARTED and mouse.isPressedIn(polygon_11) or mouse.isPressedIn(polygon_12):
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_11.started')
            text_11.setAutoDraw(True)
        if text_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_11.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_11.tStop = t  # not accounting for scr refresh
                text_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_11.stopped')
                text_11.setAutoDraw(False)
        
        # *background_4* updates
        if background_4.status == NOT_STARTED and mouse.isPressedIn(polygon_11):
            # keep track of start time/frame for later
            background_4.frameNStart = frameN  # exact frame index
            background_4.tStart = t  # local t and not account for scr refresh
            background_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_4.started')
            background_4.setAutoDraw(True)
        if background_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_4.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                background_4.tStop = t  # not accounting for scr refresh
                background_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_4.stopped')
                background_4.setAutoDraw(False)
        
        # *text_12* updates
        if text_12.status == NOT_STARTED and mouse.isPressedIn(polygon_11):
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_12.started')
            text_12.setAutoDraw(True)
        if text_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_12.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_12.tStop = t  # not accounting for scr refresh
                text_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_12.stopped')
                text_12.setAutoDraw(False)
        
        # *polygon_10* updates
        if polygon_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_10.frameNStart = frameN  # exact frame index
            polygon_10.tStart = t  # local t and not account for scr refresh
            polygon_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_10.started')
            polygon_10.setAutoDraw(True)
        if polygon_10.status == STARTED:
            if bool(mouse.isPressedIn(polygon_11)):
                # keep track of stop time/frame for later
                polygon_10.tStop = t  # not accounting for scr refresh
                polygon_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_10.stopped')
                polygon_10.setAutoDraw(False)
        
        # *polygon_11* updates
        if polygon_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_11.frameNStart = frameN  # exact frame index
            polygon_11.tStart = t  # local t and not account for scr refresh
            polygon_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_11.started')
            polygon_11.setAutoDraw(True)
        if polygon_11.status == STARTED:
            if bool(mouse.isPressedIn(polygon_11)):
                # keep track of stop time/frame for later
                polygon_11.tStop = t  # not accounting for scr refresh
                polygon_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_11.stopped')
                polygon_11.setAutoDraw(False)
        
        # *polygon_12* updates
        if polygon_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_12.frameNStart = frameN  # exact frame index
            polygon_12.tStart = t  # local t and not account for scr refresh
            polygon_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_12.started')
            polygon_12.setAutoDraw(True)
        if polygon_12.status == STARTED:
            if bool(mouse.isPressedIn(polygon_11)):
                # keep track of stop time/frame for later
                polygon_12.tStop = t  # not accounting for scr refresh
                polygon_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_12.stopped')
                polygon_12.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in poly4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "poly4" ---
    for thisComponent in poly4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "poly4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "poly5" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    poly5Components = [text_13, background_5, text_14, polygon_13, polygon_14, polygon_15]
    for thisComponent in poly5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "poly5" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_13* updates
        if text_13.status == NOT_STARTED and mouse.isPressedIn(polygon_14) or mouse.isPressedIn(polygon_15):
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_13.started')
            text_13.setAutoDraw(True)
        if text_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_13.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_13.tStop = t  # not accounting for scr refresh
                text_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_13.stopped')
                text_13.setAutoDraw(False)
        
        # *background_5* updates
        if background_5.status == NOT_STARTED and mouse.isPressedIn(polygon_14):
            # keep track of start time/frame for later
            background_5.frameNStart = frameN  # exact frame index
            background_5.tStart = t  # local t and not account for scr refresh
            background_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_5.started')
            background_5.setAutoDraw(True)
        if background_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_5.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                background_5.tStop = t  # not accounting for scr refresh
                background_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_5.stopped')
                background_5.setAutoDraw(False)
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and mouse.isPressedIn(polygon_14):
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_14.started')
            text_14.setAutoDraw(True)
        if text_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_14.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_14.stopped')
                text_14.setAutoDraw(False)
        
        # *polygon_13* updates
        if polygon_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_13.frameNStart = frameN  # exact frame index
            polygon_13.tStart = t  # local t and not account for scr refresh
            polygon_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_13.started')
            polygon_13.setAutoDraw(True)
        if polygon_13.status == STARTED:
            if bool(mouse.isPressedIn(polygon_14)):
                # keep track of stop time/frame for later
                polygon_13.tStop = t  # not accounting for scr refresh
                polygon_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_13.stopped')
                polygon_13.setAutoDraw(False)
        
        # *polygon_14* updates
        if polygon_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_14.frameNStart = frameN  # exact frame index
            polygon_14.tStart = t  # local t and not account for scr refresh
            polygon_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_14.started')
            polygon_14.setAutoDraw(True)
        if polygon_14.status == STARTED:
            if bool(mouse.isPressedIn(polygon_14)):
                # keep track of stop time/frame for later
                polygon_14.tStop = t  # not accounting for scr refresh
                polygon_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_14.stopped')
                polygon_14.setAutoDraw(False)
        
        # *polygon_15* updates
        if polygon_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_15.frameNStart = frameN  # exact frame index
            polygon_15.tStart = t  # local t and not account for scr refresh
            polygon_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_15.started')
            polygon_15.setAutoDraw(True)
        if polygon_15.status == STARTED:
            if bool(mouse.isPressedIn(polygon_14)):
                # keep track of stop time/frame for later
                polygon_15.tStop = t  # not accounting for scr refresh
                polygon_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_15.stopped')
                polygon_15.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in poly5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "poly5" ---
    for thisComponent in poly5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "poly5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "poly6" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    poly6Components = [text_15, background_6, text_16, polygon_16, polygon_17, polygon_18]
    for thisComponent in poly6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "poly6" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_15* updates
        if text_15.status == NOT_STARTED and mouse.isPressedIn(polygon_17) or mouse.isPressedIn(polygon_18):
            # keep track of start time/frame for later
            text_15.frameNStart = frameN  # exact frame index
            text_15.tStart = t  # local t and not account for scr refresh
            text_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_15.started')
            text_15.setAutoDraw(True)
        if text_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_15.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_15.tStop = t  # not accounting for scr refresh
                text_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_15.stopped')
                text_15.setAutoDraw(False)
        
        # *background_6* updates
        if background_6.status == NOT_STARTED and mouse.isPressedIn(polygon_17):
            # keep track of start time/frame for later
            background_6.frameNStart = frameN  # exact frame index
            background_6.tStart = t  # local t and not account for scr refresh
            background_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_6.started')
            background_6.setAutoDraw(True)
        if background_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_6.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                background_6.tStop = t  # not accounting for scr refresh
                background_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_6.stopped')
                background_6.setAutoDraw(False)
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and mouse.isPressedIn(polygon_17):
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_16.started')
            text_16.setAutoDraw(True)
        if text_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_16.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_16.tStop = t  # not accounting for scr refresh
                text_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_16.stopped')
                text_16.setAutoDraw(False)
        
        # *polygon_16* updates
        if polygon_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_16.frameNStart = frameN  # exact frame index
            polygon_16.tStart = t  # local t and not account for scr refresh
            polygon_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_16.started')
            polygon_16.setAutoDraw(True)
        if polygon_16.status == STARTED:
            if bool(mouse.isPressedIn(polygon_17)):
                # keep track of stop time/frame for later
                polygon_16.tStop = t  # not accounting for scr refresh
                polygon_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_16.stopped')
                polygon_16.setAutoDraw(False)
        
        # *polygon_17* updates
        if polygon_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_17.frameNStart = frameN  # exact frame index
            polygon_17.tStart = t  # local t and not account for scr refresh
            polygon_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_17.started')
            polygon_17.setAutoDraw(True)
        if polygon_17.status == STARTED:
            if bool(mouse.isPressedIn(polygon_17)):
                # keep track of stop time/frame for later
                polygon_17.tStop = t  # not accounting for scr refresh
                polygon_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_17.stopped')
                polygon_17.setAutoDraw(False)
        
        # *polygon_18* updates
        if polygon_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_18.frameNStart = frameN  # exact frame index
            polygon_18.tStart = t  # local t and not account for scr refresh
            polygon_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_18.started')
            polygon_18.setAutoDraw(True)
        if polygon_18.status == STARTED:
            if bool(mouse.isPressedIn(polygon_17)):
                # keep track of stop time/frame for later
                polygon_18.tStop = t  # not accounting for scr refresh
                polygon_18.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_18.stopped')
                polygon_18.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in poly6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "poly6" ---
    for thisComponent in poly6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "poly6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "poly7" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    poly7Components = [text_17, background_7, text_18, polygon_19, polygon_20, polygon_21]
    for thisComponent in poly7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "poly7" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_17* updates
        if text_17.status == NOT_STARTED and mouse.isPressedIn(polygon_20) or mouse.isPressedIn(polygon_21):
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_17.started')
            text_17.setAutoDraw(True)
        if text_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_17.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_17.tStop = t  # not accounting for scr refresh
                text_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_17.stopped')
                text_17.setAutoDraw(False)
        
        # *background_7* updates
        if background_7.status == NOT_STARTED and mouse.isPressedIn(polygon_21):
            # keep track of start time/frame for later
            background_7.frameNStart = frameN  # exact frame index
            background_7.tStart = t  # local t and not account for scr refresh
            background_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_7.started')
            background_7.setAutoDraw(True)
        if background_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_7.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                background_7.tStop = t  # not accounting for scr refresh
                background_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_7.stopped')
                background_7.setAutoDraw(False)
        
        # *text_18* updates
        if text_18.status == NOT_STARTED and mouse.isPressedIn(polygon_21):
            # keep track of start time/frame for later
            text_18.frameNStart = frameN  # exact frame index
            text_18.tStart = t  # local t and not account for scr refresh
            text_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_18.started')
            text_18.setAutoDraw(True)
        if text_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_18.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_18.tStop = t  # not accounting for scr refresh
                text_18.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_18.stopped')
                text_18.setAutoDraw(False)
        
        # *polygon_19* updates
        if polygon_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_19.frameNStart = frameN  # exact frame index
            polygon_19.tStart = t  # local t and not account for scr refresh
            polygon_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_19.started')
            polygon_19.setAutoDraw(True)
        if polygon_19.status == STARTED:
            if bool(mouse.isPressedIn(polygon_21)):
                # keep track of stop time/frame for later
                polygon_19.tStop = t  # not accounting for scr refresh
                polygon_19.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_19.stopped')
                polygon_19.setAutoDraw(False)
        
        # *polygon_20* updates
        if polygon_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_20.frameNStart = frameN  # exact frame index
            polygon_20.tStart = t  # local t and not account for scr refresh
            polygon_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_20.started')
            polygon_20.setAutoDraw(True)
        if polygon_20.status == STARTED:
            if bool(mouse.isPressedIn(polygon_21)):
                # keep track of stop time/frame for later
                polygon_20.tStop = t  # not accounting for scr refresh
                polygon_20.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_20.stopped')
                polygon_20.setAutoDraw(False)
        
        # *polygon_21* updates
        if polygon_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_21.frameNStart = frameN  # exact frame index
            polygon_21.tStart = t  # local t and not account for scr refresh
            polygon_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_21.started')
            polygon_21.setAutoDraw(True)
        if polygon_21.status == STARTED:
            if bool(mouse.isPressedIn(polygon_21)):
                # keep track of stop time/frame for later
                polygon_21.tStop = t  # not accounting for scr refresh
                polygon_21.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_21.stopped')
                polygon_21.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in poly7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "poly7" ---
    for thisComponent in poly7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "poly7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "poly8" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    poly8Components = [text_19, background_8, text_20, polygon_22, polygon_23, polygon_24]
    for thisComponent in poly8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "poly8" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_19* updates
        if text_19.status == NOT_STARTED and mouse.isPressedIn(polygon_23) or mouse.isPressedIn(polygon_24):
            # keep track of start time/frame for later
            text_19.frameNStart = frameN  # exact frame index
            text_19.tStart = t  # local t and not account for scr refresh
            text_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_19.started')
            text_19.setAutoDraw(True)
        if text_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_19.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_19.tStop = t  # not accounting for scr refresh
                text_19.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_19.stopped')
                text_19.setAutoDraw(False)
        
        # *background_8* updates
        if background_8.status == NOT_STARTED and mouse.isPressedIn(polygon_24):
            # keep track of start time/frame for later
            background_8.frameNStart = frameN  # exact frame index
            background_8.tStart = t  # local t and not account for scr refresh
            background_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_8.started')
            background_8.setAutoDraw(True)
        if background_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_8.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                background_8.tStop = t  # not accounting for scr refresh
                background_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_8.stopped')
                background_8.setAutoDraw(False)
        
        # *text_20* updates
        if text_20.status == NOT_STARTED and mouse.isPressedIn(polygon_24):
            # keep track of start time/frame for later
            text_20.frameNStart = frameN  # exact frame index
            text_20.tStart = t  # local t and not account for scr refresh
            text_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_20.started')
            text_20.setAutoDraw(True)
        if text_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_20.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_20.tStop = t  # not accounting for scr refresh
                text_20.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_20.stopped')
                text_20.setAutoDraw(False)
        
        # *polygon_22* updates
        if polygon_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_22.frameNStart = frameN  # exact frame index
            polygon_22.tStart = t  # local t and not account for scr refresh
            polygon_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_22.started')
            polygon_22.setAutoDraw(True)
        if polygon_22.status == STARTED:
            if bool(mouse.isPressedIn(polygon_24)):
                # keep track of stop time/frame for later
                polygon_22.tStop = t  # not accounting for scr refresh
                polygon_22.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_22.stopped')
                polygon_22.setAutoDraw(False)
        
        # *polygon_23* updates
        if polygon_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_23.frameNStart = frameN  # exact frame index
            polygon_23.tStart = t  # local t and not account for scr refresh
            polygon_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_23.started')
            polygon_23.setAutoDraw(True)
        if polygon_23.status == STARTED:
            if bool(mouse.isPressedIn(polygon_24)):
                # keep track of stop time/frame for later
                polygon_23.tStop = t  # not accounting for scr refresh
                polygon_23.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_23.stopped')
                polygon_23.setAutoDraw(False)
        
        # *polygon_24* updates
        if polygon_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_24.frameNStart = frameN  # exact frame index
            polygon_24.tStart = t  # local t and not account for scr refresh
            polygon_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_24.started')
            polygon_24.setAutoDraw(True)
        if polygon_24.status == STARTED:
            if bool(mouse.isPressedIn(polygon_24)):
                # keep track of stop time/frame for later
                polygon_24.tStop = t  # not accounting for scr refresh
                polygon_24.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_24.stopped')
                polygon_24.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in poly8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "poly8" ---
    for thisComponent in poly8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "poly8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "poly9" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    poly9Components = [text_21, background_9, text_22, polygon_25, polygon_26, polygon_27]
    for thisComponent in poly9Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "poly9" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_21* updates
        if text_21.status == NOT_STARTED and mouse.isPressedIn(polygon_26) or mouse.isPressedIn(polygon_27):
            # keep track of start time/frame for later
            text_21.frameNStart = frameN  # exact frame index
            text_21.tStart = t  # local t and not account for scr refresh
            text_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_21.started')
            text_21.setAutoDraw(True)
        if text_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_21.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_21.tStop = t  # not accounting for scr refresh
                text_21.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_21.stopped')
                text_21.setAutoDraw(False)
        
        # *background_9* updates
        if background_9.status == NOT_STARTED and mouse.isPressedIn(polygon_26):
            # keep track of start time/frame for later
            background_9.frameNStart = frameN  # exact frame index
            background_9.tStart = t  # local t and not account for scr refresh
            background_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_9.started')
            background_9.setAutoDraw(True)
        if background_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_9.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                background_9.tStop = t  # not accounting for scr refresh
                background_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_9.stopped')
                background_9.setAutoDraw(False)
        
        # *text_22* updates
        if text_22.status == NOT_STARTED and mouse.isPressedIn(polygon_26):
            # keep track of start time/frame for later
            text_22.frameNStart = frameN  # exact frame index
            text_22.tStart = t  # local t and not account for scr refresh
            text_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_22.started')
            text_22.setAutoDraw(True)
        if text_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_22.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_22.tStop = t  # not accounting for scr refresh
                text_22.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_22.stopped')
                text_22.setAutoDraw(False)
        
        # *polygon_25* updates
        if polygon_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_25.frameNStart = frameN  # exact frame index
            polygon_25.tStart = t  # local t and not account for scr refresh
            polygon_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_25.started')
            polygon_25.setAutoDraw(True)
        if polygon_25.status == STARTED:
            if bool(mouse.isPressedIn(polygon_26)):
                # keep track of stop time/frame for later
                polygon_25.tStop = t  # not accounting for scr refresh
                polygon_25.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_25.stopped')
                polygon_25.setAutoDraw(False)
        
        # *polygon_26* updates
        if polygon_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_26.frameNStart = frameN  # exact frame index
            polygon_26.tStart = t  # local t and not account for scr refresh
            polygon_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_26, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_26.started')
            polygon_26.setAutoDraw(True)
        if polygon_26.status == STARTED:
            if bool(mouse.isPressedIn(polygon_26)):
                # keep track of stop time/frame for later
                polygon_26.tStop = t  # not accounting for scr refresh
                polygon_26.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_26.stopped')
                polygon_26.setAutoDraw(False)
        
        # *polygon_27* updates
        if polygon_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_27.frameNStart = frameN  # exact frame index
            polygon_27.tStart = t  # local t and not account for scr refresh
            polygon_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_27, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_27.started')
            polygon_27.setAutoDraw(True)
        if polygon_27.status == STARTED:
            if bool(mouse.isPressedIn(polygon_26)):
                # keep track of stop time/frame for later
                polygon_27.tStop = t  # not accounting for scr refresh
                polygon_27.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_27.stopped')
                polygon_27.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in poly9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "poly9" ---
    for thisComponent in poly9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "poly9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "poly10" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    poly10Components = [text_23, background_10, text_24, polygon_28, polygon_29, polygon_30]
    for thisComponent in poly10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "poly10" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_23* updates
        if text_23.status == NOT_STARTED and mouse.isPressedIn(polygon_30) or mouse.isPressedIn(polygon_29):
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_23.started')
            text_23.setAutoDraw(True)
        if text_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_23.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_23.tStop = t  # not accounting for scr refresh
                text_23.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_23.stopped')
                text_23.setAutoDraw(False)
        
        # *background_10* updates
        if background_10.status == NOT_STARTED and mouse.isPressedIn(polygon_30):
            # keep track of start time/frame for later
            background_10.frameNStart = frameN  # exact frame index
            background_10.tStart = t  # local t and not account for scr refresh
            background_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(background_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'background_10.started')
            background_10.setAutoDraw(True)
        if background_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > background_10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                background_10.tStop = t  # not accounting for scr refresh
                background_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'background_10.stopped')
                background_10.setAutoDraw(False)
        
        # *text_24* updates
        if text_24.status == NOT_STARTED and mouse.isPressedIn(polygon_30):
            # keep track of start time/frame for later
            text_24.frameNStart = frameN  # exact frame index
            text_24.tStart = t  # local t and not account for scr refresh
            text_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_24.started')
            text_24.setAutoDraw(True)
        if text_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_24.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_24.tStop = t  # not accounting for scr refresh
                text_24.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_24.stopped')
                text_24.setAutoDraw(False)
        
        # *polygon_28* updates
        if polygon_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_28.frameNStart = frameN  # exact frame index
            polygon_28.tStart = t  # local t and not account for scr refresh
            polygon_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_28, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_28.started')
            polygon_28.setAutoDraw(True)
        if polygon_28.status == STARTED:
            if bool(mouse.isPressedIn(polygon_30)):
                # keep track of stop time/frame for later
                polygon_28.tStop = t  # not accounting for scr refresh
                polygon_28.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_28.stopped')
                polygon_28.setAutoDraw(False)
        
        # *polygon_29* updates
        if polygon_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_29.frameNStart = frameN  # exact frame index
            polygon_29.tStart = t  # local t and not account for scr refresh
            polygon_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_29.started')
            polygon_29.setAutoDraw(True)
        if polygon_29.status == STARTED:
            if bool(mouse.isPressedIn(polygon_30)):
                # keep track of stop time/frame for later
                polygon_29.tStop = t  # not accounting for scr refresh
                polygon_29.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_29.stopped')
                polygon_29.setAutoDraw(False)
        
        # *polygon_30* updates
        if polygon_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_30.frameNStart = frameN  # exact frame index
            polygon_30.tStart = t  # local t and not account for scr refresh
            polygon_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_30, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygon_30.started')
            polygon_30.setAutoDraw(True)
        if polygon_30.status == STARTED:
            if bool(mouse.isPressedIn(polygon_30)):
                # keep track of stop time/frame for later
                polygon_30.tStop = t  # not accounting for scr refresh
                polygon_30.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_30.stopped')
                polygon_30.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in poly10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "poly10" ---
    for thisComponent in poly10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "poly10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "trial" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
trialComponents = [mouse, text]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trial" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse.started', t)
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:
        if bool(mouse.getPressed()[0]):
            # keep track of stop time/frame for later
            mouse.tStop = t  # not accounting for scr refresh
            mouse.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.addData('mouse.stopped', t)
            mouse.status = FINISHED
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([text_2,text_3])
                    clickableList = [text_2,text_3]
                except:
                    clickableList = [[text_2,text_3]]
                for obj in clickableList:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
                if gotValidClick:
                    continueRoutine = False  # abort routine on response
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    if text.status == STARTED:
        if bool(mouse.getPressed()[0]):
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trial" ---
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.addData('mouse.clicked_name', mouse.clicked_name)
thisExp.nextEntry()
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)

thisExp.abort()  # or data files will save again on exit


#creates a scatterplot of degrees rotated vs. seconds to click
def plot_results(name):
    print(name)
    data = []
    with open(name +'.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            data.append(row)
   
    events = data[0]
    times = data[1]

    t = [
        float(times[events.index('polygon.stopped')]) - float(times[events.index('polygon.started')]),
        float(times[events.index('polygon_4.stopped')]) - float(times[events.index('polygon_4.started')]),
        float(times[events.index('polygon_7.stopped')]) - float(times[events.index('polygon_7.started')]),
        float(times[events.index('polygon_10.stopped')]) - float(times[events.index('polygon_10.started')]),
        float(times[events.index('polygon_13.stopped')]) - float(times[events.index('polygon_13.started')]),
        float(times[events.index('polygon_16.stopped')]) - float(times[events.index('polygon_16.started')]),
        float(times[events.index('polygon_19.stopped')]) - float(times[events.index('polygon_19.started')]),
        float(times[events.index('polygon_22.stopped')]) - float(times[events.index('polygon_22.started')]),
        float(times[events.index('polygon_25.stopped')]) - float(times[events.index('polygon_25.started')]),
        float(times[events.index('polygon_28.stopped')]) - float(times[events.index('polygon_28.started')])
        ]

    a = [60,20,34,40,47,90,52,9,50,30]
    plt.plot(np.unique(a), np.poly1d(np.polyfit(a, t, 1))(np.unique(a)))
    plt.scatter(a,t)
    plt.ylabel("Response Time (s)")
    plt.xlabel("Degrees Rotated")
    plt.title("Rotation Experiment Results")
    plt.show()
   
    return

plot_results(filename)

win.close()
core.quit()
