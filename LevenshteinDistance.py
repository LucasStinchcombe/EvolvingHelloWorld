#!/usr/bin/env python

##### MAIN #####
def main():
    s1 = args.string[0]
    s2 = args.string[1]
    print editdistance(s1,s2)

def editdistance(s1,s2):
    M = [[0 for x in range(len(s2)+1)] for x in range(len(s1)+1)]

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if min(i,j) == 0:
                M[i][j] = max(i,j)
            else:
                M[i][j] = recurrence(M,s1,s2,i,j)

    return M[len(s1)][len(s2)]

def recurrence(M,s1,s2,i,j):
    r1 = M[i-1][j]+1
    r2 = M[i][j-1]+1
    r3 = M[i-1][j-1] if s1[i-1]==s2[j-1] else M[i-1][j-1]+1
    return min(r1,r2,r3)

def print_matrix(M):
    for row in M:
        for i in row:
            print repr(i).rjust(3),
        print "\n"

if __name__ == "__main__":
    import sys
    import argparse

    ##### Argument Parser #####
    descr = 'Compute Levenshtein edit distance between two strings'
    parser = argparse.ArgumentParser(description = descr)
    parser.add_argument("string", help="display a square of a given number",
                                  nargs=2)
    args = parser.parse_args()

    main()
