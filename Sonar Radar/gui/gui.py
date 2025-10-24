import serial
import time
import re
import math
import tkinter as tk

# ---- Serial setup ----
try:
    ser = serial.Serial('COM5', 9600, timeout=2)
    time.sleep(2)
except Exception as e:
    print("Error opening serial port:", e)
    exit()

# ---- Tkinter setup ----
root = tk.Tk()
root.title("ESP8266 Sonar Radar")
canvas_size = 500
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="black")
canvas.pack()

center = canvas_size // 2
radius = center - 40

# Radar background
for r in range(50, radius+1, 50):
    canvas.create_oval(center-r, center-r, center+r, center+r, outline="#006400", width=1)
canvas.create_line(center, 0, center, canvas_size, fill="#006400", width=1)
canvas.create_line(0, center, canvas_size, center, fill="#006400", width=1)

# Labels
angle_label = tk.Label(root, text="Angle: 0°", font=("Arial", 14), fg="lime", bg="black")
angle_label.pack()
distance_label = tk.Label(root, text="Distance: 0 cm", font=("Arial", 14), fg="lime", bg="black")
distance_label.pack()

# Data
data_points = []
current_angle = 0  # For smoothing
current_dist = 0

# ---- Update function ----
def update_radar():
    global data_points, current_angle, current_dist

    latest_angle = None
    latest_dist = None

    # Read only the **last available line** from serial
    while ser.in_waiting:
        try:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            match = re.search(r"angle:\s*(\d+).*distance:\s*([\d.]+)", line, re.IGNORECASE)
            if match:
                latest_angle = float(match.group(1))
                latest_dist = float(match.group(2))
        except:
            pass

    if latest_angle is not None and latest_dist is not None:
        # Smooth movement: interpolate previous -> new
        current_angle += (latest_angle - current_angle) * 0.2
        current_dist += (latest_dist - current_dist) * 0.2

        # Scale distance
        dist_scaled = min(current_dist, 100) * radius / 100
        data_points.append((current_angle, dist_scaled, time.time()))

        # Keep last 2 seconds
        now = time.time()
        data_points[:] = [(a,d,t) for a,d,t in data_points if now - t < 2]

        # Update labels
        angle_label.config(text=f"Angle: {current_angle:.1f}°")
        distance_label.config(text=f"Distance: {current_dist:.1f} cm")

    # Draw
    canvas.delete("beam")
    canvas.delete("dots")
    if data_points:
        a, d, _ = data_points[-1]
        rad = math.radians(a - 90)
        x = center + d * math.cos(rad)
        y = center + d * math.sin(rad)
        canvas.create_line(center, center, x, y, fill="#00FF00", width=2, tags="beam")

        now = time.time()
        for a,d,t in data_points:
            fade = int(255 * (1 - (now - t)/2))
            fade = max(0, min(255, fade))
            color = f'#00{fade:02x}00'
            radp = math.radians(a - 90)
            xp = center + d * math.cos(radp)
            yp = center + d * math.sin(radp)
            canvas.create_oval(xp-4, yp-4, xp+4, yp+4, fill=color, outline="", tags="dots")

    root.after(100, update_radar)  # slower update for visibility

# Start
update_radar()
root.mainloop()
ser.close()
