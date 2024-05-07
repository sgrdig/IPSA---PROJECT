import tkinter as tk
import math
import random
from easygopigo3 import EasyGoPiGo3


#Project with the fisrt purpose to do a robot that with a lidar is capable of "seeing the object and enable the controller to move without collide by forking the process"
W = 542
H = 542

gpg = EasyGoPiGo3()
value = 90
# Initialisez le capteur de distance
my_distance_sensor = gpg.init_distance_sensor()

# Initialisez le servo
servo = gpg.init_servo()
servo.rotate_servo(value)

Radar = tk.Tk()
canvas = tk.Canvas(Radar, width=W, height=H, borderwidth=0, highlightthi=0, bg="black")
canvas.grid()

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)

tk.Canvas.create_circle = _create_circle

def draw():
    for i in range(6):
        canvas.create_oval(W / 2 - (45 + i * 45), H / 2 - (45 + i * 45), W / 2 + (45 + i * 45), H / 2 + (45 + i * 45), outline="green", width=1)

    canvas.create_line(W / 2, 0, W / 2, H, fill="green")
    canvas.create_line(0, H / 2, W, H / 2, fill="green")

def go():
    
    distance = my_distance_sensor.read_mm()
    lidar_angle = value

    draw_Radar(W / 2, H / 2)
    if distance < 3000:
        draw_obstacle(W / 2, H / 2, distance, lidar_angle)
    else:
        canvas.delete("obstacle")

def draw_Radar(x_center, y_center):
    canvas.delete("Radar")
    canvas.create_circle(x_center, y_center, 3, fill="red", outline="", tags="Radar")

def draw_obstacle(x_center, y_center, distance, lidar_angle):
    # Convertir l'angle du LiDAR en radians
    lidar_angle_radians = math.radians(lidar_angle)

    # Longueur du rayon du LiDAR (représentant la distance à l'obstacle)
    lidar_radius = distance / 5

    # Coordonnées de départ du rayon du LiDAR
    x_start_lidar = x_center
    y_start_lidar = y_center

    # Coordonnées de fin du rayon du LiDAR
    x_end_lidar = x_center + lidar_radius * math.cos(lidar_angle_radians)
    y_end_lidar = y_center - lidar_radius * math.sin(lidar_angle_radians)

    # Dessiner le point représentant l'obstacle
    canvas.create_circle(x_end_lidar, y_end_lidar, 3, fill="blue", outline="", tags="obstacle")

def animate():
    draw()
    go()
    Radar.after(100, animate)

# Lancez l'animation
animate()

Radar.wm_title("Radar de détection d'obstacles")
Radar.mainloop()
#_____________________________________________________________________________________________________________________________________________________
#combine moi les deux codes et donne le code complet combiné : from easygopigo3 import EasyGoPiGo3
#_____________________________________________________________________________________________________________________________________________________
import time
import sys

# Initialize the EasyGoPiGo3 instance
gpg = EasyGoPiGo3()

# Global position variables
x = 0
y = 0
i = 0
angle_rotation = 0  # Global variable for tracking rotation

# Constants for wheel and movement calculations
wheel_diameter = 66.5  # Diameter of the wheel in mm
wheel_circumference = 3.14159 * wheel_diameter  # Circumference in mm
ticks_per_revolution = 360  # Number of encoder ticks per wheel revolution

def get_distance_from_ticks(ticks):
    """Convert encoder ticks to distance in mm."""
    return ticks * (wheel_circumference / ticks_per_revolution)

def move_fixed_distance(distance, direction):
    global x, y, angle_rotation  # Use global position and angle variables

    def modulo_180(angle):
        """Wrap angle between 0 and 179 degrees."""
        return angle % 180

    start_encoders = gpg.read_encoders()
    
    if direction == 'forward':
        gpg.forward()
    elif direction == 'backward':
        gpg.backward()
    
    while True:
        current_encoders = gpg.read_encoders()
        if direction == 'forward':
            distance_moved = get_distance_from_ticks(current_encoders[1] - start_encoders[1])
        else:
            distance_moved = get_distance_from_ticks(start_encoders[1] - current_encoders[1])

        if distance_moved >= distance:
            gpg.stop()
            break
        time.sleep(0.1)

    # Update position based on direction and rotation
    if direction == 'forward' or direction == 'backward':
        if modulo_180(angle_rotation) == 0:  # Assumes 0 is east and 90 is north
            x += distance if direction == 'forward' else -distance
        elif modulo_180(angle_rotation) == 90:
            y += distance if direction == 'forward' else -distance

def turn(direction):
    def modulo_180(angle):
        """Wrap angle between 0 and 179 degrees."""
        return angle % 180
    global angle_rotation
    if direction == 'left':
        angle_rotation += 90
        gpg.turn_degrees(-90)
    elif direction == 'right':
        angle_rotation -= 90
        gpg.turn_degrees(90)
    angle_rotation = modulo_180(angle_rotation)

def main():
    print("Voltage: {}".format(gpg.volt()))
    print("Speed: {}".format(gpg.get_speed()))
    print("Encoders: {}".format(gpg.read_encoders()))
    print("Current angle: {}".format(angle_rotation))
    print("Position: (x={}, y={})".format(x, y))

    while True:
        command = input("Enter your command (z for forward, s for backward, q for left, d for right, p to stop): ").strip().lower()
        if command == 'z':
            move_fixed_distance(100, 'forward')
        elif command == 's':
            move_fixed_distance(100, 'backward')
        elif command == 'q':
            turn('left')
        elif command == 'd':
            turn('right')
        elif command == 'p':
            print('x :',x)
            print('y:',y)
            
            while angle_rotation != 0 :
                angle_rotation -= 90
                gpg.turn_degrees(-90)
            while i != x :
                if x < 0 :
                    i-= 100
                elif x > 0 :
                    i+= 100
                elif x == 0 :
                    break
            print("Stopping and exiting...")
            sys.exit()

if __name__ == "__main__":
    main()
