# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PickupLines(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, player_id: int=None, round_num: int=None, earned_swipes_left: str=None, earned_swipes_right: str=None, human_words: str=None, robot_words: str=None):  # noqa: E501
        """PickupLines - a model defined in Swagger

        :param player_id: The player_id of this PickupLines.  # noqa: E501
        :type player_id: int
        :param round_num: The round_num of this PickupLines.  # noqa: E501
        :type round_num: int
        :param earned_swipes_left: The earned_swipes_left of this PickupLines.  # noqa: E501
        :type earned_swipes_left: str
        :param earned_swipes_right: The earned_swipes_right of this PickupLines.  # noqa: E501
        :type earned_swipes_right: str
        :param human_words: The human_words of this PickupLines.  # noqa: E501
        :type human_words: str
        :param robot_words: The robot_words of this PickupLines.  # noqa: E501
        :type robot_words: str
        """
        self.swagger_types = {
            'player_id': int,
            'round_num': int,
            'earned_swipes_left': str,
            'earned_swipes_right': str,
            'human_words': str,
            'robot_words': str
        }

        self.attribute_map = {
            'player_id': 'player_id',
            'round_num': 'round_num',
            'earned_swipes_left': 'earned_swipes_left',
            'earned_swipes_right': 'earned_swipes_right',
            'human_words': 'human_words',
            'robot_words': 'robot_words'
        }

        self._player_id = player_id
        self._round_num = round_num
        self._earned_swipes_left = earned_swipes_left
        self._earned_swipes_right = earned_swipes_right
        self._human_words = human_words
        self._robot_words = robot_words

    @classmethod
    def from_dict(cls, dikt) -> 'PickupLines':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The pickup_lines of this PickupLines.  # noqa: E501
        :rtype: PickupLines
        """
        return util.deserialize_model(dikt, cls)

    @property
    def player_id(self) -> int:
        """Gets the player_id of this PickupLines.


        :return: The player_id of this PickupLines.
        :rtype: int
        """
        return self._player_id

    @player_id.setter
    def player_id(self, player_id: int):
        """Sets the player_id of this PickupLines.


        :param player_id: The player_id of this PickupLines.
        :type player_id: int
        """

        self._player_id = player_id

    @property
    def round_num(self) -> int:
        """Gets the round_num of this PickupLines.


        :return: The round_num of this PickupLines.
        :rtype: int
        """
        return self._round_num

    @round_num.setter
    def round_num(self, round_num: int):
        """Sets the round_num of this PickupLines.


        :param round_num: The round_num of this PickupLines.
        :type round_num: int
        """

        self._round_num = round_num

    @property
    def earned_swipes_left(self) -> str:
        """Gets the earned_swipes_left of this PickupLines.


        :return: The earned_swipes_left of this PickupLines.
        :rtype: str
        """
        return self._earned_swipes_left

    @earned_swipes_left.setter
    def earned_swipes_left(self, earned_swipes_left: str):
        """Sets the earned_swipes_left of this PickupLines.


        :param earned_swipes_left: The earned_swipes_left of this PickupLines.
        :type earned_swipes_left: str
        """

        self._earned_swipes_left = earned_swipes_left

    @property
    def earned_swipes_right(self) -> str:
        """Gets the earned_swipes_right of this PickupLines.


        :return: The earned_swipes_right of this PickupLines.
        :rtype: str
        """
        return self._earned_swipes_right

    @earned_swipes_right.setter
    def earned_swipes_right(self, earned_swipes_right: str):
        """Sets the earned_swipes_right of this PickupLines.


        :param earned_swipes_right: The earned_swipes_right of this PickupLines.
        :type earned_swipes_right: str
        """

        self._earned_swipes_right = earned_swipes_right

    @property
    def human_words(self) -> str:
        """Gets the human_words of this PickupLines.


        :return: The human_words of this PickupLines.
        :rtype: str
        """
        return self._human_words

    @human_words.setter
    def human_words(self, human_words: str):
        """Sets the human_words of this PickupLines.


        :param human_words: The human_words of this PickupLines.
        :type human_words: str
        """

        self._human_words = human_words

    @property
    def robot_words(self) -> str:
        """Gets the robot_words of this PickupLines.


        :return: The robot_words of this PickupLines.
        :rtype: str
        """
        return self._robot_words

    @robot_words.setter
    def robot_words(self, robot_words: str):
        """Sets the robot_words of this PickupLines.


        :param robot_words: The robot_words of this PickupLines.
        :type robot_words: str
        """

        self._robot_words = robot_words
