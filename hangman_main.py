
import random
easy_list = ('DEPTH', 'FROTH', 'PHASE', 'SHOWY', 'CREAK', 'MANOR', 'ATOLL', 'BAYOU', 'CREPT', 'TIARA', 'ASSET', 'VOUCH', 'ALBUM', 'HINGE', 'MONEY', 'SCRAP', 'GAMER', 'GLASS', 'SCOUR', 'BEING',
 'DELVE', 'YIELD', 'METAL', 'TIPSY', 'SLUNG', 'FARCE', 'GECKO', 'SHINE', 'CANNY', 'MIDST', 'BADGE', 'HOMER', 'TRAIN', 'STORY', 'HAIRY', 'FORGO', 'LARVA', 'TRASH', 'ZESTY', 'SHOWN', 'HEIST',
  'ASKEW', 'INERT', 'OLIVE', 'PLANT', 'OXIDE', 'CARGO', 'FOYER', 'FLAIR', 'AMPLE', 'CHEEK', 'SHAME', 'MINCE', 'CHUNK', 'ROYAL', 'SQUAD', 'BLACK', 'STAIR', 'SCARE', 'FORAY', 'COMMA', 'NATAL',
   'SHAWL', 'FEWER', 'TROPE', 'SNOUT', 'LOWLY', 'STOVE', 'SHALL', 'FOUND', 'NYMPH', 'EPOXY', 'DEPOT', 'CHEST', 'PURGE', 'SLOSH', 'THEIR', 'RENEW', 'ALLOW', 'SAUTE', 'MOVIE', 'CATER', 'TEASE',
    'SMELT', 'FOCUS', 'TODAY', 'WATCH', 'LAPSE', 'MONTH', 'SWEET', 'HOARD', 'CLOTH', 'BRINE', 'AHEAD', 'MOURN', 'NASTY', 'RUPEE', 'CHOKE', 'CHANT', 'SPILL', 'VIVID')


def word_choice( list_type):
    num =int( random.random()*100 )
    global randword
    randword = list_type[num]
    print(randword) # DELETE THIS LATER ON




def game_setup():
    #diff_choice = input("What difficulty do you want?\n easy, medium or hard: ")
    diff_choice = "easy"
    if diff_choice == "easy":
        word_choice(easy_list)
        fail_num = 6
    elif diff_choice == "medium":
        pass                        # make medium diff
    elif diff_choice == "hard":
        pass                        # make hard diff
    else:
        print ("That wasn't a choice")
    return fail_num

def game_main( randword):
    word_len = len(randword)
    print(word_len)
    a = ""
    b = "_ "
    underline = []
    loop_count = 0
    while loop_count < word_len:
        underline.append(b)
        loop_count += 1
    print("".join(underline))


    count = 0
    while True:
        guess_input = input("What is your letter>>>> ")
        for x in randword:
            count += 1

            if x.lower() == guess_input:
                count_measure = count -1
        #print(count_measure, count,underline)
        leftover = count - count_measure
        underline.pop(count_measure)
        underline.insert(count_measure, guess_input.lower())
        underline_str = "".join(underline)
        print(underline_str)
        count = count_measure = 0
        if guess_input == "exit":
            break
        if underline_str.upper() == randword:
            print("You won good job!!")
            break






    #print(word_choice)

game_setup()

game_main(randword)
