from collections import Counter 

members = {
    "Amar" : 12,
    "Kedar" : 1,
    "Rohan" : 3,
    "Rohit" : 5,
    "Tejas" : 0,
    "Kiran" : 9

}


books ={
    "css" : 3,
    "c++" : 2,
    "java" :5,
    "javascript" : 1,
    "python": 10
}


AvgBookBorrowed = sum(members.values())/len(members)
HigestBorrowedBook = max(books,key=books.get)
LowestBorrowedBook = min(books,key=books.get)
ZeroBorrowedBook = list(members.values()).count(0)
BorrowedCount = Counter(members.values())
MostFrequentlyBorrowedBooks = BorrowedCount.most_common(1)[0][0]



print("avarge Books Borrowed : ",AvgBookBorrowed)
print("Highest Borrowed Book :",HigestBorrowedBook)
print("Lowest Borrowed Book :",LowestBorrowedBook)
print("Zero Borrowed book : ",ZeroBorrowedBook)
print("Most Frequently Borrowed Book : ",MostFrequentlyBorrowedBooks)
