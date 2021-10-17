#Lykilorð skulu vera af lengdinni 6 tákn. Í þau má nota þrjár gerðir tákna, þ.e. bókstafi, sértákn
#og tölustafi. Gerum ráð fyrir 30 bókstöfum í stafrófinu, 20 sértáknum og 10 tölustöfum. Gerum
#ráð fyrir því að öll slík lykilorð séu leyfileg
#Setjum nú það skilyrði að lykilorð verði að innihalda allar þrjár gerðir tákna, það
#er a.m.k. einn bókstaf, a.m.k. eitt sértákn og a.m.k. einn tölustaf. Hve mörg lykilorð
#uppfylla þetta skilyrði?




#Breytum skilyrðum til að það taki ekki alla eilífð að reikna þetta. Höfum 10 bókstafi , 6 sértákn og 3 tölustafi. 

LETTERS = "abcdefghij"
SPECIALS = "!#$%&*"
NUMBERS = "012"

def get_all():
    '''Creates a list of all possible strings of length 6 that are made of LETTERS, SPECIALS and/or NUMBERS'''
    all_set = set()

    LSN = LETTERS + SPECIALS + NUMBERS
    

    for char1 in LSN:
        for char2 in LSN:
            for char3 in LSN:
                for char4 in LSN:
                    for char5 in LSN:
                        for char6 in LSN:
                            word = char1 + char2 + char3 + char4 + char5 + char6
                            all_set.add(word)
    return all_set

def get_answer_set(all_set):
    '''Iterates through all_set and returns only words that contain character AND special AND number'''

    answer_set = set()
    for word in all_set:
        has_letter = False
        has_special = False
        has_number = False
        for char in word:
            if char in LETTERS:
                has_letter = True
            elif char in SPECIALS:
                has_special = True
            elif char in NUMBERS:
                has_number = True
        if (has_letter == True) and (has_special == True) and (has_number == True):
            answer_set.add(word)

    return answer_set
        

def main():
    all_set = get_all()
    print("Fjöldi mögulegra lykilorða alls:", len(all_set))

    answer_set = get_answer_set(all_set)
    print("Fjöldi mögulegra lykilorða sem innihalda bókstaf og sértákn og tölu:", len(answer_set))

if __name__ == "__main__":
    main()

# Útkomur úr þessum kóða gefa:
# Fjöldi mögulegra lykilorða alls: 47045881
# Fjöldi mögulegra lykilorða sem innihalda bókstaf og sértákn og tölu: 25957800

#Ef ég svo reikna út samkvæmt mínum útreiknum á dæmablaði þá fæ ég út: 
# 19^6 - (9^6 + 13^6 + 16^6 - 3^6 - 6^6 - 10^6 + 0) = 25957800



    
