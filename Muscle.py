class Muscle():
    def __init__(self,name,req,cur):
        """Create a muscle object

        Args:
            name (str): Muscle name
            req (int): Required rest
            cur (int): Current rest
        """
        self.name = name
        self.req = req
        self.cur = cur

    def tick(self):
        """Ticks days and resets to 1 when ready
        """
        #interactions will change this
        if self.cur + 1 < self.req:
            self.cur += 1 
        else:
            self.cur = 1
