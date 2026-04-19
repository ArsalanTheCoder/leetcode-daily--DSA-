def LastZeros(CurrentNumber):

    ZeroCount = 0

    while CurrentNumber > 0 and CurrentNumber % 2 == 0:
        ZeroCount += 1
        CurrentNumber = CurrentNumber // 2

    return ZeroCount


def FindMaximumZeros(ListNumbers, MaximumBits):

    MaximumLimit = 1
    for _ in range(MaximumBits):
        MaximumLimit = MaximumLimit * 2

    BestAnswer = 0

    for XorNumber in range(MaximumLimit):

        Skip = False

        for ValueElement in ListNumbers:
            if ValueElement == XorNumber:
                Skip = True
                break

        if Skip:
            continue

        CurrentScore = 0

        for ValueElement in ListNumbers:
            NewNumber = ValueElement ^ XorNumber
            CurrentScore += LastZeros(NewNumber)

        if CurrentScore > BestAnswer:
            BestAnswer = CurrentScore

    return BestAnswer


binaryCounter = int(input())

for _ in range(binaryCounter):

    FirstLine = input().split()

    TotalNumbers = int(FirstLine[0])
    TotalQueries = int(FirstLine[1])
    MaximumBits = int(FirstLine[2])

    ListNumbers = list(map(int, input().split()))

    print(FindMaximumZeros(ListNumbers, MaximumBits))

    for _ in range(TotalQueries):

        QueryLine = input().split()

        PositionIndex = int(QueryLine[0])
        upd_val = int(QueryLine[1])

        PositionIndex = PositionIndex - 1

        ListNumbers[PositionIndex] = upd_val

        print(FindMaximumZeros(ListNumbers, MaximumBits))