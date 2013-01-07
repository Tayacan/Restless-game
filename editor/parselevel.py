from obstacles import Box

class Parser:
    @staticmethod
    def parse(text,screen):
        tokens = text.split(" ")
        if tokens[0].lower() == "box":
            x = int(tokens[1])
            y = int(tokens[2])
            w = int(tokens[3])
            h = int(tokens[4])
            return Box(screen,(x,y),(w,h))

