import cv2
import mediapipe as mp
import pyttsx3
import time
import logging

class PokeGestureSec:
    def __init__(self):
        self.logger = self.setup_logger()
        self.engine = pyttsx3.init()
        self.hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1)
        self.drawer = mp.solutions.drawing_utils
        self.last_gesture = ""
        self.last_trigger_time = 0
        self.gesture_actions = {
            "AJUDA": lambda: self.speak("Gesto de ajuda detectado."),
            "PAZ": lambda: self.speak("Sinal de paz."),
            "PUNHO": lambda: self.speak("Punho fechado, sem gesto visível.")
        }

    def setup_logger(self):
        logger = logging.getLogger("PokeGestureSec")
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler("pokegesturesec.log", mode='w')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def speak(self, text):
        self.logger.info(f"Voz: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def detect_gesture(self, landmarks):
        fingers = [False] * 5
        try:
            fingers[0] = landmarks[4].x < landmarks[3].x
            fingers[1] = landmarks[8].y < landmarks[6].y
            fingers[2] = landmarks[12].y < landmarks[10].y
            fingers[3] = landmarks[16].y < landmarks[14].y
            fingers[4] = landmarks[20].y < landmarks[18].y

            if fingers == [False, True, False, False, False]:
                return "AJUDA"
            elif fingers == [False, True, True, False, False]:
                return "PAZ"
            elif all(not f for f in fingers):
                return "PUNHO"
            else:
                return "DESCONHECIDO"
        except Exception as e:
            self.logger.error(f"Erro ao detectar gesto: {e}")
            return "ERRO"

    def draw_gesture_info(self, frame, gesture):
        cv2.putText(frame, f"Gesto: {gesture}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    def run(self, camera_index=0):
        self.logger.info("Iniciando o PokeGestureSec...")
        cap = cv2.VideoCapture(camera_index)
        if not cap.isOpened():
            self.logger.error("Erro ao abrir a câmera.")
            print("Erro: câmera não detectada.")
            return

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                self.logger.warning("Frame não capturado.")
                break

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb)

            if results.multi_hand_landmarks:
                for hand in results.multi_hand_landmarks:
                    self.drawer.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
                    gesture = self.detect_gesture(hand.landmark)

                    if gesture != self.last_gesture and (time.time() - self.last_trigger_time > 2):
                        self.last_gesture = gesture
                        self.last_trigger_time = time.time()
                        if gesture in self.gesture_actions:
                            self.gesture_actions[gesture]()
                        else:
                            self.logger.info(f"Gesto não reconhecido: {gesture}")

                    self.draw_gesture_info(frame, gesture)

            cv2.imshow("PokeGestureSec - Reconhecimento de Gestos", frame)
            if cv2.waitKey(1) & 0xFF == 27:
                self.logger.info("Encerrando execução.")
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = PokeGestureSec()
    app.run()
