def get_data():
    l = []
    r = []
    with open('12-1.txt', 'r') as f:
        for line in f:
            left, right = map(int, line.split())  # Split and convert to integers
            l.append(left)
            r.append(right)
        
        return l,r
    
if __name__ == "__main__":
    l, r = get_data()
    l.sort()
    r.sort()

    dists = []

    for left, right in zip(l, r):
        d = abs(right-left)
        dists.append(d)
    
    print("Sum of distances:", sum(dists))

    sims = []

    for num in l:
        c = r.count(num)
        sims.append(c*num)
    
    print("Sum of similarites:", sum(sims))
