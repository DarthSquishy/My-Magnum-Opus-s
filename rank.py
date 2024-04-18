def main():

    print ("Insert Rank and Tier (Iron 1) or Rank Tier and RR (Iron 1 33rr) RR RECOMMENDED FOR IMM/RAD")
    p0 = input("Team 1 Player 1: ").strip().lower()
    p0 = ranktype(p0)
    print (p0)
    p1 = input("Team 1 Player 2: ").strip().lower()
    p1 = ranktype(p1)
    print (p1)
    p2 = input("Team 1 Player 3: ").strip().lower()
    p2 = ranktype(p2)
    print (p2)
    p3 = input("Team 1 Player 4: ").strip().lower()
    p3 = ranktype(p3)
    print (p3)
    p4 = input("Team 1 Player 5: ").strip().lower()
    p4 = ranktype(p4)
    print (p4)
    p5 = input("Team 2 Player 1: ").strip().lower()
    p5 = ranktype(p5)
    print (p5)
    p6 = input("Team 2 Player 2: ").strip().lower()
    p6 = ranktype(p6)
    print (p6)
    p7 = input("Team 2 Player 3: ").strip().lower()
    p7 = ranktype(p7)
    print (p7)
    p8 = input("Team 2 Player 4: ").strip().lower()
    p8 = ranktype(p8)
    print (p8)
    p9 = input("Team 2 Player 5: ").strip().lower()
    p9 = ranktype(p9)
    print (p9)
    t1 = int((p0 + p1 + p2 + p3 + p4) / 5)
    print (f"Team 1 is {t1}RR")
    t2 = int((p5 + p6 + p7 + p8 + p9) / 5)
    print (f"Team 2 is {t2}RR")
    if t1 > t2:
        t1 = t1 - t2
        print (f"Team 1 is {t1}RR higher than Team 2!")
    elif t2 > t1:
        t2 = t2 - t1
        print (f"Team 2 is {t2}RR higher than Team 1!")
    else:
         print ("Team 1 and Team 2 are perfectly balanced, as all things should be...")





def ranktype(a):
    a = str(a)
    if (a).startswith("stop"):
         sys.exit(closed)

    elif (a).startswith("radiant") or (a).startswith("immortal"):
        if (a).endswith("rr"):
            a = (a).rstrip("rr")
            (rank), (tier), (rr) = (a).split(" ", maxsplit=2)
            rank = (rankrr(rank))
            rank = int(rank)
            rr = int(rr)
            (a) = rank + rr
            return (a)

        elif (a).endswith(str(1)) or (a).endswith(str(2)) or (a).endswith(str(3)):
            (rank), (tier) = (a).split(" ")
            rank = (rankrr(rank))
            rank = int(rank)
            (a) = rank
            return (a)
        else:
             print("USER ERROR - MIGHT HAVE FORGOT TO WRITE RR")

    elif (a).endswith("rr"):
        a = (a).rstrip("rr")
        (rank), (tier), (rr) = (a).split(" ", maxsplit=2)
        rank = (rankrr(rank))
        rank = int(rank)
        tier = (tierrr(tier))
        tier = int(tier)
        rr = int(rr)
        (a) = rank + tier + rr
        return (a)

    elif (a).endswith(str(1)) or (a).endswith(str(2)) or (a).endswith(str(3)):
        (rank), (tier) = (a).split(" ")
        rank = (rankrr(rank))
        rank = int(rank)
        tier = (tierrr(tier))
        tier = int(tier)
        (a) = rank + tier
        return (a)
    else:
         print("USER ERROR - MIGHT HAVE FORGOT TO WRITE RR")


def rankrr(b):
    if b == ("iron"):
        b = 0
        return (b)
    elif b == ("bronze"):
         b = 300
         return (b)
    elif b == ("silver"):
         b = 600
         return (b)
    elif b == ("gold"):
         b = 900
         return (b)
    elif b == ("platinum"):
         b = 1200
         return (b)
    elif b == ("diamond"):
         b = 1500
         return (b)
    elif b == ("ascendant"):
         b = 1800
         return (b)
    elif b == ("immortal"):
         b = (2100)
         return (b)
    elif "rad" in (b):
         b = (2100)
         return (b)
    else:
         print("RANK ERROR (invalid rank name)")

def tierrr(c):
    if c == ("1"):
         c = 0
         return (c)
    elif c == ("2"):
         c = 100
         return (c)
    elif c == ("3"):
         c = 200
         return (c)
    else:
         print("RANK TIER ERROR (invalid tier number)")

#def rrrr(d):




main()
