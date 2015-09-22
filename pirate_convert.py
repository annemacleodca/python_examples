import urllib

# define function to read input english text and output pirate translated text

def read_text():
    input_file = open("text_to_translate.txt")
    file_contents = input_file.read()
    print("Original text: "+file_contents)
    input_file.close()
    convert_to_pirate(file_contents)

# convert english text into pirate translated text

def convert_to_pirate(text_to_convert):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_convert)
    pirate_output = connection.read()
    print("Pirate translation: "+pirate_output)
    connection.close()
  

read_text()
