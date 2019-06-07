
class Probability:

    def ProbabilityOfDrawinganAce(Self):

        ace = 4

        NumberOfCards = 52

        Probability = 4/52

# Print probability rounded to two decimal places
        print(round(Probability, 2))


    def Function1(self):
        drwanCard=1
        NumberOfCards = 52
        RemainingCards = NumberOfCards-drwanCard
        ace=4
        # Determine the probability of drawing an Ace after drawing a King on the first draw
        probability1 = ace/RemainingCards

       
        # Determine the probability of drawing an Ace after drawing an Ace on the first draw
        ace = ace-1
        probability2 = ace/NumberOfCards
        print(round(probability1, 2))
        print(round(probability2, 2))



def main():

    v1 = ("AceProbability")
    v2 = ("ProbabilityAfterDrawingAce")
    val = input("Enter your opration: ")
  
    if v1 == val:
        p1 = Probability()
        p1.ProbabilityOfDrawinganAce()
    elif v2 == val:
        p1 = Probability()
        p1.Function1()    
        
main()        

 