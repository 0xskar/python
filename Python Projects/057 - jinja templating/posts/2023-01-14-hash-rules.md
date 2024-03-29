---
title: Hash Rule Standards
date: 2023-01-14 01:20:00 -0500
categories: [Resources, hashes]
tags: [hashcat, john, Scripting, operators, rules]
---

![Hash rule standards](/assets/crackthehash-top.png)

## Wordlist rules syntax.

Each wordlist rule consists of optional rule reject flags followed by one or more simple commands, listed all on one line and optionally separated with spaces. There's also a preprocessor, which generates multiple rules for a single source line. Below you will find descriptions of the rule reject flags, the rule commands (many of them are compatible with those of Crack 5.0a), and the preprocessor syntax.

## Rule reject flags.

| Command | Operation | 
|---------|-----------|
| `-:` | no-op: don't reject |
| `-c` | reject this rule unless current hash type is case-sensitive |
| `-8` | reject this rule unless current hash type uses 8-bit characters |
| `-s` | reject this rule unless some password hashes were split at loading |
| `-p` | reject this rule unless word pair commands are currently allowed |

## Numeric constants and variables.

Numeric constants may be specified and variables referred to with the following characters:

| Command | Operation | 
|---------|-----------|
| `0...9` | for 0...9 |
| `A...Z` | for 10...35 |
| `*` | for max_length |
| `-` | for (max_length - 1) |
| `+` | for (max_length + 1) |
| `a...k` | user-defined numeric variables (with the "v" command) |
| `l` | initial or updated word's length (updated whenever "v" is used) |
| `m` | initial or memorized word's last character position |
| `p` | position of the character last found with the "/" or "%" commands |
| `z` | "infinite" position or length (beyond end of word) |

Here max_length is the maximum plaintext length supported for the current hash type.

These may be used to specify character positions, substring lengths, and other numeric parameters to rule commands as appropriate for a given command. Character positions are numbered starting with 0. Thus, for example, the initial value of "m" (last character position) is one less than that of "l" (length).

## Character classes.

| Command | Operation | 
|---------|-----------|
| `??` | matches "?" |
| `?v` | matches vowels: "aeiouAEIOU" |
| `?c` | matches consonants: "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" |
| `?w` | matches whitespace: space and horizontal tabulation characters |
| `?p` | matches punctuation: ".,:;'?!`" and the double quote character |
| `?s` | matches symbols "$%^&*()-_+=|\<>[]{}#@/~" |
| `?l` | matches lowercase letters a-z |
| `?u` | matches uppercase letters A-Z |
| `?d` | matches digits 0-9 |
| `?a` | matches letters a-zA-Z |
| `?x` | matches letters and digits a-zA-Z0-9 |
| `?z` | matches all characters |

The complement of a class can be specified by uppercasing its name. For example, "?D" matches everything but digits.

## Simple commands.

| Command | Operation | 
|---------|-----------|
| `:` | no-op: do nothing to the input word |
| `l` | convert to lowercase |
| `u` | convert to uppercase |
| `c` | capitalize |
| `C` | lowercase the first character, and uppercase the rest |
| `t` | toggle case of all characters in the word |
| `TN` | toggle case of the character in position N |
| `r` | reverse: "Fred" -> "derF" |
| `d` | duplicate: "Fred" -> "FredFred" |
| `f` | reflect: "Fred" -> "FredderF" |
| `{` | rotate the word left: "jsmith" -> "smithj" |
| `}` | rotate the word right: "smithj" -> "jsmith" |
| `$X` | append character X to the word |
| `^X` | prefix the word with character X |

## String commands.

AN"STR"	insert string STR into the word at position N

To append a string, specify "z" for the position. To prefix the word with a string, specify "0" for the position.

Although the use of the double-quote character is good for readability, you may use any other character not found in STR instead. This is particularly useful when STR contains the double-quote character. There's no way to escape your quotation character of choice within a string (preventing it from ending the string and the command), but you may achieve the same effect by specifying multiple commands one after another. For example, if you choose to use the forward slash as your quotation character, yet it happens to be found in a string and you don't want to reconsider your choice, you may write "Az/yes/$/Az/no/", which will append the string "yes/no". Of course, it is simpler and more efficient to use, say, "Az,yes/no," for the same effect.

## Length control commands.

| Command | Operation | 
|---------|-----------|
| `<N` | reject the word unless it is less than N characters long |
| `>N` | reject the word unless it is greater than N characters long |
| `'N` | truncate the word at length N |

## English grammar commands.

| Command | Operation | 
|---------|-----------|
| `p` | pluralize: "crack" -> "cracks", etc. (lowercase only) |
| `P` | "crack" -> "cracked", etc. (lowercase only) |
| `I` | "crack" -> "cracking", etc. (lowercase only) |

## Insert/delete commands.

| Command | Operation | 
|---------|-----------|
| `[` | delete the first character |
| `]` | delete the last character |
| `DN` | delete the character in position N |
| `xNM` | extract substring from position N for up to M characters |
| `iNX` | insert character X in position N and shift the rest right |
| `oNX` | overstrike character in position N with character X |

Also see the "X" command (extract and insert substring) under "Memory access commands" below.

Note that square brackets ("[" and "]") are special characters to the preprocessor: you should escape them with a backslash ("\") if using these commands.

## Charset conversion commands.

| Command | Operation | 
|---------|-----------|
| `S` | shift case: "Crack96" -> "cRACK(^" |
| `V` | lowercase vowels, uppercase consonants: "Crack96" -> "CRaCK96" |
| `R` | shift each character right, by keyboard: "Crack96" -> "Vtsvl07" |
| `L` | shift each character left, by keyboard: "Crack96" -> "Xeaxj85" |

## Memory access commands.

| Command | Operation | 
|---------|-----------|
| `M` | memorize the word (for use with "Q", "X", or to update "m") |
| `Q` | query the memory and reject the word unless it has changed |
| `XNMI` | extract substring NM from memory and insert into current word at I |

If "Q" or "X" are used without a preceding "M", they read from the initial "word". In other words, you may assume an implied "M" at the start of each rule, and there's no need to ever start a rule with "M" (that "M" would be a no-op). The only reasonable use for "M" is in the middle of a rule, after some commands have possibly modified the word.

The intended use for the "Q" command is to help avoid duplicate candidate passwords that could result from multiple similar rules. For example, if you have the rule "l" (lowercase) somewhere in your ruleset and you want to add the rule "lr" (lowercase and reverse), you could instead write the latter as "lMrQ" in order to avoid producing duplicate candidate passwords for palindromes.

The "X" command extracts a substring from memory (or from the initial word if "M" was never used) starting at position N (in the memorized or initial word) and going for up to M characters. It inserts the substring into the current word at position I. The target position may be "z" for appending the substring, "0" for prefixing the word with it, or it may be any other valid numeric constant or variable. Some example uses, assuming that we're at the start of a rule or after an "M", would be "X011" (duplicate the first character), "Xm1z" (duplicate the last character), "dX0zz" (triplicate the word), "<4X011X113X215" (duplicate every character in a short word), ">9x5zX05z" (rotate long words left by 5 characters, same as ">9{{{{{"), ">9vam4Xa50'l" (rotate right by 5 characters, same as ">9}}}}}").

## Numeric commands.

| Command | Operation | 
|---------|-----------|
| `vVNM` | update "l" (length), then subtract M from N and assign to variable V |

"l" is set to the current word's length, and its new value is usable by this same command (if N or/and M is also "l").

V must be one of "a" through "k". N and M may be any valid numeric constants or initialized variables. It is OK to refer to the same variable in the same command more than once, even three times. For example, "va00" and "vaaa" will both set the variable "a" to zero (but the latter will require "a" to have been previously initialized), whereas "vil2" will set the variable "i" to the current word's length minus 2. If "i" is then used as a character position before the word is modified further, it will refer to the second character from the end. It is OK for intermediate variable values to become negative, but such values should not be directly used as positions or lengths. For example, if we follow our "vil2" somewhere later in the same rule with "vj02vjij", we'll set "j" to "i" plus 2, or to the word's length as of the time of processing of the "vil2" command earlier in the rule.

## Character class commands.

| Command | Operation | 
|---------|-----------|
| `sXY` | replace all characters X in the word with Y |
| `s?CY` | replace all characters of class C in the word with Y |
| `@X` | purge all characters X from the word |
| `@?C` | purge all characters of class C from the word |
| `!X` | reject the word if it contains character X |
| `!?C` | reject the word if it contains a character in class C |
| `/X` | reject the word unless it contains character X |
| `/?C` | reject the word unless it contains a character in class C |
| `=NX` | reject the word unless character in position N is equal to X |
| `=N?C` | reject the word unless character in position N is in class C |
| `(X` | reject the word unless its first character is X |
| `(?C` | reject the word unless its first character is in class C |
| `)X` | reject the word unless its last character is X |
| `)?C` | reject the word unless its last character is in class C |
| `%NX` | reject the word unless it contains at least N instances of X |
| `%N?C` | reject the word unless it contains at least N characters of class C |

## Extra "single crack" mode commands.

When defining "single crack" mode rules, extra commands are available for word pairs support, to control if other commands are applied to the first, the second, or to both words:

| Command | Operation | 
|---------|-----------|
| `1` | first word only |
| `2` | second word only |
| `+` | the concatenation of both (should only be used after a "1" or "2") |

If you use some of the above commands in a rule, it will only process word pairs (e.g., full names from the GECOS field) and reject single words. A "+" is assumed at the end of any rule that uses some of these commands, unless you specify it manually. For example, "1l2u" will convert the first word to lowercase, the second one to uppercase, and use the concatenation of both. The use for a "+" might be to apply some more commands: "1l2u+r" will reverse the concatenation of both words, after applying some commands to them separately.

## The rule preprocessor.

The preprocessor is used to combine similar rules into one source line. For example, if you need to make John try lowercased words with digits appended, you could write a rule for each digit, 10 rules total. Now imagine appending two-digit numbers - the configuration file would get large and ugly.

With the preprocessor you can do these things easier. Simply write one source line containing the common part of these rules followed by the list of characters you would have put into separate rules, in square brackets (the way you would do in a regexp). The preprocessor will then generate the rules for you (at John startup for syntax checking, and once again while cracking, but never keeping all of the expanded rules in memory). For the examples above, the source lines will be `l$[0-9]` (lowercase and append a digit) and `l$[0-9]$[0-9]` (lowercase and append two digits). These source lines will be expanded to 10 and 100 rules, respectively. By the way, preprocessor commands are processed right-to-left while character lists are processed left-to-right, which results in natural ordering of numbers in the above examples and in other typical cases. Note that arbitrary combinations of character ranges and character lists are valid. For example, `[aeiou]` will use vowels, whereas `[aeiou0-9]` will use vowels and digits. If you need to have John try vowels followed by all other letters, you can use `[aeioua-z]` - the preprocessor is smart enough not to produce duplicate rules in such cases (although this behavior may be disabled with the "\r" magic escape sequence described below).

There are some special characters in rules ("[" starts a preprocessor character list, "-" marks a range inside the list, etc.) You should prefix them with a backslash ("\") if you want to put them inside a rule without using their special meaning. Of course, the same applies to "\" itself. Also, if you need to start a preprocessor character list at the very beginning of a line, you'll have to prefix it with a ":" (the no-op rule command), or it would be treated as a new section start.

Finally, the preprocessor supports some magic escape sequences. These start with a backslash and use characters that you would not normally need to escape. In the following paragraph describing the escapes, the word "range" refers to a single instance of a mix of character lists and/or ranges placed in square brackets as illustrated above.

Currently supported are "\1" through "\9" for back-references to prior ranges (these will be substituted by the same character that is currently substituted for the referenced range, with ranges numbered from 1, left-to-right), "\0" for back-reference to the immediately preceding range, "\p" before a range to have that range processed "in parallel" with all preceding ranges, "\p1" through "\p9" to have the range processed "in parallel" with the specific referenced range, "\p0" to have the range processed "in parallel" with the immediately preceding range, and "\r" to allow the range to produce repeated characters. The "\r" escape is only useful if the range is "parallel" to another one or if there's at least one other range "parallel" to this one, because you should not want to actually produce duplicate rules.

Please refer to the default configuration file for John the Ripper for many example uses of the features described in here.

Cleanup up formatting of <https://www.openwall.com/john/doc/RULES.shtml> for easy reference.