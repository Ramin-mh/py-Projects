# this program makes a relation transitive 

relation = [("c", "a"), ("d", "e"), ("b", "a"), ("e", "f"), ("a", "e")]
relation_new = relation.copy()

def find_transitive(length):
    for i in range(length):
        for j in range(length):
            if not j == i:
                if relation_new[i][1] == relation_new[j][0]:
                    if (relation_new[i][0], relation_new[j][1]) not in relation_new:
                        relation_new.append((relation_new[i][0], relation_new[j][1]))

                        return 1
    
    return 0


if __name__ == '__main__':
    while True:
        if find_transitive(len(relation_new)) == 1:
            continue
        else:
            break


    print("------------------------------")
    print(f"Given relation: {relation}")
    print("===========================================================================")
    print(f"Transitive relation: {relation_new}")
    print("------------------------------")