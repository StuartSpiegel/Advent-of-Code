# --- Day 4: Passport Processing --- You arrive at the airport only to realize that you grabbed your North Pole
# Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't
# issued by a country and therefore aren't actually valid documentation for travel in most of the world.
#
# It seems like you're not the only one having problems, though; a very long line has formed for the automatic
# passport scanners, and the delay could upset your travel itinerary.
#
# Due to some questionable network security, you realize you might be able to solve both of these problems at the
# same time.
#
# The automatic passport scanners are slow because they're having trouble detecting which passports have all required
# fields. The expected fields are as follows:
#
# byr (Birth Year) iyr (Issue Year) eyr (Expiration Year) hgt (Height) hcl (Hair Color) ecl (Eye Color) pid (Passport
# ID) cid (Country ID) Passport data is validated in batch files (your puzzle input). Each passport is represented as
# a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

# Here is an example batch file containing four passports:
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% The first passport is valid - all
# eight fields are present. The second passport is invalid - it is missing hgt (the Height field).
#
# The third passport is interesting; the only missing field is cid, so it looks like data from North Pole
# Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid
# fields. Treat this "passport" as valid.
#
# The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not,
# so this passport is invalid.
#
# According to the above rules, your improved system would report 2 valid passports.
#
# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch
# file, how many passports are valid?

def PassportProcessing(d):
    counter = 0
    for k in 'byr iyr eyr hgt hcl ecl pid'.split():
        if k in d:
            counter += 1
    return counter == 7


def PassportProcessing_2(d):
    def ishex(s):
        for j in s:
            if j not in '0123456789abcdef': return False  # check the input is valid hex / subfunction - ishex
        return True

    counter = 0
    for k in 'byr iyr eyr hgt hcl ecl pid'.split():
        if k in d:
            counter += 1
    if counter != 7: return False  # we are missing a field
    v = d['byr']  # store the birth year field for comparison
    if not (len(v) == 4 and v.isdigit() and '1920' <= v <= '2002'): return False  # start Rules check for automatic
    # validation (1920-2002)
    v = d['iyr']
    if not (len(v) == 4 and v.isdigit() and '2010' <= v <= '2020'): return False  # iyr 2010-2020
    v = d['eyr']
    if not (len(v) == 4 and v.isdigit() and '2020' <= v <= '2030'): return False  # eyr 2020-2030
    v = d['hgt']
    if v.endswith('cm'):
        if not (150 <= int(v[:-2]) <= 193): return False  # height calc for cm (150-193)
    elif v.endswith('in'):
        if not (59 <= int(v[:-2]) <= 76): return False  # height calc for in (59-76)
    else:
        return False
    v = d['hcl']
    if not (len(v) == 7 and v[0] == '#' and ishex(v[1:])): return False  # haircolor is followed by exactly 6 chars (
    # hex check)
    v = d['ecl']
    if v not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'): return False  # Exactly 1 value
    v = d['pid']
    if not (len(v) == 9 and v.isdigit()): return False  # enforce 9 digit number
    return True


d = {}
c1, c2 = 0, 0
for l in open("input.txt").read().splitlines():
    if len(l) == 0:
        if PassportProcessing(d):
            c1 += 1
        if PassportProcessing_2(d):
            c2 += 1
        d = {}
    else:
        for p in l.split():
            k, v = p.split(':')
            d[k] = v
print(c1)
print(c2)
