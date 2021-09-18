from pysubparser import parser

transcript = parser.parse()

timestamps = []
lines = []
for line in transcript:
    timestamps.append(str(line.start))
    lines.append(str(line))