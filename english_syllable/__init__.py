import re


def count(s):
    total_syllables = 0

    # qu to tq
    s = re.sub(r'qu','qw', s)

    # replace endings
    s = re.sub(r'(es$)|(que$)|(gue$)', '', s)

    s = re.sub(r'^re', r'ren', s)
    s = re.sub(r'^gua', r'ga', s)
    s = re.sub(r'([aeiou])(l+e$)', r'\g<1>', s)
    (s, syllables) = re.subn(r'([bcdfghjklmnpqrstvwxyz])(l+e$)', r'\g<1>', s)
    total_syllables += syllables

    s = re.sub(r'([aeiou])(ed$)', r'\g<1>', s)
    (s, syllables) = re.subn(r'([bcdfghjklmnpqrstvwxyz])(ed$)', r'\g<1>', s)
    total_syllables += syllables

    endsp = re.compile(r'(ly$)|(ful$)|(ness$)|(ing$)|(est$)|(er$)|(ent$)|(ence$)')
    (s, syllables) = endsp.subn(r'', s)
    total_syllables += syllables
    (s, syllables) = endsp.subn(r'', s)
    total_syllables += syllables

    s = re.sub(r'(^y)([aeiou][aeiou]*)', r'\g<2>', s)
    s = re.sub(r'([aeiou])(y)', r'\g<1>t', s)
    (s, syllables) = re.subn(r'(^y)([bcdfghjklmnpqrstvwxyz])', r'\g<2>', s)
    total_syllables += syllables
    total_syllables += syllables

    s = re.sub(r'aa+', r'a', s)
    s = re.sub(r'ee+', r'e', s)
    s = re.sub(r'ii+', r'i', s)
    s = re.sub(r'oo+', r'o', s)
    s = re.sub(r'uu+', r'u', s)

    # Dipthongs
    dipthongs = re.compile(r'(ai)|(au)|(ea)|(ei)|(eu)|(ie)|(io)|(oa)|(oe)|(oi)|(ou)|(ue)|(ui)')
    s, syllables = dipthongs.subn('', s)
    total_syllables += syllables

    if len(s) > 3:
        s = re.sub(r'([bcdfghjklmnpqrstvwxyz])(e$)', r'\g<1>', s)

    s, syllables = re.subn(r'[aeiouy]', '', s)
    total_syllables += syllables

    return total_syllables
