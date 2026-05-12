# Given sentence
sentence = """The/DT planet/NN Jupiter/NNP and/CC its/PPS moons/NNS are/VBP in/IN effect/NN a/DT minisolar/JJ system/?? ,/, and/CC Jupiter/NNP itself/PRP is/VBZ often/RB called/VBN a/DT star/?? that/IN never/RB caught/??? fire/NN ./."""

# Fill missing tags based on context
sentence = sentence.replace("system/??", "system/NN")
sentence = sentence.replace("star/??", "star/NN")
sentence = sentence.replace("caught/???", "caught/VBN")

# Print final answer
print(sentence)



# Given sentence
sentence = "People/NNS continue/VBP to/TO inquire/VB the/DT reason/?? for/IN the/DT race/NN for/IN outer/JJ space/??"

# Fill missing tags based on context
sentence = sentence.replace("reason/??", "reason/NN")
sentence = sentence.replace("space/??", "space/NN")

# Print final answer
print(sentence)