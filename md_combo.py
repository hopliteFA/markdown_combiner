

def append_file(input_name, output_file):
    content = ''
    with open(input_name, 'r') as file_in:
        content = file_in.read()
    with open(output_file, 'a') as file_out:
        file_out.write(content)

def get_file_list(input_file):
    with open(input_file, 'r') as f:
        file_list = f.read().splitlines()
    return file_list 

def combo(input_file, output_file):
    file_list = get_file_list(input_file)
    for line in file_list:
        append_file(line, output_file)

print("running the combiner")
combo("content.txt", 'ouput.md')
