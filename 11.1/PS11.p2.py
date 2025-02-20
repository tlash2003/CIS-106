names = ['Adams', 'Black', 'Cook', 'Dean', 'Elis', 'Flout', 'Gomez', 'Herrera', 'Indie', 'Jacobs']
scores = [100, 90, 89, 76, 96, 65, 49, 70, 60, 83]

def fnames(names, scores):
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

def fnames2(names, scores):
    names.reverse()
    scores.reverse()
    for name, score in zip(names, scores):
        print(f"{name}: {score}")
    return names, scores

# Example calls to the functions
fnames(names, scores)
fnames2(names, scores)
