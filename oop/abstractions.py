class Tv:

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def capture_signal(self):
        print("capture the signal")

    # interface method
    def process_signal(self, signal_type):
        self.capture_signal()

        print("signal process started")

        if signal_type == "volume_up":
            self.volume_up()

        print("signal process done")

    def volume_up(self):
        print("volume up")        


t1 = Tv()
t1.process_signal("volume_up")
t1.process_signal("volume_down")
