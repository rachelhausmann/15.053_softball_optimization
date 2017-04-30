import data
import outcome_functions as results
import best_thousand
import pprint

best_orders = best_thousand.best

batters = [data.jasmin, data.monica, data.ali, data.natalie, data.amanda, data.zoe, data.erika, data.kim, data.katie,
           data.tori]
outcomes = [results.walk, results.strikeout, results.single, results.double, results.triple, results.homerun,
            results.out_advance_runners, results.out_no_advance]
outcome_words = ["walk", "strikeout", "single", "double", "triple", "homerun", "out_advance", "out_no_advance"]

batter_mapping = {
    1: data.jasmin,
    2: data.monica,
    3: data.ali,
    5: data.natalie,
    6: data.amanda,
    10: data.zoe,
    11: data.erika,
    12: data.kim,
    16: data.katie,
    23: data.tori
}

# state defined as (on 1st, on 2nd, on 3rd, inning, outs, score, batter index)

start = (False, False, False, 1, 0, 0, 0)
scores_list = []

for attempt in best_orders:
    order = attempt[1]
    states = set()
    states.add(start)
    state_prob = {start: 1}
    exp_score = 0
    while len(states) > 0:
        state = states.pop()
        for i in range(len(outcomes)):
            res = outcomes[i](state)
            res_prob = state_prob[state]*batter_mapping[order[state[6]]][outcome_words[i]]
            # res_prob = state_prob[state]*batters[order[state[6]]][outcome_words[i]]
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
    print (exp_score, order)
    scores_list.append((exp_score, order))

scores_list.sort()
print scores_list




