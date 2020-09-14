import hashlib
import timeit

def prep_dictionary(dict_file,mode):
    dict = {}
    words = ()
    previous_count = 1
    fobj = open(dict_file, mode)
    for line in fobj:
        line = line.strip()
        words = line,hashlib.md5(line.encode('utf-8')).hexdigest()     
        dict[previous_count] = words
        previous_count += 1
    fobj.close()
    return dict

def brute_force(dict,passwd):
    for x,y in dict.items():
        if(y[1] == passwd):
            print("Es konnte eine Übereinstimmung gefunden werden mit dem {}. Element {}".format(x,y))
            return True
    print("Es konnte keine Übereinstimmung gefunden werden")
    return False

def main():
    print("Geben Sie ein Wort ein:")
    str=input()
    passwd=hashlib.md5(str.encode('utf-8')).hexdigest()
    print("Der MD5 Hash für das eingegebene Wort lautet: {}".format(passwd))
    dict = prep_dictionary("words_alpha.txt", "r")
    brute_force(dict, passwd)

if __name__ == "__main__":
    main()
    input()