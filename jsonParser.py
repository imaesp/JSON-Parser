import json


def convert_to_array_format(input_file, output_file):
   with open(input_file, 'r') as infile:

       data = []

       for line in infile:
           line = line.strip() 
           if line: 
               try:
   
                   data.append(json.loads(line))
               except json.JSONDecodeError as e:
                   print(f"Error decoding JSON: {e}")

   with open(output_file, 'w') as outfile:
       json.dump(data, outfile, indent=4)


convert_to_array_format('.json', '.json')
print("Parsing Done!")

