# rules.py
import datetime
import math
import re
# The total number of rules we plan to have
N_RULES = 45
CURRENT_YEAR = '2025'

# All rules are defined here. This is the single source of truth for all rules.
RULES_DEFINITION = [
    {'description': "Password must be at least 8 characters long.",
     'active': True,
     'check_js': "p => p.length >= 8",
     'check_py': lambda p: len(p) >= 8},

    {'description': "Must contain an uppercase letter.",
     'active': True,
     'check_js': "p => /[A-Z]/.test(p)",
     'check_py': lambda p: any(c.isupper() for c in p)},

    {'description': "Must contain a number.",
     'active': True,
     'check_js': "p => /[0-9]/.test(p)",
     'check_py': lambda p: any(c.isdigit() for c in p)},

    {'description': "Must contain a chess move in algebraic notation.",
     'active': True,
     'check_js': "p => /(?:[RNBQK]?[a-h][1-8]|[a-h][1-8][a-h][1-8])/.test(p)",
     'check_py': (lambda p: re.search(r'(?:[RNBQK]?[a-h][1-8]|[a-h][1-8][a-h][1-8])', p) is not None)},

    {'description': "Must contain a two-digit number that is a multiple of 7.",
     'active': True,
     'check_js': ("p => {const nums = p.match(/\\d{2}/g);"
                  "return nums ? nums.some(n => parseInt(n, 10) % 7 === 0) : false;}"),
     'check_py': (lambda p: any(int(n) % 7 == 0 for n in re.findall(r'\d{2}', p)))},

    {'description': "The first digit must be an even number.",
     'active': True,
     'check_js': "p => /\\d/.test(p) && parseInt(p.match(/\\d/)[0]) % 2 === 0",
     'check_py': lambda p: (m := re.search(r'\d', p)) and int(m.group()) % 2 == 0},

    {'description': "Must contain a special character that is not a letter or number.",
     'active': True,
     'check_js': "p => /[^a-zA-Z0-9]/.test(p)",
     'check_py': lambda p: any(c for c in p if not c.isalnum())},

    {'description': "Must contain a special character from this set: @#$%^&*",
     'active': True,
     'check_js': "p => /[@#$%^&*]/.test(p)",
     'check_py': lambda p: any(c in "@#$%^&*" for c in p)},

    {'description': "Password must contain a word with double letters (like 'letter', 'coffee', 'bottle').",
     'active': True,
     'check_js': "p => /(\\w)\\1/.test(p)",
     'check_py': lambda p: re.search(r'(\w)\1', p) is not None},

    {'description': "Password must contain a chemical element symbol (H, He, Li, Be, ...).",
     'check_js': ("p => /(H|He|Li|Be|B|C|N|O|F|Ne|Na|Mg|Al|Si|P|S|Cl|Ar|K|Ca)/.test(p)"),
     'check_py': lambda p: re.search(r'(H|He|Li|Be|B|C|N|O|F|Ne|Na|Mg|Al|Si|P|S|Cl|Ar|K|Ca)', p) is not None},

    {'description': "Password cannot contain a US state abbreviation (case-sensitive).",
     'active': True,
     'check_js': ("p => !/(AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|"
                  "LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|"
                  "OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WV|WI|WY)/.test(p)"),
     'check_py': (lambda p: not any(abbr in p for abbr in (
         'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
         'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI',
         'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
         'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
         'VT', 'VA', 'WV', 'WI', 'WY')))},

    {'description': "Password must contain the name of a season (spring, summer, autumn, fall, winter).",
     'check_js': "p => /(spring|summer|autumn|fall|winter)/i.test(p)",
     'check_py': lambda p: re.search(r'(spring|summer|autumn|fall|winter)', p, re.I) is not None},

    {'description': "Password must contain the current year.",
     'check_js': ("p => p.includes(new Date().getFullYear().toString())"),
     'check_py': (lambda p: str(datetime.datetime.now().year) in p)},

    {'description': f"The current year cannot immediately follow the season.",
     'check_js': ("p => !/(spring|summer|autumn|fall|winter)\\s*" + CURRENT_YEAR + "/i.test(p)"),
     'check_py': (lambda p, y=CURRENT_YEAR: re.search(r'(spring|summer|autumn|fall|winter)\s*' + y, p, re.I) is None)},

    {'description': "Password must contain exactly 2 exclamation marks, no more, no less.",
     'active': True,
     'check_js': "p => (p.match(/!/g) || []).length === 2",
     'check_py': lambda p: p.count('!') == 2},

    {'description': "Password must include a phone number.",
     'check_js': ("p => /(?:\\+?\\d{1,3}[\\s.-]?)?(?:\\(\\d{3}\\)|\\d{3})[\\s.-]?\\d{3}[\\s.-]?\\d{4}/.test(p)"),
     'check_py': (lambda p: re.search(r"(?:\+?\d{1,3}[\s.-]?)?(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}", p) is not None)},

    {'description': "Password length must be at least 40 characters to be post-quantum ready.",
     'check_js': "p => p.length >= 40",
     'check_py': lambda p: len(p) >= 40},

    {'description': 'Password must contain the phrase "like and subscribe" once per every 37 characters of password.',
     'check_js': ("p => {"
                  "const phrase = 'like and subscribe';"
                  "const expected = Math.floor(p.length / 37);"
                  "const actual = (p.match(new RegExp(phrase, 'gi')) || []).length;"
                  "return actual === expected;}"),
     'check_py': (lambda p: ((p.lower().count("like and subscribe")) == math.floor(len(p) / 37)))},

    {'description': "The password must contain the word 'cat' but not 'dog'.",
     'active': True,
     'check_js': "p => p.toLowerCase().includes('cat') && !p.toLowerCase().includes('dog')",
     'check_py': lambda p: 'cat' in p.lower() and 'dog' not in p.lower()},

    {'description': "Must contain a primary, secondary, or neutral color that is not gray, green, yellow, or red.",
     'active': True,
     'check_js': ("p => /(blue|orange|purple|pink|brown|black|white)/i.test(p) "
                  "&& !/(green|yellow|red)/i.test(p)"),
     'check_py': (lambda p: re.search(r'(blue|orange|purple|pink|brown|black|'
                                      r'white)', p, re.I) and not
                                      re.search(r'(green|yellow|red)', p,  re.I))},

    {'description': "Must contain the current day of the week, spelled out.",
     'active': True,
     'check_js': ("p => p.toLowerCase().includes(new Date().toLocaleString('en-US', {weekday: 'long'})"
                  ".toLowerCase())"),
     'check_py': (lambda p: datetime.datetime.now().strftime('%A').lower() in
                  p.lower())},

    {'description': "Password cannot contain three consecutive letters of the same case.",
     'check_js': ("p => !(/[A-Z]{3}/.test(p) || /[a-z]{3}/.test(p))"),
     'check_py': (lambda p: re.search(r'[A-Z]{3}', p) is None and re.search(r'[a-z]{3}', p) is None)},

    {'description': "Password must include the name of a month.",
     'check_js': ("p => /(january|february|march|april|may|june|july|august|september|october|november|december)/i.test(p)"),
     'check_py': (lambda p: re.search(
     r'(january|february|march|april|may|june|july|august|september|october|november|december)', p, re.IGNORECASE
     ) is not None)},

    {'description': "Months in the password cannot be in any of the seasons in the password.",
     'check_js': ("p => {"
                  "const seasons = {"
                  " spring: ['march','april','may'],"
                  " summer: ['june','july','august'],"
                  " autumn: ['september','october','november'],"
                  " fall: ['september','october','november'],"
                  " winter: ['december','january','february']"
                  "};"
                  "const lower = p.toLowerCase();"
                  "for (const [season, months] of Object.entries(seasons)) {"
                  " if (lower.includes(season)) {"
                  "  for (const m of months) {"
                  "   if (lower.includes(m)) return false;"
                  "  }"
                  " }"
                  "}"
                  "return true;"
                  "}"),
    'check_py': (lambda p: (lambda lower: all(
                not (re.search(season, lower) and any(m in lower for m in months))
                for season, months in {
                    'spring': ['march','april','may'],
                    'summer': ['june','july','august'],
                    'autumn': ['september','october','november'],
                    'fall': ['september','october','november'],
                    'winter': ['december','january','february']
                }.items()
            ))(p.lower())
        )},

    {'description': "The length must be a prime number.",
     'active': True,
     'check_js': ("p => { const num = p.length; if (num <= 1) return false; "
                  "for (let i = 2; i <= Math.sqrt(num); i++) { "
                  "if (num % i === 0) return false; } return true; }"),
     'check_py': (lambda p: (all(len(p) % i != 0 for i in range(2, int(
         math.sqrt(len(p))) + 1)) if len(p) > 1 else True))},

    {'description': "Password must contain the word from the list: apple, june, mississippi, winter, grape, march, summer, honey, october, cyber, at the index determined by the password length mod 10.",
     'check_js': ("p => {"
                  "const idx = p.length % 10;"
                  "const words = ['apple', 'june', 'mississippi,', 'winter', 'grape', 'march', 'summer', 'honey', 'october', 'cyber'];"
                  "return p.toLowerCase().includes(words[idx].toLowerCase());}"),
        'check_py': (lambda p: ['apple', 'june', 'mississippi,', 'winter', 'grape', 'march', 'summer', 'honey', 'october', 'cyber'][len(p) % 10].lower() in p.lower())},

    {'description': "The last character must be '!'",
     'active': True,
     'check_js': "p => p.endsWith('!')",
     'check_py': lambda p: p.endswith('!')},

    {'description': "Must contain the solution to 'Twist, Lick, Dunk' cookie [4]",
     'check_js': "p => /oreo/i.test(p)",
     'check_py': lambda p: 'oreo' in p.lower()},

    {'description': "Must contain the word 'password' (case-insensitive).",
     'active': True,
     'check_js': "p => /password/i.test(p)",
     'check_py': lambda p: 'password' in p.lower()},

    {'description': "Password must contain the first 14 decimal digits of pi in order, each increased by one (mod 10)",
     'check_js': ("p => {const PI14 = '14159265358979'; "
                  "const bumped = [...PI14].map(d => String((Number(d)+1)%10)); "
                  "const pattern = bumped.join('.*'); "
                  "return new RegExp(pattern).test(p);}"),
     'check_py': (lambda p: re.search('.*'.join(str((int(d)+1)%10) for d in '14159265358979'), p) is not None)},

    {'description': "Password must not contain consecutive repeating digits.",
     'check_js': "p => !/(\\d)\\1/.test(p)",
     'check_py': lambda p: re.search(r'(\d)\1', p) is None},

    {'description': "Must contain the Roman numeral for 1337.",
     'active': True,
     'check_js': ("p => /MCCCXXXVII/i.test(p)"),
     'check_py': (lambda p: re.search(r'MCCCXXXVII', p, re.I) is not None)},

    {'description': "Must contain the character 'a' less than 4 times.",
     'active': True,
     'check_js': "p => (p.match(/a/g) || []).length < 4",
     'check_py': lambda p: p.lower().count('a') < 4},

    {'description': "Negative numbers are not allowed.",
     'check_js': ("p => !/-\\d+/.test(p)"),
     'check_py': (lambda p: not re.search(r'-\d+', p))},

    {'description': "The sum of all digits must be a multiple of 8.",
     'active': True,
     'check_js': ("p => {const digits = p.match(/\\d/g); "
                  "if (!digits) return false; "
                  "const sum = digits.reduce((a, d) => a + parseInt(d, 10), 0); "
                  "  return sum % 8 === 0; }"),
     'check_py': lambda p: (sum(int(c) for c in p if c.isdigit()) % 8 == 0) if any(c.isdigit() for c in p) else False},

    {'description': "Password must not contain the number 37.",
     'check_js': ("p => !/37/.test(p)"),
     'check_py': (lambda p: not re.search(r'37', p))},

    {'description': "Password must contain the cube of its own length.",
     'check_js': ("p => p.includes((p.length ** 3).toString())"),
     'check_py': (lambda p: str(len(p) ** 3) in p)},

    {'description': "Password cannot contain any lowercase 'l' characters.",
     'check_js': ("p => !/[l]/.test(p)"),
     'check_py': (lambda p: 'l' not in p)},

    {'description': "Password must contain the phrase 'Where is the post office?' in Spanish.",
     'check_js': ("p => p.toLowerCase().includes('¿dónde está la oficina de correos?')"),
     'check_py': (lambda p: '¿dónde está la oficina de correos?' in p.lower())},

    {'description': "Password must include the phrase 'Nobody expects the Spanish Inquisition!'.",
     'check_js': ("p => p.toLowerCase().includes('nobody expects the spanish inquisition!')"),
     'check_py': (lambda p: 'nobody expects the spanish inquisition!' in p.lower())},

    {'description': "Password must contain one 'bruh' for each occurrence of 'like and subscribe'.",
     'check_js': ("p => {"
                  "const lasCount = (p.match(/like and subscribe/gi) || []).length;"
                  "const bruhCount = (p.match(/bruh/gi) || []).length;"
                  "return lasCount === bruhCount && lasCount > 0;}"),
     'check_py': (lambda p: (len(re.findall(r'like and subscribe', p, re.I)) == len(re.findall(r'bruh', p, re.I)) and len(re.findall(r'like and subscribe', p, re.I)) > 0))},

    {'description': "Must be a palindrome.",
     'check_js': "p => p === p.split('').reverse().join('')",
     'check_py': lambda p: p == p[::-1]},


]
