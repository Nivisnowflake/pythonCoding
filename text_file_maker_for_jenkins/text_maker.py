default_content = open('default_content_file', 'r')

filename = f'{input("Enter a filename to create .properties file (default content set inside the code):")}.properties'
first_line = input("Enter data for first line in file:")

file_create = open(filename, "w")

content = default_content.read()

file_create.write(f'LOREM={first_line}(\\"ASD\\")\n{content}')

file_create.close()
