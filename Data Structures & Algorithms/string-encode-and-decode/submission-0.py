class Solution:

    def encode(self, strs: List[str]) -> str:
    #loop through the words, count the letters and concatonate length*word
        encoded_string = ""
        for i in strs:
            count = len(i)
            encoded_string = encoded_string + str(count) + "*" + i
        return encoded_string

    def decode(self, s: str) -> List[str]:
        #two pointers, one at start, one at *, 
        #then count the number of words and update
        decoded_strs = []
        i = 0
        
        # We use a while loop because 'i' will jump dynamically
        while i < len(s):
            j = i
            # Move j forward until it finds the asterisk
            while s[j] != "*":
                j += 1
            
            # Grab the number before the asterisk and convert to int
            freq = int(s[i:j])
            
            # Slice the exact word out (no inner loop needed!)
            word = s[j + 1 : j + 1 + freq]
            decoded_strs.append(word)
            
            # Move 'i' to the start of the next number token
            i = j + 1 + freq
        return decoded_strs

