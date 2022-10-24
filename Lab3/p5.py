def validate_dict(rule_tuples_set, dict):
    for key in dict.keys(): #verifica daca in toate cheile din dictionar se afla si in set ul cu tuple
        if not any(key in tuples for tuples in rule_tuples_set):
            print("The key ", key, " from dictionary does not exist in tuple set")
            return False
    for rule in rule_tuples_set:
        if rule[0] in dict.keys():
            if not dict[rule[0]].startswith(rule[1]) and rule[1] != "":#verif daca valoarea din dictionar incepe cu prefixul din regula,prefixul poate fi si gol: -""- cu "come"
                print("The string ", dict[rule[0]], " does not start with prefix ", rule[1])
                return False
            if not rule[2] in dict[rule[0]][1: len(dict[rule[0]])]: #verif de la al 2 lea pana la penultimul daca contine middleul din tupla: -inside it  too cold- in -inside- 
                print("The string ", dict[rule[0]], " does not have in the middle ", rule[2])
                return False
            if not dict[rule[0]].endswith(rule[3]) and rule[3] != "":#verif daca valoarea din dictionar se termina cu sufixul din regula,sufixul poate fi gol: -""- cu -out-
                print("The string ", dict[rule[0]], " does not end with suffix ", rule[3])
                return False
    print("Dictionary matches rule tuples")
    return True

if __name__=="__main__":
    s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    print(validate_dict(s,d))