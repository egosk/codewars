# TASK:
# Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and
# the expected justification width. The longest word will never be greater than this width.
# Here are the rules:
#     Use spaces to fill in the gaps between words.
#     Each line should contain as many words as possible.
#     Use '\n' to separate lines.
#     Gap between words can't differ by more than one space.
#     Lines should end with a word not a space.
#     '\n' is not included in the length of a line.
#     Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
#     Last line should not be justified, use only one space between words.
#     Last line should not contain '\n'
#     Strings with one word do not need gaps ('somelongword\n').

def justify(text, width):

    if text == '':
        return ''
    words = text.split()
    justified = ''
    line = words[0]
    words.remove(line)
    for word in words:
        if len(line)+len(word)+1 <= width:
            line = line + ' '
            line = line + word
        else:
            spaces_needed_total = width - len(line)
            spaces_in_line = line.count(' ')
            if spaces_in_line != 0:
                all_spaces_lenght, add_at_begining = divmod(spaces_needed_total,spaces_in_line)
                line = line.replace(' ', ' '*(all_spaces_lenght+2), add_at_begining)
                line = (' '*(all_spaces_lenght+1)).join(line.rsplit(" ", spaces_in_line-add_at_begining))

            justified = justified + line
            justified = justified + '\n'
            line = word
    justified = justified + line
    return justified


print(justify('Very nice! In an unscientific benchmark of replacing the last occurrence of an expression in a typical string in my program (> 500 characters), your solution ', 20))