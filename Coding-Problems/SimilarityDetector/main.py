####################### PROJECT 4: PLAGIARISM DETECTION #####################
##################### BY: KEYANN AL-KHEDER & LANCE GARCIA ###################
######################### DATE MODIFIED: DEC 9, 2017 ########################


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""           
                Program for finding the similarity between two files
                using jaquards similarity formula
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#Step 1:
#Return essay file
def file(essay_path):
    fileRef = open(essay_path, 'r')
    line = fileRef.read()
    return line



#Step 2:
#Transform essay files into shingle set
def get_shingled(k, doc):
    shingle = [doc[i:i + k] for i in range(len(doc) - k + 1)]  
    return shingle




#Step 3:
#Analyze Similarity of shingle Set
def intersection(shingle_setA, shingle_setB):
    x = list(shingle_setA)
    y = list(shingle_setB)
    listA = []
    listB = []
    for i in x:
        if i in y:
            listA.append(i)
    listB = (listA) + []
   # return ''.join(listB)
    return len(listB)


#Step 4:
def j_similarity(intersect, a, b):
    return intersect / (a+b-intersect)
    


#Algorithm called by main function
def main():

    #file path input
    filePath_A = input("Enter the pathname of the first essay's file: ")
    filePath_B = input("Enter the pathname of the second essay's file: ")

    #size-k input
    n = int(input("Enter a number-k for shingles: "))


    #create variable for essay
    essay_A = file(filePath_A)
    essay_B = file(filePath_A)


    #pass essay to shingle function
    shingleA = get_shingled(n, essay_A)
    shingleB = get_shingled(n, essay_B)


    #functions analyze shingle set

    AXB = intersection(shingleA, shingleB)

    similarity = j_similarity(AXB, len(shingleA), len(shingleB))

    print("Intersection: ", AXB)
    print("Jacquard's similarity: ", similarity)

    

if __name__ == "__main__":
    main()
