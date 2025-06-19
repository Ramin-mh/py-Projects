# this program makes a relation transitive 

given_relation = {("c", "a"), ("d", "e"), ("b", "a"), ("e", "f"), ("a", "e")}

def find_transitive(relation):
    new_relation = set(relation)
    added = True

    while added:
        added = False
        new_pairs = set()

        for a, b in new_relation:
            for c, d in new_relation:
                if b == c and (a, d) not in new_relation:
                    new_pairs.add((a,d))
                    added = True
        
        new_relation.update(new_pairs)

    return new_relation

if __name__ == '__main__':
    print("------------------------------")
    print(f"Given relation: {given_relation}")
    print("===========================================================================")
    print(f"Transitive relation: {find_transitive(given_relation)}")
    print("------------------------------")