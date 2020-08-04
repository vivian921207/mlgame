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
            direction = self.getDirection(self.previous_ball, current_ball)

            predict = 100
            if direction <= 2:  # 球正在往上不判斷落點
                pass
            else:  # 球正在往下，判斷球的落點
                # 2.Predict Falling X
                predict = self.predictFalling_x(self.previous_ball, current_ball)
                # 判斷command

            # 3.Return Command
            command = self.getCommand(scene_info["platform"][0], predict)

        self.previous_ball = current_ball
        return command

    def getDirection(self, previous_ball, current_ball):
        if previous_ball[0]-current_ball[0]>0:
            if previous_ball[1]>current_ball[1]>0:
                return 2
            else :
                return 3
        else:
            if previous_ball[1]>current_ball[1]>0:
                return 1
            else :
                return 4
        """
        result
        1 : top right
        2 : top left
        3 : bottom left
        4 : bottom right
        """

        # TODO
        return 3

    def predictFalling_x(self,previous_ball, current_ball):
        x1=previous_ball[0]
        x2=current_ball[0]
        y1=previous_ball[1]
        y2=current_ball[1]
        if (y1-y2)!=0:
            a=(x1-x2)/(y1-y2)
        else:
            a=0
        if a<0:
            y=y1-a*x1
            if y>=400:
                x=x1-(y1-400)/a
            else:
                x=(y-400)*a
            return x
        elif a==0:
            return x2
        else:
            y=y1-a*(x1-200)
            if y>=400:
                x=x1-(y1-400)/a
            else:
                x=(y-400)*(a)+200
            return x


    def getCommand(self, platform_x, predict_x):
        """
        return "MOVE_LEFT", "MOVE_RIGHT" or "NONE"
        """
        if platform_x>predict_x:
            return "MOVE_LEFT"
        elif platform_x<predict_x:
            return "MOVE_RIGHT"
        else:
            return "NONE"
        # TODO

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
