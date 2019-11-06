# word frequency
# make the letters lowercase


def word_count(str):
    count = dict()
    words = str.split()

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

example_paragraph = "It was a beautiful day in New York City. " \
                    "Our hero Ariana Grande was on a walk from the Standard to Duane Reade." \
                    " Ariana Grande was walking rather " \
                    "quickly because she had lived in New York for a few months." \
                    " All of a sudden a slimy donut appeared out of nowhere. Ariana Grande " \
                    "decided to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade " \
                    "Ariana Grande decides to go to Times Square instead. What a beautiful day in New York."

# make all letters lowercase
example_paragraph_lower = example_paragraph.lower()

# remove all periods
example_paragraph_lower_no_punctuation = example_paragraph_lower.replace(".", "")

print(word_count(example_paragraph_lower_no_punctuation))
