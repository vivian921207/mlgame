"""
The template of the main script of the machine learning process
"""
import random


class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.previous_ball = (0, 0)

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
                scene_info["status"] == "GAME_PASS"):
            return "RESET"
        current_ball = scene_info["ball"]
        if not self.ball_served:

            self.ball_served = True
            command = random.choice(["SERVE_TO_RIGHT", "SERVE_TO_LEFT"])  # 發球
        else:
            # 1.Find Direction
            direction = self.getDirection(
                self.previous_ball, current_ball)

            predict = 100
            if direction <= 2:  # 球正在往上不判斷落點
                pass
            else:  # 球正在往下，判斷球的落點
                # 2.Predict Falling X
                predict = self.predictFalling_x(
                    self.previous_ball, current_ball)
                # 判斷command

            # 3.Return Command
            command = self.getCommand(
                scene_info["platform"][0], predict)

        self.previous_ball = current_ball
        return command

    def getDirection(self, previous_ball, current_ball):
        """
        result
        1 : top right
        2 : top left
        3 : bottom left
        4 : bottom right
        """
        # TODO
        return 3

    def predictFalling_x(self, previous_ball, current_ball):
        # TODO
        return 100

    def getCommand(self, platform_x, predict_x):
        """
        return "MOVE_LEFT", "MOVE_RIGHT" or "NONE"
        """
        # TODO
        return "MOVE_RIGHT"

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
