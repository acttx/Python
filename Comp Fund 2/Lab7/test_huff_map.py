from huffMap import HuffMap


def main():
    """
    This mainline code should follow the following algorithm:
    1. Create a HuffMap object for storing character counts.
     
    2. Read the FDREconomics.txt file. Concatenate each line 
       from the file into a string object using the read_file 
       method that you must code below.
         
    3. Loop through the string object, character-by-character, 
       to record the character frequencies in the string:
       First, You must check whether or not the character is
       already a key in the HuffMap.  
       a) If the character exists in the HuffMap, then obtain
          the HuffElement associated with the character and 
          increment the frequency count for the character. 
       b) If the character does not exist in the HuffMap, then
          create a new HuffElement for the character and 
          set the value of the count to one and add the new
          MapEntry to the HuffMap.
         
     4. Once you have read the whole file, you must retrieve 
        the set of characters (keys) from the HuffMap.
        Next, iterate through the key set: 
        a) For each character (key) found, get the corresponding 
           HuffElement and retrieve the frequency count for the 
           character.
        b) Print the character and the count.   
    
    """

    INPUT_FILE = "FDREconomics.txt"
    huff_map = HuffMap()
    string = read_file(INPUT_FILE)

    for ch in string:
        if not huff_map.contains_char(ch):
            huff_map.add_char(ch)
        else:
            huff_element = huff_map.get_huff_elem(ch)
            huff_element.inc_freq()

    key_set = huff_map.get_char_set()
    for key in key_set:
        huff_ele = huff_map.get_huff_elem(key)
        freq = huff_ele.get_freq()

        print('Char:', key, 'Count:', freq)


def read_file(filename):
    """
    Reads the input file into a String
    """
    file_str = ""
    with open(filename, 'r') as inputFile:
        file_str += "".join([lines.rstrip() for lines in inputFile])
    return file_str


main()
