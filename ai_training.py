# ai_training.py
import threading
import time
import random
import numpy as np

class AIAgent:
    def __init__(self):
        self.q_table = np.zeros((5, 5))  # Contoh Q-table sederhana
    
    def train(self, episodes=1000, learning_rate=0.1, discount_factor=0.9):
        for episode in range(episodes):
            state = random.randint(0, 4)  # Mulai di posisi acak
            for _ in range(100):  # Maksimum langkah per episode
                action = random.choice([0, 1])  # Contoh tindakan
                next_state = (state + action) % 5
                reward = 1 if next_state == 4 else 0
                
                # Update Q-table
                self.q_table[state, action] = (1 - learning_rate) * self.q_table[state, action] + \
                                              learning_rate * (reward + discount_factor * np.max(self.q_table[next_state]))
                state = next_state
                time.sleep(0.01)  # Simulasi waktu pelatihan
    
    def get_q_table(self):
        return self.q_table

def start_training():
    agent = AIAgent()
    training_thread = threading.Thread(target=agent.train)
    training_thread.start()
    return agent
