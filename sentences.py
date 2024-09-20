import random

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else :
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # Randomly choose and return a noun.
    word = random.choice(words)
    return word


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    
    # Randomly choose and return a preposition.
    preposition = random.choice(prepositions)
    return preposition
    

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or plural.
    Return: a prepositional phrase.
    """

    prepos_phrase = get_preposition() + " " + get_determiner(quantity) + " " + get_noun(quantity)

    return prepos_phrase


def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjectives:
        "fast", "smart", "beautiful", "gifted", "healthy",
        "hilarius", "lucky", "perfect", "successful", "kind", "mysterius", "happy",
        "delightful", "busy", "crazy", "scary", "thankful", "tired", "hungry" 

    Return: a randomly chosen adjective.
    """
    adjectives = ["beautiful", "busy", "crazy", "delightful", "fast", "gifted", "happy", "healthy", "hilarius", "hungry", "kind", "lucky", "mysterius", "perfect", "successful", "scary", "smart", "tired", "thankful"]

    # Randomly choose and return an adjective.
    adjective = random.choice(adjectives)
    return adjective


def get_adverb():
    """Return a randomly chosen adverb
    from this list of adverbs:
        "always", "never", "unexpectedly", "stupidly", "sadly", "nicely", "obediently", "seriously", "awkwardly", "arrogantly"
        "naturally", "mysteriously", "innocently", "freely", "furiously", "elegantly" "correctly", "cautiously", "curiously".

    Return: a randomly chosen adverb
    """
    adverbs = ["always", "never", "unexpectedly", "stupidly", "sadly", "nicely", "obediently", "seriously", "awkwardly", "arrogantly", "naturally", "mysteriously", "innocently", "freely", "furiously", "elegantly", "correctly", "cautiously", "curiously"]

    # Randomly choose and return an adverb
    adverb = random.choice(adverbs)
    return adverb


def get_sentence(quantity, tense):
    """Call the get_determiner, get_noun, get_verb, get_adjective, get_prepositional_phrase and return a full sentence 
        containing an article, noun, verb, adjective and prepositional phrase.
        Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
        
        Return: a setence.
        """
    sentence = f"{get_determiner(quantity)} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity)} {get_adverb()} {get_verb(quantity, tense)} {get_prepositional_phrase(quantity)}"

    if tense == "future":
        splited = get_verb(quantity, tense).split(' ')
        will = splited[0]
        verb = splited[1]

        sentence = f"{get_determiner(quantity)} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity)} {will} {get_adverb()} {verb} {get_prepositional_phrase(quantity)}"
        return sentence
    
    else:
        return sentence


def main():

    print(get_sentence(1, "past"))
    print(get_sentence(1, "present"))
    print(get_sentence(1, "future"))
    print(get_sentence(2, "past"))
    print(get_sentence(3, "present"))
    print(get_sentence(4, "future"))


if __name__ == "__main__":
    main() 
