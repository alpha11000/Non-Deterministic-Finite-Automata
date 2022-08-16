def applyTransition(symbol, atualStates, AFNe, emptyTransition = False):
    nextStates = atualStates if emptyTransition else []
    
    for state in atualStates:
        stateTransitions = AFNe[state]
        apliedStates = stateTransitions[symbol] if symbol in stateTransitions else []

        for appliedState in apliedStates:
            if not appliedState in nextStates:
                nextStates.append(appliedState)

    return nextStates

def applyEmptyTransition(atualStates, AFNe):
    return applyTransition('ε', atualStates, AFNe, True)

def wordRecognition(word, initialState, finalStates, AFNe):
    nextStates = [initialState]
    print(f"{nextStates}")

    for c in word:
        nextStates = applyEmptyTransition(nextStates, AFNe)
        print(f"ε -> {nextStates}")
        nextStates = applyTransition(c, nextStates, AFNe)
        print(f"{c} -> {nextStates}")

    return next((True for state in nextStates if state in finalStates), False)


def main():
    initialState = 1
    finalStates = [2]
    word = "bbaa"

    AFNe = { 
        1:{ 'ε':[2],
            'b':[3]},

        2:{ 'a':[1]},

        3:{ 'a':[2],
            'b':[3, 2]}
    }

    print("Palavra reconhecida." if wordRecognition(word, initialState, finalStates, AFNe) 
    else "Palavra não reconhecida")


if __name__ == "__main__":
    main()