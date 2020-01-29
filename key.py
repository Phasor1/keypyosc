from pynput.keyboard import Key, Listener
from pythonosc import udp_client, osc_message_builder

IP = '127.0.0.1'
PORT = 12345
client = udp_client.SimpleUDPClient(IP, PORT)
# on address /keyboard set a prefix equal to the name of the coder

# callback of pressing a key
def on_press(key):
	msg = osc_message_builder.OscMessageBuilder(address = '/keyboard')
	msg.add_arg(str(key))
	msg = msg.build()
	client.send(msg)



# Collect events until released
print("starting keyboard thread")
with Listener(
        on_press=on_press) as listener:
    listener.join()