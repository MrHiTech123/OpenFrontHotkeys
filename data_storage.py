from enum import Enum
from typing import NamedTuple

import pyautogui
import pynput.keyboard as keyboard
from time import sleep


class BuildValue(NamedTuple):
    key: str | keyboard.Key
    mouse_x: int
    mouse_y: int
    
    def do(self):
        Action.BUILD.value.do()
        
        original_coords = pyautogui.position()
        pyautogui.moveTo(self.mouse_x, self.mouse_y)
        pyautogui.leftClick()
        sleep(.1)
        pyautogui.moveTo(*original_coords)
        

class Build(Enum):
    ATOM_BOMB = BuildValue('a', 612, 499)
    MIRV = BuildValue('v', 779, 508)
    HYDROGEN_BOMB = BuildValue('h', 951, 500)
    WARSHIP = BuildValue('w', 1125, 508)
    PORT = BuildValue('p', 1315, 485)
    MISSILE_SILO = BuildValue('m', 698, 697)
    SAM_LAUNCHER = BuildValue('s', 878, 707)
    DEFENSE_POST = BuildValue('d', 1067, 704)
    CITY = BuildValue('c', 1235, 701)
        
    __key_to_build__: dict[str, BuildValue] = {}
    
    @staticmethod
    def from_key(key: str) -> BuildValue:
        if Build.__key_to_build__ == {}:
            Build.__generate_key_to_build__()
        
        if key not in Build.__key_to_build__:
            return None
        
        return Build.__key_to_build__[key]
    
    @staticmethod
    def __generate_key_to_build__():
        Build.__key_to_build__ = {x.value.key: x.value for x in Build}

class ActionValue(NamedTuple):
    key: str | keyboard.Key | None
    delta_mouse_x: int
    delta_mouse_y: int
    
    
    
    def do(self):
        pyautogui.rightClick()
        print(self.delta_mouse_x, self.delta_mouse_y)
        pyautogui.move(self.delta_mouse_x, self.delta_mouse_y)
        pyautogui.leftClick()
        pyautogui.move(-self.delta_mouse_x, -self.delta_mouse_y)
    

class Action(Enum):
    BUILD = ActionValue(None, -82, 0)
    INFO = ActionValue('i', 0, -59)
    NAVAL_INVASION = ActionValue('n', 73, 0)
    ALLIANCE_OR_BETRAY = ActionValue('b', 0, 76)
        
    __key_to_action__: dict[str, ActionValue] = {}
    
    @staticmethod
    def from_key(key: str) -> ActionValue | None:
        if Action.__key_to_action__ == {}:
            Action.__generate_key_to_build__()
        
        if key not in Action.__key_to_action__:
            return None
        
        return Action.__key_to_action__[key]
    
    @staticmethod
    def __generate_key_to_build__():
        Action.__key_to_action__ = {x.value.key: x.value for x in Action if x.value.key is not None}