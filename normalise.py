# -*- coding: utf-8 -*-

import re

def is_ascii(s):
    try:
        s.encode("ascii")
        return True
    except UnicodeEncodeError:
        return False
        
# checks if a string contains more than tolerance percentage of
# alphanumerical characters
def is_language(s, tolerance=0.5):
    alpha_chars = list(filter(str.isalpha, s))
    if len(alpha_chars)/len(s) < tolerance:
        return False
    return True

def has_special_char(s):
    special_chars = re.compile('[@_#\$%;^&*<>/\|}{~+\]\[§=]')        
    return bool(special_chars.search(s))

def has_special_char_seq(s):
    special_chars = re.compile('[@_#\$%;^&*<>/\|}{~+\]\[§=][@_#\$%;^&*<>/\|}{~+\]\[§=]')        
    return bool(special_chars.search(s))


def is_only_whitespace(s):
    not_whitespace = re.compile("\S")
    return not bool(not_whitespace.search(s))
   
    
# character correspondences of HTML entities 
known_entities = {"&apos;": "'",
                  "&le;": "≤",
                  "&ge;": "≥",
                  "&gt;": ">",
                  "&lt;": "<",
                  "&amp;": "&",
                  "&quot;": '"',
                  "&#91;":"[",
                  "&#93;":"]"}

def replace_html_entities(s):
    html_entity = re.compile("&\s*[a-z]+\s*;|&\s*#[0-9]+\s*;")                             
    new_s = s[:]
    for result in html_entity.finditer(s):
        start, end = result.span()
        
        found_entity = re.sub("\s+", "", s[start:end])
        if found_entity in known_entities:
            new_s = new_s.replace(s[start:end], known_entities[found_entity])
        
    return new_s


# remove weird unicode entities which do not have character correspondences
def replace_unicode_artifacts(s):
    s = s.replace("\ufeff", "")
    s = s.replace("\u200b", "")
    return s


basic_punct_EN = {".", ",", ";", ":", "?", "!"}
basic_punct_TI = {"፧", "፦", "፣", "።"}
def separate_basic_punct(s, cur_punct_set):
    ls = []
    for i, c in enumerate(s):
        if c in cur_punct_set:
            if i > 0 and not s[i-1] == " ":
                ls.append(" " + c)
            else:
                ls.append(c)
        else:
            ls.append(c)
            
    return "".join(ls)


basic_punct_correspondences = {"?":"፧", ":":"፦", ":":"፤", ";":"፥", ",":"፣", ".":"።"}
inv_punct_corres = {v: k for k, v in basic_punct_correspondences.items()}
def normalise_punct(s, punct_corres_dict):
    ls = []
    for c in s:
        if c in punct_corres_dict:
            ls.append(punct_corres_dict[c])
        else:
            ls.append(c)
            
    return "".join(ls)
        

ti_word_separator = "፡"
def replace_word_separator(s):
    return s.replace(ti_word_separator, "")
#    ls = []
#    for i, c in enumerate(s):
#        if c == ti_word_separator:
            


def cleaner_iter(lines_en, lines_ti):
    is_lang_25 = lambda s: is_language(s, tolerance=0.25)   
    for i, (s_en, s_ti) in enumerate(zip(lines_en, lines_ti)):
        ### filtering
        
        # whitespace
        if is_only_whitespace(s_en) and is_only_whitespace(s_ti):
            continue
        elif is_only_whitespace(s_en) or is_only_whitespace(s_ti):
            raise ValueError("WHITESPACE: " + s_en + "\t" + s_ti)
        
        if not is_lang_25(s_en) and not is_lang_25(s_ti):
            continue
        elif not is_lang_25(s_en) or not is_lang_25(s_ti):
            continue
            
            
        ### processing
        
        # strip
        clean_s_en, clean_s_ti = s_en.strip(), s_ti.strip()
        
        # html entities
        clean_s_en, clean_s_ti = replace_html_entities(clean_s_en),\
                                    replace_html_entities(clean_s_ti)
        
        clean_s_en, clean_s_ti = replace_html_entities(clean_s_en),\
                                    replace_html_entities(clean_s_ti)
        
        # handle encoding artifacts
        clean_s_en, clean_s_ti = replace_unicode_artifacts(clean_s_en),\
                                    replace_unicode_artifacts(clean_s_ti)
                                    
        # handle special character sequences
        clean_s_en, clean_s_ti = clean_s_en.replace("===", ""),\
                                    clean_s_ti.replace("===", "")
        clean_s_en, clean_s_ti = clean_s_en.replace("==", ""),\
                                    clean_s_ti.replace("==", "")
                                    
        # convert Ge'ez punctuation to English punctuation    
        clean_s_en, clean_s_ti = normalise_punct(clean_s_en, inv_punct_corres),\
                            normalise_punct(clean_s_ti, inv_punct_corres)
            
        # add a whitespace between words and punctuation
        clean_s_en, clean_s_ti = separate_basic_punct(clean_s_en, basic_punct_EN),\
                                separate_basic_punct(clean_s_ti, basic_punct_EN)
        
        # replace the Ge'ez word separator (only rarely used anymore)
        clean_s_en, clean_s_ti = replace_word_separator(clean_s_en),\
                                replace_word_separator(clean_s_ti)
        
        yield clean_s_en, clean_s_ti
    
    
##%%
#        
#
#        
#d = "JW_nonbible"
#f_en = "nonbible_en_1"
#f_ti = "nonbible_ti_1"
#
#
#with open(d + "/" + f_en, encoding="utf-8") as handle:
#    lines_en = list(handle)
#    
#with open(d + "/" + f_ti, encoding="utf-8") as handle:
#    lines_ti = list(handle)
#
#
#
#
#    
#d = "JW_nonbible"
#f_en = "nonbible_en_3"
#f_ti = "nonbible_ti_3"
#
#
#with open(d + "/" + f_en, encoding="utf-8") as handle:
#    lines_en.extend(list(handle))
#    
#with open(d + "/" + f_ti, encoding="utf-8") as handle:
#    lines_ti.extend(list(handle))
#    
#
##%%
#    
#
#cleaned_tups = list(cleaner_iter(lines_en, lines_ti))
#
#en_cleaned, ti_cleaned = list(zip(*cleaned_tups))
#
#
#
#
#
#
#
#
##%%
#
#
#d = "."
#f_en = "EN_volunteers"
#f_ti = "TI_volunteers"
#
#
#with open(d + "/" + f_en, encoding="utf-8") as handle:
#    lines_en = list(handle)
#    
#with open(d + "/" + f_ti, encoding="utf-8") as handle:
#    lines_ti = list(handle)
#
#
#
#
#    
#d = "."
#f_en = "EN_jw"
#f_ti = "TI_jw"
#
#
#with open(d + "/" + f_en, encoding="utf-8") as handle:
#    lines_en.extend(list(handle))
#    
#with open(d + "/" + f_ti, encoding="utf-8") as handle:
#    lines_ti.extend(list(handle))
#    
#
#d = "."
#f_en = "EN_bible"
#f_ti = "TI_bible"
#
#
#with open(d + "/" + f_en, encoding="utf-8") as handle:
#    lines_en.extend(list(handle))
#    
#with open(d + "/" + f_ti, encoding="utf-8") as handle:
#    lines_ti.extend(list(handle))
#
#
##%%
#    
#en_cleaned, ti_cleaned = lines_en, lines_ti
#    
##%%
#
#f_out_en = "EN_ALL"
#f_out_ti = "TI_ALL"
#
#
#with open(f_out_en, "w", encoding="utf-8") as handle:
#    for s in en_cleaned:
#        handle.write(s)
#        handle.write("\n")
#
#with open(f_out_ti, "w", encoding="utf-8") as handle:
#    for s in ti_cleaned:
#        handle.write(s)
#        handle.write("\n")


