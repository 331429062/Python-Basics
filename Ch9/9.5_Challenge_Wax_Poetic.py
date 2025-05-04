import random
nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "bounces", "slurps", "meows", "explodes", "curdles"]
adj = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

def poem ():

    n1= random.choice(nouns)
    n2= random.choice(nouns)
    n3= random.choice(nouns)
    
    if n1 == n2:
        n2 = random.choice(nouns)
    elif n1 == n3:
        n1 = random.choice(nouns)
    
    v1 = random.choice(verbs)
    v2 = random.choice(verbs)
    v3 = random.choice(verbs)

    if v1 == v2:
        v2 = random.choice(verbs)
    elif v1 == v3:
        v1 = random.choice(verbs)

    adj1 = random.choice(adj)
    adj2 = random.choice(adj)
    adj3 = random.choice(adj)

    if adj1 == adj2:
        adj2 = random.choice(adj)
    elif adj1 == adj3:
        adj1 = random.choice(adj)

    perp1 = random.choice(prepositions)
    perp2 = random.choice(prepositions)

    if perp1 == perp2:
        perp2 = random.choice(prepositions)

    adverb1= random.choice(adverbs)

    if "aeiou".find(adj1[0]) != -1:  # First letter is a vowel
        article = "An"
    else:
        article = "A"

    print(f"""{article} {adj1} {n1}

{article} {adj1} {n1} {v1} {perp1} the {adj2} {n2}
{adverb1}, the {n1} {v2}
the {n2} {v3} {perp2} a {adj3} {n3} \n""")
    

poem()


