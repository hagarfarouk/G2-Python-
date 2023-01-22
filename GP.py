### simulation code for a Node That receives from UART port then check and analyz the frame to generates
### the data in array and generates a CAN frame from it and then resending occure

import serial
import tkinter as tk

def receive_uart_frame():
    # Open the serial port
    ser = serial.Serial("COM3", baudrate=9600, timeout=1)

    # Read data from the UART
    data = ser.readline()

    # Convert the data to an array
    data_array = list(data)

    return data_array

def analyze_uart_frame(data_array):
    # Analyze all parts of the frame
    start_byte = data_array[0]
    payload = data_array[1:-2]
    checksum = data_array[-2]
    end_byte = data_array[-1]

    # Check the checksum
    calculated_checksum = 0
    for i in payload:
        calculated_checksum += i
    if checksum == calculated_checksum:
        # Checksum is valid
        print("Checksum is valid")
    else:
        # Checksum is invalid
        print("Checksum is invalid")

    # Check the frame of the data
    if start_byte == 0x01 and end_byte == 0x04:
        # Frame is valid
        print("Frame is valid")
        return payload
    else:
        # Frame is invalid
        print("Frame is invalid")
        return None
		
def create_can_frame(data_array):
    # Set the CAN ID, DLC, arbitration field and ACK field
    can_id = 0x123
    can_dlc = len(data_array)
    arbitration_field = 0x00
    ack_field = 0x00

    # Create the complete CAN frame
    can_frame = bytearray(can_dlc + 6)
    can_frame[0] = can_id & 0xFF
    can_frame[1] = (can_id >> 8) & 0xFF
    can_frame[2] = can_dlc
    can_frame[3] = arbitration_field
    can_frame[4] = ack_field
    for i in range(can_dlc):
        can_frame[5 + i] = data_array[i]
        
    # Calculate the CAN CRC
    crc = 0xFFFF
    for i in range(len(can_frame)):
        crc = crc ^ can_frame[i]
        for _ in range(8):
            if crc & 0x0001:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc = crc >> 1
    can_frame[5+can_dlc] = crc & 0xFF
    can_frame[5+can_dlc+1] = (crc >> 8) & 0xFF
    return can_frame

def send_can_frame(can_frame):
    # Open a serial connection
    ser = serial.Serial()
    ser.port = "/dev/ttyUSB0"
    ser.baudrate = 125000
    ser.open()

    # Send the CAN frame
    ser.write(can_frame)

    # Close the serial connection
    ser.close()

# GUI code
root = tk.Tk()
root.title("UART-CAN Simulation")

# Received data label
received_data_label = tk.Label(root, text="Received Data: ")
received_data_label.pack()

# Received data textbox
received_data_textbox = tk.Text(root, height=5, width=50)
received_data_textbox.pack()



# Analyze button
def on_analyze_button_click():
    data_array = receive_uart_frame()
    received_data_textbox.insert("1.0", data_array)
    payload = analyze_uart_frame(data_array)
    if payload != None:
        print("Payload: ", payload)

# Create and send button
def on_create_and_send_button_click():
    data_string = data_entry.get()
    data_array = list(map(int, data_string.split(',')))
    can_frame = create_can_frame(data_array)
    send_can_frame(can_frame)	
	
analyze_button = tk.Button(root, text="Analyze", command=on_analyze_button_click)
analyze_button.pack()

create_and_send_button = tk.Button(root, text="Create and Send", command=on_create_and_send_button_click)
create_and_send_button.pack()
root.mainloop()

