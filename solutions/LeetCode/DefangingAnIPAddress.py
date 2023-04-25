class Solution(object):
    def defangIPaddr(self, address):
        ls_address = list(address)
        str_address = ""
        for i in ls_address:
            if i == ".":
               i = "[.]"
            str_address += i
        return str_address
