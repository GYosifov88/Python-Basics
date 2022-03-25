

most_powerfull_word = ''
most_powerfull_score = 0
while True:
    word = input()

    if word == 'End of words':
        break

    current_counter_of_chars = 0
    for ch in word:
        current_counter_of_chars += ord(ch)
    if word[0].lower() in 'aeoiuy':
        current_counter_of_chars = current_counter_of_chars * len(word)
    else:
        current_counter_of_chars = int(current_counter_of_chars / len(word))

    if current_counter_of_chars > most_powerfull_score:
        most_powerfull_word = word
        most_powerfull_score = current_counter_of_chars

print (f"The most powerful word is {most_powerfull_word} - {most_powerfull_score}")