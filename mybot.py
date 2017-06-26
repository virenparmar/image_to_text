import aiml
import os

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")


os.system("tesseract ziyaad2.png out2")

with open("out2.txt") as f:
	for line in f:
		ans = kernel.respond(line)
		print ans
		os.system("espeak '%s'" % ans)
	
