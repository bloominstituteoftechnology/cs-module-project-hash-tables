class Solution(object):
    def isValid(self, s):
        """     
        :type s: str
        :rtype: bool
        """
        # given a string of just parentheses
        # go through the string 
        # keep track if something is the correct closing parentheses
        # O(N) where n is the length of the string
        # {[]} this is the correct one to get to
        # map the opening ones and map the closing ones

        stack = []
        
        par_mapping = {"}" : "{", "]" : "[", ")" : "("}

        # Use a stack
        # push opening brackets onto the stack
        # if I encounter closing bracket, pop most recent off the stack
        # check if they match, if so return true, if not return false

        # examples: ( ) [ ] { }

        for p in s:
            if p in par_mapping:
                if len(stack) == 0:
                    return False
                most_recent = stack.pop()
                if par_mapping[p] != most_recent:
                    return False

            else:
                stack.append(p)

        if len(stack) != 0:
            return False

        return True
