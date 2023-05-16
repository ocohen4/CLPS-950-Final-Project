#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Tue May  9 18:31:11 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""
#SOPHIA WROTE AND DEBUGGED

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
expName = 'stroop experiment'  # from the Builder filename that created this script
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
    originPath='/Users/sophiasadikman/Documents/stroop_experiment_final.py',
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
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
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

# --- Initialize components for Routine "Instructions" ---
WelcomeMessage = visual.TextStim(win=win, name='WelcomeMessage',
    text='Welcome to the Stroop task!\n\nIn this task, you will see words that describe colors. You need to respond to the physical color of the words/letters, not their meaning, by pressing the corresponding key (r,g,b,y for red, green, blue, and yellow stimuli).\n\nPress the space bar to start!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyStart = keyboard.Keyboard()
# Run 'Begin Experiment' code from initialize_variables
# initialize some variables:
n_congruent = 0
rt_congruent = 0.0

n_incongruent = 0
rt_incongruent = 0.0

# --- Initialize components for Routine "blank500" ---
textblank500 = visual.TextStim(win=win, name='textblank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "stroopTrial" ---
textstroopWord = visual.TextStim(win=win, name='textstroopWord',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyStroop = keyboard.Keyboard()

# --- Initialize components for Routine "Correct" ---
text_correct = visual.TextStim(win=win, name='text_correct',
    text='Correct',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Incorrect" ---
text_incorrect = visual.TextStim(win=win, name='text_incorrect',
    text='Incorrect',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "blank500" ---
textblank500 = visual.TextStim(win=win, name='textblank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Feedback_reactiontime" ---
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "GoodbyeScreen" ---
textGoodbye = visual.TextStim(win=win, name='textGoodbye',
    text='Thanks for participating!\n\n\nPress SPACEBAR to exit the experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
endexperiment = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
keyStart.keys = []
keyStart.rt = []
_keyStart_allKeys = []
# keep track of which components have finished
InstructionsComponents = [WelcomeMessage, keyStart]
for thisComponent in InstructionsComponents:
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

# --- Run Routine "Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeMessage* updates
    if WelcomeMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeMessage.frameNStart = frameN  # exact frame index
        WelcomeMessage.tStart = t  # local t and not account for scr refresh
        WelcomeMessage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeMessage, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'WelcomeMessage.started')
        WelcomeMessage.setAutoDraw(True)
    
    # *keyStart* updates
    waitOnFlip = False
    if keyStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyStart.frameNStart = frameN  # exact frame index
        keyStart.tStart = t  # local t and not account for scr refresh
        keyStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyStart, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'keyStart.started')
        keyStart.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyStart.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyStart.status == STARTED and not waitOnFlip:
        theseKeys = keyStart.getKeys(keyList=['space'], waitRelease=False)
        _keyStart_allKeys.extend(theseKeys)
        if len(_keyStart_allKeys):
            keyStart.keys = _keyStart_allKeys[-1].name  # just the last key pressed
            keyStart.rt = _keyStart_allKeys[-1].rt
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
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if keyStart.keys in ['', [], None]:  # No response was made
    keyStart.keys = None
thisExp.addData('keyStart.keys',keyStart.keys)
if keyStart.keys != None:  # we had a response
    thisExp.addData('keyStart.rt', keyStart.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank500" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [textblank500]
for thisComponent in blank500Components:
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

# --- Run Routine "blank500" ---
while continueRoutine and routineTimer.getTime() < 0.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textblank500* updates
    if textblank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textblank500.frameNStart = frameN  # exact frame index
        textblank500.tStart = t  # local t and not account for scr refresh
        textblank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textblank500, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textblank500.started')
        textblank500.setAutoDraw(True)
    if textblank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textblank500.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            textblank500.tStop = t  # not accounting for scr refresh
            textblank500.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textblank500.stopped')
            textblank500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank500" ---
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.500000)

# set up handler to look after randomisation of conditions etc
trialsStroop = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stroop_conditions_stimuli.xlsx'),
    seed=None, name='trialsStroop')
thisExp.addLoop(trialsStroop)  # add the loop to the experiment
thisTrialsStroop = trialsStroop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsStroop.rgb)
if thisTrialsStroop != None:
    for paramName in thisTrialsStroop:
        exec('{} = thisTrialsStroop[paramName]'.format(paramName))

for thisTrialsStroop in trialsStroop:
    currentLoop = trialsStroop
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsStroop.rgb)
    if thisTrialsStroop != None:
        for paramName in thisTrialsStroop:
            exec('{} = thisTrialsStroop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "stroopTrial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    textstroopWord.setColor(color, colorSpace='rgb')
    textstroopWord.setText(word)
    keyStroop.keys = []
    keyStroop.rt = []
    _keyStroop_allKeys = []
    # keep track of which components have finished
    stroopTrialComponents = [textstroopWord, keyStroop]
    for thisComponent in stroopTrialComponents:
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
    
    # --- Run Routine "stroopTrial" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textstroopWord* updates
        if textstroopWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textstroopWord.frameNStart = frameN  # exact frame index
            textstroopWord.tStart = t  # local t and not account for scr refresh
            textstroopWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textstroopWord, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textstroopWord.started')
            textstroopWord.setAutoDraw(True)
        if textstroopWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textstroopWord.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                textstroopWord.tStop = t  # not accounting for scr refresh
                textstroopWord.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textstroopWord.stopped')
                textstroopWord.setAutoDraw(False)
        
        # *keyStroop* updates
        waitOnFlip = False
        if keyStroop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyStroop.frameNStart = frameN  # exact frame index
            keyStroop.tStart = t  # local t and not account for scr refresh
            keyStroop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyStroop, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyStroop.started')
            keyStroop.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyStroop.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyStroop.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyStroop.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyStroop.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                keyStroop.tStop = t  # not accounting for scr refresh
                keyStroop.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyStroop.stopped')
                keyStroop.status = FINISHED
        if keyStroop.status == STARTED and not waitOnFlip:
            theseKeys = keyStroop.getKeys(keyList=['r','g','b','y'], waitRelease=False)
            _keyStroop_allKeys.extend(theseKeys)
            if len(_keyStroop_allKeys):
                keyStroop.keys = _keyStroop_allKeys[-1].name  # just the last key pressed
                keyStroop.rt = _keyStroop_allKeys[-1].rt
                # was this correct?
                if (keyStroop.keys == str(correct_key)) or (keyStroop.keys == correct_key):
                    keyStroop.corr = 1
                else:
                    keyStroop.corr = 0
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
        for thisComponent in stroopTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stroopTrial" ---
    for thisComponent in stroopTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyStroop.keys in ['', [], None]:  # No response was made
        keyStroop.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           keyStroop.corr = 1;  # correct non-response
        else:
           keyStroop.corr = 0;  # failed to respond (incorrectly)
    # store data for trialsStroop (TrialHandler)
    trialsStroop.addData('keyStroop.keys',keyStroop.keys)
    trialsStroop.addData('keyStroop.corr', keyStroop.corr)
    if keyStroop.keys != None:  # we had a response
        trialsStroop.addData('keyStroop.rt', keyStroop.rt)
    # Run 'End Routine' code from congruent_incongruent
    if type == 'congruent': 
        n_congruent = n_congruent + 1
        total_rt_congruent = rt_congruent  + keyStroop.rt
    elif type == 'incongruent':
        n_incongruent = n_incongruent + 1
        total_rt_incongruent = rt_incongruent + keyStroop.rt
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "Correct" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    CorrectComponents = [text_correct]
    for thisComponent in CorrectComponents:
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
    
    # --- Run Routine "Correct" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_correct* updates
        if text_correct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_correct.frameNStart = frameN  # exact frame index
            text_correct.tStart = t  # local t and not account for scr refresh
            text_correct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_correct, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_correct.started')
            text_correct.setAutoDraw(True)
        if text_correct.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_correct.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_correct.tStop = t  # not accounting for scr refresh
                text_correct.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_correct.stopped')
                text_correct.setAutoDraw(False)
        # Run 'Each Frame' code from correct_code
        if (keyStroop.corr == 0):
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CorrectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Correct" ---
    for thisComponent in CorrectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "Incorrect" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    IncorrectComponents = [text_incorrect]
    for thisComponent in IncorrectComponents:
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
    
    # --- Run Routine "Incorrect" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_incorrect* updates
        if text_incorrect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_incorrect.frameNStart = frameN  # exact frame index
            text_incorrect.tStart = t  # local t and not account for scr refresh
            text_incorrect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_incorrect, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_incorrect.started')
            text_incorrect.setAutoDraw(True)
        if text_incorrect.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_incorrect.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text_incorrect.tStop = t  # not accounting for scr refresh
                text_incorrect.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_incorrect.stopped')
                text_incorrect.setAutoDraw(False)
        # Run 'Each Frame' code from incorrect_code
        if (keyStroop.corr == 1):
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IncorrectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Incorrect" ---
    for thisComponent in IncorrectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "blank500" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    blank500Components = [textblank500]
    for thisComponent in blank500Components:
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
    
    # --- Run Routine "blank500" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textblank500* updates
        if textblank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textblank500.frameNStart = frameN  # exact frame index
            textblank500.tStart = t  # local t and not account for scr refresh
            textblank500.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textblank500, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textblank500.started')
            textblank500.setAutoDraw(True)
        if textblank500.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textblank500.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                textblank500.tStop = t  # not accounting for scr refresh
                textblank500.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textblank500.stopped')
                textblank500.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank500" ---
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'trialsStroop'


# --- Prepare to start Routine "Feedback_reactiontime" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from mean_rt
mean_congruent = round(((total_rt_congruent / n_congruent) * 1000), 2)
mean_incongruent = round(((total_rt_incongruent / n_incongruent) * 1000), 2)

text.setText("CONGRUENT: " + str(mean_congruent) + "  ms" + '\n' + '\n' + '\n' + '\n' + "INCONGRUENT: " + str(mean_incongruent) + "  ms"
)
# keep track of which components have finished
Feedback_reactiontimeComponents = [text]
for thisComponent in Feedback_reactiontimeComponents:
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

# --- Run Routine "Feedback_reactiontime" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 5-frameTolerance:
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
    for thisComponent in Feedback_reactiontimeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Feedback_reactiontime" ---
for thisComponent in Feedback_reactiontimeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "GoodbyeScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
endexperiment.keys = []
endexperiment.rt = []
_endexperiment_allKeys = []
# keep track of which components have finished
GoodbyeScreenComponents = [textGoodbye, endexperiment]
for thisComponent in GoodbyeScreenComponents:
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

# --- Run Routine "GoodbyeScreen" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textGoodbye* updates
    if textGoodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textGoodbye.frameNStart = frameN  # exact frame index
        textGoodbye.tStart = t  # local t and not account for scr refresh
        textGoodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textGoodbye, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'textGoodbye.started')
        textGoodbye.setAutoDraw(True)
    if textGoodbye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textGoodbye.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            textGoodbye.tStop = t  # not accounting for scr refresh
            textGoodbye.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textGoodbye.stopped')
            textGoodbye.setAutoDraw(False)
    
    # *endexperiment* updates
    waitOnFlip = False
    if endexperiment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endexperiment.frameNStart = frameN  # exact frame index
        endexperiment.tStart = t  # local t and not account for scr refresh
        endexperiment.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endexperiment, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endexperiment.started')
        endexperiment.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endexperiment.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endexperiment.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endexperiment.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endexperiment.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            endexperiment.tStop = t  # not accounting for scr refresh
            endexperiment.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endexperiment.stopped')
            endexperiment.status = FINISHED
    if endexperiment.status == STARTED and not waitOnFlip:
        theseKeys = endexperiment.getKeys(keyList=['space'], waitRelease=False)
        _endexperiment_allKeys.extend(theseKeys)
        if len(_endexperiment_allKeys):
            endexperiment.keys = _endexperiment_allKeys[-1].name  # just the last key pressed
            endexperiment.rt = _endexperiment_allKeys[-1].rt
            # was this correct?
            if (endexperiment.keys == str(correct_key)) or (endexperiment.keys == correct_key):
                endexperiment.corr = 1
            else:
                endexperiment.corr = 0
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
    for thisComponent in GoodbyeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GoodbyeScreen" ---
for thisComponent in GoodbyeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if endexperiment.keys in ['', [], None]:  # No response was made
    endexperiment.keys = None
    # was no response the correct answer?!
    if str(correct_key).lower() == 'none':
       endexperiment.corr = 1;  # correct non-response
    else:
       endexperiment.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('endexperiment.keys',endexperiment.keys)
thisExp.addData('endexperiment.corr', endexperiment.corr)
if endexperiment.keys != None:  # we had a response
    thisExp.addData('endexperiment.rt', endexperiment.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

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
