original = open("BuiltInVariables_OG.txt", "r")
docs = open("Docs.txt", "a")
output = open("BuiltInVariables.txt","w+")

running = True
while running:
    group = input('What group would you like the variable / function to be in?: ')
    name = input('Enter the name of the object. If it\'s a function, put its parameters: ')
    desc = input('Enter description: ')

    newDoc = "Diego\'s Custom Library,  %s,  V2,  feat_NaturalLanguageInActive,    noFeatRest,       F, B,   %s; // %s" % (group, name, desc)

    docs.write(newDoc + '\n\n')

    choice = input("Got it! Is that all? (Y / N)")
    running = choice.lower() != 'y'
    print("\n")

docs.close()
rDocs = open("Docs.txt", "r")

for line in original:
    output.write(line)

for line in rDocs:
    output.write(line)

rDocs.close()
original.close()