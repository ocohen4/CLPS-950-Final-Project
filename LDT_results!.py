#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Tue May  9 18:31:31 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""
## Lexical Decision Task
#MAIZY WROTE AND DEBUGGED, 17 hours total

# --- Import packages ---
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'Lexical Decision Task 2'  # from the Builder filename that created this script
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
    originPath='/Users/maizynunes/Desktop/Lexical Decision Task 2.py',
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

# --- Initialize components for Routine "start" ---
start_text = visual.TextStim(win=win, name='start_text',
    text="You will see two words.\n\nIf they are both REAL words, PRESS 'Z'.\n\nIf one or both are NONSENSE words, PRESS 'M'. (ex:DOGZ)\n\nRespond quickly!\nClick the space bar to start. \n\n",
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from code
n_related = 0
rt_related = 0.0

n_unrelated = 0
rt_unrelated = 0.0

n_nonsense = 0
rt_nonsense = 0.0
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='Welcome to the Lexical Decision Task Experiment!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color=[1.0000, 0.2549, -0.0431], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "trial" ---
trial_text = visual.TextStim(win=win, name='trial_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trial_resp = keyboard.Keyboard()

# --- Initialize components for Routine "correct1" ---
correct1_text = visual.TextStim(win=win, name='correct1_text',
    text='Correct!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.1922, 0.9686, 0.1922], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "incorrect1" ---
incorrect1_text = visual.TextStim(win=win, name='incorrect1_text',
    text='Incorrect',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7255, -0.8431, -0.5294], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "feedback_reaction_rate" ---
results_text = visual.TextStim(win=win, name='results_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
end_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "start" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
start_resp.keys = []
start_resp.rt = []
_start_resp_allKeys = []
# keep track of which components have finished
startComponents = [start_text, start_resp, welcome_text]
for thisComponent in startComponents:
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

# --- Run Routine "start" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_text* updates
    if start_text.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        start_text.frameNStart = frameN  # exact frame index
        start_text.tStart = t  # local t and not account for scr refresh
        start_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_text.started')
        start_text.setAutoDraw(True)
    
    # *start_resp* updates
    waitOnFlip = False
    if start_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_resp.frameNStart = frameN  # exact frame index
        start_resp.tStart = t  # local t and not account for scr refresh
        start_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_resp.started')
        start_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_resp.status == STARTED and not waitOnFlip:
        theseKeys = start_resp.getKeys(keyList=['space'], waitRelease=False)
        _start_resp_allKeys.extend(theseKeys)
        if len(_start_resp_allKeys):
            start_resp.keys = _start_resp_allKeys[-1].name  # just the last key pressed
            start_resp.rt = _start_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_text.started')
        welcome_text.setAutoDraw(True)
    if welcome_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome_text.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            welcome_text.tStop = t  # not accounting for scr refresh
            welcome_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_text.stopped')
            welcome_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start" ---
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start_resp.keys in ['', [], None]:  # No response was made
    start_resp.keys = None
thisExp.addData('start_resp.keys',start_resp.keys)
if start_resp.keys != None:  # we had a response
    thisExp.addData('start_resp.rt', start_resp.rt)
thisExp.nextEntry()
# Run 'End Routine' code from code
if start_resp.keys == 'space':
    numReps= 1

# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=numReps, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PracticePsychoPywithKey3.xlsx'),
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
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    trial_text.setText(word)
    trial_resp.keys = []
    trial_resp.rt = []
    _trial_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [trial_text, trial_resp]
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
        
        # *trial_text* updates
        if trial_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_text.frameNStart = frameN  # exact frame index
            trial_text.tStart = t  # local t and not account for scr refresh
            trial_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_text.started')
            trial_text.setAutoDraw(True)
        
        # *trial_resp* updates
        waitOnFlip = False
        if trial_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_resp.frameNStart = frameN  # exact frame index
            trial_resp.tStart = t  # local t and not account for scr refresh
            trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_resp.started')
            trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = trial_resp.getKeys(keyList=['z','m'], waitRelease=False)
            _trial_resp_allKeys.extend(theseKeys)
            if len(_trial_resp_allKeys):
                trial_resp.keys = _trial_resp_allKeys[-1].name  # just the last key pressed
                trial_resp.rt = _trial_resp_allKeys[-1].rt
                # was this correct?
                if (trial_resp.keys == str(correctKey)) or (trial_resp.keys == correctKey):
                    trial_resp.corr = 1
                else:
                    trial_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
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
    # check responses
    if trial_resp.keys in ['', [], None]:  # No response was made
        trial_resp.keys = None
        # was no response the correct answer?!
        if str(correctKey).lower() == 'none':
           trial_resp.corr = 1;  # correct non-response
        else:
           trial_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('trial_resp.keys',trial_resp.keys)
    trials.addData('trial_resp.corr', trial_resp.corr)
    if trial_resp.keys != None:  # we had a response
        trials.addData('trial_resp.rt', trial_resp.rt)
    # Run 'End Routine' code from code_3
    if type == 'related': 
        n_related = n_related + 1
        total_rt_related = rt_related  + trial_resp.rt
    if type == 'unrelated':
        n_unrelated = n_unrelated + 1
        total_rt_unrelated = rt_unrelated + trial_resp.rt
    if type == 'nonsense':
        n_nonsense = n_nonsense + 1
        total_rt_nonsense = rt_nonsense  + trial_resp.rt
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "correct1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    correct1Components = [correct1_text]
    for thisComponent in correct1Components:
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
    
    # --- Run Routine "correct1" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *correct1_text* updates
        if correct1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            correct1_text.frameNStart = frameN  # exact frame index
            correct1_text.tStart = t  # local t and not account for scr refresh
            correct1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(correct1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'correct1_text.started')
            correct1_text.setAutoDraw(True)
        if correct1_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correct1_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                correct1_text.tStop = t  # not accounting for scr refresh
                correct1_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'correct1_text.stopped')
                correct1_text.setAutoDraw(False)
        # Run 'Each Frame' code from code_2
        if (trial_resp.corr==0):
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in correct1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "correct1" ---
    for thisComponent in correct1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "incorrect1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    incorrect1Components = [incorrect1_text]
    for thisComponent in incorrect1Components:
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
    
    # --- Run Routine "incorrect1" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *incorrect1_text* updates
        if incorrect1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            incorrect1_text.frameNStart = frameN  # exact frame index
            incorrect1_text.tStart = t  # local t and not account for scr refresh
            incorrect1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(incorrect1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'incorrect1_text.started')
            incorrect1_text.setAutoDraw(True)
        if incorrect1_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > incorrect1_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                incorrect1_text.tStop = t  # not accounting for scr refresh
                incorrect1_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'incorrect1_text.stopped')
                incorrect1_text.setAutoDraw(False)
        # Run 'Each Frame' code from code_6
        if (trial_resp.corr ==1):
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in incorrect1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "incorrect1" ---
    for thisComponent in incorrect1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed numReps repeats of 'trials'


# --- Prepare to start Routine "feedback_reaction_rate" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_4
mean_related = round(((total_rt_related / n_related) *1000), 3)
mean_unrelated = round(((total_rt_unrelated / n_unrelated) *1000), 3)
mean_nonsense = round(((total_rt_nonsense / n_nonsense) *1000), 3)
results_text.setText("RELATED words (ms):" + '\n' + str(mean_related) + '\n' + "UNRELATED words (ms):" + '\n' + str(mean_unrelated) + '\n' + "NONSENSE words (ms):" '\n' + str(mean_nonsense)+ '\n' + "Press space to exit.")
end_resp.keys = []
end_resp.rt = []
_end_resp_allKeys = []
# keep track of which components have finished
feedback_reaction_rateComponents = [results_text, end_resp]
for thisComponent in feedback_reaction_rateComponents:
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

# --- Run Routine "feedback_reaction_rate" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *results_text* updates
    if results_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        results_text.frameNStart = frameN  # exact frame index
        results_text.tStart = t  # local t and not account for scr refresh
        results_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(results_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'results_text.started')
        results_text.setAutoDraw(True)
    if results_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > results_text.tStartRefresh + 15.0-frameTolerance:
            # keep track of stop time/frame for later
            results_text.tStop = t  # not accounting for scr refresh
            results_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'results_text.stopped')
            results_text.setAutoDraw(False)
    
    # *end_resp* updates
    waitOnFlip = False
    if end_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_resp.frameNStart = frameN  # exact frame index
        end_resp.tStart = t  # local t and not account for scr refresh
        end_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_resp.started')
        end_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_resp.status == STARTED and not waitOnFlip:
        theseKeys = end_resp.getKeys(keyList=['space'], waitRelease=False)
        _end_resp_allKeys.extend(theseKeys)
        if len(_end_resp_allKeys):
            end_resp.keys = _end_resp_allKeys[-1].name  # just the last key pressed
            end_resp.rt = _end_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in feedback_reaction_rateComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "feedback_reaction_rate" ---
for thisComponent in feedback_reaction_rateComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_resp.keys in ['', [], None]:  # No response was made
    end_resp.keys = None
thisExp.addData('end_resp.keys',end_resp.keys)
if end_resp.keys != None:  # we had a response
    thisExp.addData('end_resp.rt', end_resp.rt)
thisExp.nextEntry()
# the Routine "feedback_reaction_rate" was not non-slip safe, so reset the non-slip timer
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
win.close()
core.quit()
