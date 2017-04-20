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
start = (False, False, False, 1, 0, 0, 0)
states = set()
states.add(start)
state_prob = {start: 1}
score_prob = {}

state = states.pop()
for i in range(len(outcomes)):
    res = outcomes[i](state)
    states.add(res)
    if res not in state_prob:
        state_prob[res] = 0
    state_prob[res] += state_prob[state]*batters[order[state[6]]][outcome_words[i]]
state_prob[state] = 0

pprint.pprint(states)
pprint.pprint(state_prob)

# while len(states) > 0:
#     state = states.pop()


