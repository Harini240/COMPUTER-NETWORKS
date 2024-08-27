import random

def receive_ack():
    return random.choice([True, False]) 

def stop_and_wait(frames):
    print("Stop-and-Wait Protocol:")
    for frame in frames:
        sent = False
        while not sent:
            print(f"Sending: {frame}")
            if receive_ack():
                print(f"ACK received for {frame}")
                sent = True
            else:
                print(f"No ACK for {frame}, resending...")

def sliding_window(frames, window_size):
    print("\nSliding Window Protocol:")
    window_start = 0
    total_frames = len(frames)
    
    while window_start < total_frames:
        print("Sending frames:", end=" ")
        for i in range(window_start, min(window_start + window_size, total_frames)):
            print(frames[i], end=" ")
        print()
        ack_count = random.randint(1, min(window_size, total_frames - window_start))
        print(f"ACKs received for {ack_count} frame(s)")
        window_start += ack_count

frames = ["Frame1", "Frame2", "Frame3", "Frame4", "Frame5"]
stop_and_wait(frames)
window_size = 3
sliding_window(frames, window_size)
