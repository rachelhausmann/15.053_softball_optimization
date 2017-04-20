import data

print(data.jasmin)

# state defined as (on 1st, on 2nd, on 3rd, inning, outs, score, batter index)

def walk(state):
    print("walk")
    # no one on first
    if not state[0]:
        return (True, state[1], state[2], state[3], state[4], state[5], (state[6]+1)%9)
    # no one on second
    elif not state[1]:
        return (True, True, state[2], state[3], state[4], state[5], (state[6]+1)%9)
    # no one on third
    elif not state[2]:
        return (True, True, True, state[3], state[4], state[5], (state[6]+1)%9)
    # someone on every base
    else:
        return (True, True, True, state[3], state[4], state[5]+1, (state[6]+1)%9)

def strikeout(state):
    print("strikeout")
    # 2 outs
    if state[4] == 2:
        # not last inning
        if state[3] < 7:
            return (False, False, False, state[3]+1, 0, state[5], (state[6]+1)%9)
        else:
            # end of game
            return
    else:
        return (state[0], state[1], state[2], state[3], state[4]+1, state[5], (state[6]+1)%9)

def single(state):
    print("single")
    score = state[5]
    # People on 2nd and 3rd score
    if state[1]:
        score += 1
    if state[2]:
        score += 1
    # if someone on 1st --> 3rd
    if state[0]:
        return (True, False, True, state[3], state[4], score, (state[6]+1)%9)
    else:
        return (True, False, False, state[3], state[4], score, (state[6]+1)%9)

def double(state):
    print("double")
    score = state[5]
    # People on 1st, 2nd, and 3rd score
    if state[0]:
        score += 1
    if state[1]:
        score += 1
    if state[2]:
        score += 1
    return (False, True, False, state[3], state[4], score, (state[6]+1)%9)

def triple(state):
    print("triple")
    score = state[5]
    # People on 1st, 2nd, and 3rd score
    if state[0]:
        score += 1
    if state[1]:
        score += 1
    if state[2]:
        score += 1
    return (False, False, True, state[3], state[4], score, (state[6]+1)%9)

def homerun(state):
    print("homerun")
    # batter scores
    score = state[5] + 1
    # People on 1st, 2nd, and 3rd score
    if state[0]:
        score += 1
    if state[1]:
        score += 1
    if state[2]:
        score += 1
    return (False, False, False, state[3], state[4], score, (state[6]+1)%9)

def out_advance_runners(state):
    print("out advance")
    if state[4] == 2:
        # not last inning
        if state[3] < 7:
            return (False, False, False, state[3]+1, 0, state[5], (state[6]+1)%9)
        else:
            # end of game
            return
    else:
        score = state[5]
        # person on 3rd scores
        if state[2]:
            score += 1
        # everyone goes forward one
        return (False, state[0], state[1], state[3], state[4]+1, state[5], (state[6]+1)%9)

def out_no_advance(state):
    print("out no advance")
    # if already 2 outs
    if state[4] == 2:
        # not last inning
        if state[3] < 7:
            return (False, False, False, state[3]+1, 0, state[5], (state[6]+1)%9)
        else:
            # end of game
            return
    else:
        return (state[0], state[1], state[2], state[3], state[4]+1, state[5], (state[6]+1)%9)

# # Testing
# # state defined as (on 1st, on 2nd, on 3rd, inning, outs, score, batter index)
# outcomes = [single, double, triple, homerun, out_advance_runners, out_no_advance, walk, strikeout]
# for outcome in outcomes:
#     # begin = (False, False, False, 1, 0, 0, 0)
#     # print("begin game")
#     # print(begin)
#     # print(outcome(begin))
#     onfirst = (True, False, False, 1, 0, 0, 0)
#     print("on first")
#     print(onfirst)
#     print(outcome(onfirst))

