from directkeys import W, A, S, D
from directkeys import PressKey, ReleaseKey

class Control:
    current_key_pressed = set()

    def startControlling(self,distance,slope):
        keyPressed = False
        keyPressed_lr = False
        recentKey = None

        if 120 <= distance <= 220:
            PressKey(W)
            recentKey = W
            print('Press W')
            keyPressed = True
            self.current_key_pressed.add(W)
        elif 20 <= distance <= 115:
            PressKey(S)
            recentKey = S
            print('Press S')
            keyPressed = True
            self.current_key_pressed.add(S)

        if -0.41 < slope < -0.25:
            PressKey(A)
            print('Press <--')
            self.current_key_pressed.add(A)
            keyPressed = True
            keyPressed_lr = True
        elif 0.15 < slope < 0.40:
            PressKey(D)
            print('Press -->')
            self.current_key_pressed.add(D)
            keyPressed = True
            keyPressed_lr = True

        if keyPressed:
            if recentKey == W and S in self.current_key_pressed:
                self.current_key_pressed.remove(S)
                ReleaseKey(S)

            elif recentKey == S and W in self.current_key_pressed:
                self.current_key_pressed.remove(W)
                ReleaseKey(W)

        if not keyPressed and len(self.current_key_pressed) != 0:
            for key in self.current_key_pressed:
                ReleaseKey(key)
                print('Release')
            self.current_key_pressed = set()

        if not keyPressed_lr and ((A in self.current_key_pressed) or (D in self.current_key_pressed)):
            if A in self.current_key_pressed:
                ReleaseKey(A)
                self.current_key_pressed.remove(A)
            elif D in self.current_key_pressed:
                ReleaseKey(D)
                self.current_key_pressed.remove(D)