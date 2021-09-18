from pysubparser import parser

def srt_to_text(srt_path):
    lines = []
    transcript = parser.parse(srt_path)

    for line in transcript:
        lines.append(str(line))

    return '\n'.join(lines)
