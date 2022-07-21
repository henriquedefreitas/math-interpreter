class Token:
    def __init__(self, tag, buffer=''):
        self.tag = tag
        self.is_valued = False

        if tag == 'num':
            self.val = float(buffer)
            self.is_valued = True

    def get_tag(self):
        return self.tag

    def get_val(self):
        return self.val

    def has_value(self):
        return self.is_valued
