from re import A
from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        racket2 = cast.get_last_actor(RACKET_GROUP)

        if self._keyboard_service.is_key_down(LEFT):
            racket.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT):
            racket.swing_right()
        elif self._keyboard_service.is_key_down(A):
            racket2.swing_left()
        elif self._keyboard_service.is_key_down(D):
            racket2.swing_right()
        else:
            racket.stop_moving()
            racket2.stop_moving()
