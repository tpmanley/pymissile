import pywinusb.hid as hid
import time

class MissleLauncher(object):
	def __init__(self):
		self.dev = hid.HidDeviceFilter(vendor_id=0x0A81).get_devices()[0]
		self.dev.open()
		self.report = self.dev.find_output_reports()[0]
	
	def move(self, x, amount):
		for i in [0x40, 0x40, x]:
			self.report[0xffa10005] = i
			self.report.send()
		time.sleep(.06)
		for i in range(amount):
			self.report[0xffa10005] = 0x40
			self.report.send()
			time.sleep(.06)
		self.report[0xffa10005] = 0x20
		self.report.send()
		
	def close(self):
		self.dev.close()

if __name__ == "__main__":
	dev = MissleLauncher()
	dev.move(4, 10)
	time.sleep(1)
	dev.move(8, 10)
	time.sleep(1)
	dev.move(2, 10)
	time.sleep(1)
	dev.move(1, 10)
	dev.close()
