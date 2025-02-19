from flask import Flask, jsonify
from scapy.all import sniff
import threading

app = Flask(__name__)

# Store captured packets
captured_packets = []

def packet_callback(packet):
    packet_info = {
        "src": packet[0].src if hasattr(packet[0], 'src') else "Unknown",
        "dst": packet[0].dst if hasattr(packet[0], 'dst') else "Unknown",
        "protocol": packet[0].name if hasattr(packet[0], 'name') else "Unknown",
    }
    captured_packets.append(packet_info)

# Start packet sniffing in a separate thread
def start_sniffing():
    sniff(prn=packet_callback, store=False)

threading.Thread(target=start_sniffing, daemon=True).start()

@app.route('/get_packets', methods=['GET'])
def get_packets():
    return jsonify(captured_packets)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
