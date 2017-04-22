import data
import outcome_functions as results
import pprint

batters = [data.jasmin, data.monica, data.ali, data.natalie, data.amanda, data.zoe, data.erika, data.kim, data.katie,
           data.tori]
outcomes = [results.walk, results.strikeout, results.single, results.double, results.triple, results.homerun,
            results.out_advance_runners, results.out_no_advance]
outcome_words = ["walk", "strikeout", "single", "double", "triple", "homerun", "out_advance", "out_no_advance"]

# state defined as (on 1st, on 2nd, on 3rd, inning, outs, score, batter index)

order = [0, 1, 2, 3, 4, 5, 6, 7, 8]
order = [0]*9
start = (False, False, False, 1, 0, 0, 0)
states = set()
states.add(start)
state_prob = {start: 1}
exp_score = 0

# state = states.pop()
# for i in range(len(outcomes)):
#     res = outcomes[i](state)
#     states.add(res)
#     if res not in state_prob:
#         state_prob[res] = 0
#     state_prob[res] += state_prob[state]*batters[order[state[6]]][outcome_words[i]]
# state_prob[state] = 0
#
# pprint.pprint(states)
# pprint.pprint(state_prob)
for batter in range(10):
    order = [batter]*9
    states = set()
    states.add(start)
    state_prob = {start: 1}
    exp_score = 0
    while len(states) > 0:
        state = states.pop()
        for i in range(len(outcomes)):
            res = outcomes[i](state)
            res_prob = state_prob[state]*batters[order[state[6]]][outcome_words[i]]
            # game finished
            if res[0] == "end":
                exp_score += res[1]*res_prob
            # game continuing
            else:
                states.add(res)
                if res not in state_prob:
                    state_prob[res] = 0
                state_prob[res] += res_prob
        state_prob[state] = 0

    print batters[batter]["name"], ":", exp_score




