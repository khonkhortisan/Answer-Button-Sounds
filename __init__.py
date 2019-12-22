"""
Answer Button Sounds addon for Anki 2.1 by Kyle "Khonkhortisan" Mills
"""

import os

from aqt.reviewer import Reviewer
from anki.hooks import wrap
from anki.sound import play, clearAudioQueue

#don't let nextCard crash (I wish it would tell me when I'm missing includes)
#from aqt.utils import (askUserDialog, downArrow, mungeQA,
#                       qtMenuShortcutWorkaround, tooltip)
from aqt.utils import askUserDialog
from aqt.qt import * #QMessageBox


#Toggle this variable if the nextCard function conflicts with another addon,
#or you don't like the next card's audio delay
#and are willing to lose this addon's sound effects some of the time.
LetSoundBleedOntoNextCard_InsteadOf_CancelingSoundEffectSometimes=True


addon_path = os.path.dirname(__file__)
user_files = os.path.join(addon_path, "user_files")

#def pageflip(self, url):
#	play(os.path.join(user_files, "flip.mp3"))
#	error();
#	if url == "ans":
#		clearAudioQueue()
#		play(os.path.join(user_files, "flip.mp3"))
#		#preventclearingAudioQueue()
#		error();
#	#if url == "del":
#	#	clearAudioQueue()
#	#	play(os.path.join(user_files, "rip.mp3"))
#	#	#preventclearingAudioQueue()
#	#	error();
#Reviewer._linkHandler = wrap(Reviewer._linkHandler, pageflip, "before")


def answersound(self, ease):
	#add sounds for extra buttons here
	if ease == 1:
		clearAudioQueue() #force feedback to play
		play(os.path.join(user_files, "again.mp3"))
		#preventclearingAudioQueue() #see nextCard()
	if ease == 2:
		clearAudioQueue()
		play(os.path.join(user_files, "hard.mp3"))
		#preventclearingAudioQueue()
	if ease == 3:
		clearAudioQueue()
		play(os.path.join(user_files, "good.mp3"))
		#preventclearingAudioQueue()
	if ease == 4:
		clearAudioQueue()
		play(os.path.join(user_files, "easy.mp3"))
		#preventclearingAudioQueue()
	#add sounds for extra buttons here
Reviewer._answerCard = wrap(Reviewer._answerCard, answersound, "before")


#already cleared the audio queue, don't do it again and lose the sound effects.
#but it delays the next card's sounds.
def nextCard(self):
    elapsed = self.mw.col.timeboxReached()
    if elapsed:
        part1 = ngettext("%d card studied in", "%d cards studied in", elapsed[1]) % elapsed[1]
        mins = int(round(elapsed[0]/60))
        part2 = ngettext("%s minute.", "%s minutes.", mins) % mins
        fin = _("Finish")
        diag = askUserDialog("%s %s" % (part1, part2),
                         [_("Continue"), fin])
        diag.setIcon(QMessageBox.Information)
        if diag.run() == fin:
            return self.mw.moveToState("deckBrowser")
        self.mw.col.startTimebox()
    if self.cardQueue:
        # undone/edited cards to show
        c = self.cardQueue.pop()
        c.startTimer()
        self.hadCardQueue = True
    else:
        if self.hadCardQueue:
            # the undone/edited cards may be sitting in the regular queue;
            # need to reset
            self.mw.col.reset()
            self.hadCardQueue = False
        c = self.mw.col.sched.getCard()
    self.card = c
#   clearAudioQueue()
    if not c:
        self.mw.moveToState("overview")
        return
    if self._reps is None or self._reps % 100 == 0:
        # we recycle the webview periodically so webkit can free memory
        self._initWeb()
    self._showQuestion()
if LetSoundBleedOntoNextCard_InsteadOf_CancelingSoundEffectSometimes:
	Reviewer.nextCard=nextCard