"""
Answer Button Sounds addon for Anki 2.1.20 by Kyle "Khonkhortisan" Mills
"""

import os

from anki import hooks
from aqt.sound import play, clearAudioQueue, AVPlayer
#from aqt.reviewer import Reviewer

addon_path = os.path.dirname(__file__)
user_files = os.path.join(addon_path, "user_files")

def answersound(card, ease, early):
	clearAudioQueue() #force feedback to play now
	#add sounds for extra buttons here
	if ease == 1:
		play(os.path.join(user_files, "again.mp3"))
	if ease == 2:
		clearAudioQueue()
		play(os.path.join(user_files, "hard.mp3"))
	if ease == 3:
		clearAudioQueue()
		play(os.path.join(user_files, "good.mp3"))
	if ease == 4:
		clearAudioQueue()
		play(os.path.join(user_files, "easy.mp3"))
	#add sounds for extra buttons here
	#preventclearingAudioQueue() #see ~~nextCard()~~ play_tags #force feedback to continue playing now
hooks.schedv2_did_answer_review_card.append(answersound)

if LetSoundBleedOntoNextCard_InsteadOf_CancelingSoundEffectSometimes:
    def _play_tags(self, tags: List[AVTag]) -> None:
        """Clear the existing queue, then start playing provided tags."""
        self._enqueued = tags[:]
        #if self.interrupt_current_audio:
        #if self.interrupt_current_audio and not nextCard
        if self.interrupt_current_audio and False: #TODO: do clear audio when flipping to back, don't clear it when going to the next card. This was easier when it was in the nextCard function so I could just disable it there.
            self._stop_if_playing()
        self._play_next_if_idle()
    AVPlayer.play_tags=_play_tags

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
#Reviewer._linkHandler = hooks.wrap(Reviewer._linkHandler, pageflip, "before")