states = ['DT', 'NN', 'VB']
start_p = {
    'DT': 0.6,
    'NN': 0.3,
    'VB': 0.1
}
trans_p = {
    'DT': {'DT': 0.05, 'NN': 0.85, 'VB': 0.10},
    'NN': {'DT': 0.10, 'NN': 0.30, 'VB': 0.60},
    'VB': {'DT': 0.40, 'NN': 0.50, 'VB': 0.10}
}
emit_p = {
    'DT': {'a': 0.5, 'the': 0.5},
    'NN': {'cat': 0.4, 'dog': 0.4, 'runs': 0.2},
    'VB': {'runs': 0.7, 'plays': 0.3}
}
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
    for st in states:
        V[0][st] = start_p[st] * emit_p[st].get(obs[0], 1e-6)
        path[st] = [st]
    for t in range(1, len(obs)):
        V.append({})
        new_path = {}
        for cur in states:
            best_prob, best_prev = max(
                (
                    V[t - 1][prev]
                    * trans_p[prev][cur]
                    * emit_p[cur].get(obs[t], 1e-6),
                    prev
                )
                for prev in states
            )
            V[t][cur] = best_prob
            new_path[cur] = path[best_prev] + [cur]
        path = new_path

    n = len(obs) - 1
    best_prob, best_state = max(
        (V[n][st], st) for st in states
    )
    return best_prob, path[best_state]
sentence = ['a', 'cat', 'runs']
prob, tags = viterbi(
    sentence, states, start_p, trans_p, emit_p
)
print("Sentence:", sentence)
print("Best Tag Sequence:", tags)
print(f"Probability: {prob:.6f}")