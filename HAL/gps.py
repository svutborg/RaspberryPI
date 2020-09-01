from serial import Serial
S = Serial(port="/dev/ttyS0")
message = bytearray()

def decode_sentence(sent):
    result = {"type": "unknown"}
    sent = sent.decode("utf8")
    fragments = sent.split(',')
    if fragments[0][0:3] == "$GP": # GPS Message
        if "GGA" in fragments[0]:
            result["type"] = "GGA"
            result["name"] = "Fix information"
            result["timestamp"] = fragments[1]
            result["location"] = fragments[2:6]
            result["fix quality"] = fragments[6]
            result["number of satellites"] = fragments[7]
            result["horisontal dilution"] = fragments[8]
            result["altitude"] = fragments[9:11]
            result["height of geoid"] = fragments[11:13]
            result["checksum"] = fragments[14].strip("*\r\n")
        if "GLL" in fragments[0]:
            result["type"] = "GLL"
            result["name"] = "Geographic Latitude and Longitude"
            result["location"] = fragments[1:5]
            result["timestamp"] = fragments[5]
            result["active/void"] = fragments[6]
            result["checksum"] = fragments[7].strip("*\r\n")

    return result

try:
    while True:
        mes = decode_sentence(S.readline())
        #print(mes)
        if mes["type"] != "unknown":
            print(mes["location"])


finally:
    S.close()
