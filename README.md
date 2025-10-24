#                                                                                              Sonar Radar  
(ESP8266 + Ultrasonic + Python GUI)

This project is a  **Sonar Radar Game** using an **ESP8266 (NodeMCU)**, **Ultrasonic Sensor**, and **Servo Motor**.  
The system scans the environment and visualizes detected objects in real-time using a **Python-based radar GUI**.

---

## 🚀 Features

- Real-time distance scanning using an ultrasonic sensor  
- Servo motor rotation for a sweeping radar motion  
- Serial communication between ESP8266 and Python GUI  
- Radar-style visualization using **Tkinter**  
- Smooth animation and fading detection effect  

---

## 🧩 Components Required

- ESP8266 / NodeMCU board  
- Ultrasonic Sensor (HC-SR04)  
- Servo Motor (SG90 or MG90S)  
- Breadboard  
- Jumper Wires  
- USB Cable  
- Laptop / PC (for Python visualization)  

---

## 🛠️ Software & Tools Required

- **Arduino IDE** (for uploading ESP8266 code)  
  - [Download Arduino IDE](https://www.arduino.cc/en/software)
- **Python 3** (for running GUI)  
  - Install via terminal:
    ```bash
    sudo apt install python3 python3-pip
    ```
- **Python Libraries:**
    ```bash
    pip install pyserial tkinter
    ```

---

## ⚙️ Circuit Connections

| Component Pin | ESP8266 Pin |
|----------------|-------------|
| HC-SR04 Trig   | D5          |
| HC-SR04 Echo   | D6          |
| Servo Signal   | D4          |
| VCC (Sensor & Servo) | 5V or 3.3V (depending on model) |
| GND            | GND         |

---

## 💻 Code Files

### **1️⃣ sonar_esp8266.ino**
Arduino code for controlling the servo and ultrasonic sensor.  
Sends angle and distance data via serial to the Python GUI.

### **2️⃣ sonar_gui.py**
Python GUI that reads serial data and displays a radar visualization.  
Includes fading effect for scanned objects and angle/distance display.

---

## ▶️ How to Run

1. **Upload Arduino Code**
   - Open `sonar_esp8266.ino` in Arduino IDE  
   - Select **NodeMCU 1.0 (ESP-12E Module)** board  
   - Choose correct **COM port**  
   - Click **Upload**

2. **Run Python GUI**
   - Connect NodeMCU to laptop  
   - Check the serial port (e.g., `COM5` or `/dev/ttyUSB0`)  
   - Open terminal and run:
     ```bash
     python3 sonar_gui.py
     ```

3. **Enjoy the Live Radar!**
   - Watch the radar beam sweep and detect nearby objects in real time.  

---

## ⚠️ Troubleshooting

- **No serial data?**
  - Check the correct COM port in Python script.  
  - Make sure baud rate (`9600`) matches in both Arduino and Python code.  
- **Servo not rotating?**
  - Check servo wiring and power supply.  
- **GUI not opening?**
  - Ensure `tkinter` and `pyserial` are installed.

---

## 🧠 Further Exploration

- Add buzzer feedback for close-range alerts  
- Log distance data for mapping  
- Convert to 3D radar using multiple sensors  

---

---

